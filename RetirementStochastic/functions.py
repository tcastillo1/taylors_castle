import numpy as np
import pandas as pd
import random
import pyesg

DEFAULT_CONFIG = {
    "yrs": 40,
    "freq": 12,
    "n_scen": 10,
    "age": 30,
    "sex": "M",
    "smoker": "NS",
    "ret_age": 65,
    "mi": 0.99,
    "fund_value": 100000,
    "ret_inc": 1000000,
    "salary": 100000,
    "salary_growth": 0.045,
    "invest_pct": 0.15,
    "inflation": 0.02,
    "s_pct": 0.80,
    "pct_5": 0.55,
    "s_pct_end": 0.2,
}


def age_series(age, yrs, freq=1, **kwargs):
    """Produces an array that denotes the age at each period"""
    age = age
    yrs = yrs
    age_array = np.ones(freq * yrs + 1) / freq
    age_array[0] = age
    age_array = np.cumsum(age_array)
    age_s = pd.Series(age_array, name="age")
    return age_s


def salary_series(
    salary=100000, salary_growth=0.04, freq=1, yrs=65, age=30, ret_age=65, **kwargs
):
    """Produces an array that determines the salary at each period."""
    income_period = ret_age - age
    salary_growth_per_period = (1 + salary_growth) ** (1 / freq) - 1
    salary_growth_array = np.ones(freq * yrs + 1) * (1 + salary_growth_per_period)
    salary_growth_array[0] = salary
    salary_array = np.cumprod(salary_growth_array)
    salary_array[(income_period * freq) :] = 0
    salary_s = pd.Series(salary_array, name="salary")
    return salary_s


def invest_series(
    salary_s=None,
    invest_pct=0.15,
    freq=1,
    ret_inc=100000,
    age=30,
    ret_age=65,
    **kwargs
):
    """
    Produces an array that determines the amount to be invested or withdrawn at each period. For a
    given period, if age < retirement age, investments will be made. Once retirement is reached,
    investments will cease and withdrawals will begin.
    """
    income_period = ret_age - age
    if salary_s is None:
        salary_s = salary_series(**kwargs)
    invest_pct_per_period = invest_pct / freq
    invest = salary_s * invest_pct_per_period
    invest[income_period * freq :] = -1 * ret_inc / freq
    invest.name = "invest"
       # Ensure invest is a pandas Series
    if not isinstance(invest, pd.Series):
        invest = pd.Series(invest)
    # salary_s = pd.Series(salary_array, name="salary")
    return invest


# simulate mortality for n scenarios starting at retirement
# mi is mortality improvement
def mortality_sim(
    age=32, ret_age=65, sex="F", smoker="NS", n_scen=1000, mi=0.99, **kwargs
):
    """
    Runs a monte carlo simulation on n scenarios to determine age at death. Each item in the
    resulting array represent the age at death for that scenario.
    """
    mort_df = pd.read_csv("MortalityTables/cso2017.csv")
    mort_df = mort_df.set_index(["Sex", "SmokingStatus", "IssueAge"])
    row = mort_df.loc[(sex, smoker, ret_age)]
    arr = np.empty(n_scen)

    for n in range(n_scen):
        d = 0
        j = ret_age
        i = row[d] / 1000 * (mi ** (j - age))
        while random.random() > i:
            j += 1
            d += 1
            if d < len(row):
                i = row[d] / 1000 * (mi ** (j - age))
            else:
                break
        arr[n] = j

    df = pd.DataFrame(arr, columns=["age_at_death"])

    return df


def asset_mix(
    start_pct=0.90,  # pct invested in equities at the start of the projection
    pct_5=0.55,  # pct invested in equities 5 yrs out from retirement
    end_pct=0.40,  # pct invested in equities at retirement
    age=30,  # age at the start of the projection
    ret_age=65,  # retirement age and the age at which the end asset_mix pct is reached
    freq=12,  # the number of periods in a year
    yrs=40,  # length of the projection in yrs
    **kwargs
):
    """
    Produces a 2 x n multidimensional array that defines the asset mix between stocks and bonds at
    a given period. the sum of the two arrays is always equal to 1.0.
    """
    # income_period represents the number of income earning yrs
    income_period = ret_age - age

    # segment_one_length represents the number of periods at the initial constant asset_mix
    segment_one_length = 0 if income_period <= 30 else (income_period - 30) * freq

    # segment_four_length represents the number of periods at the ending constant asset_mix
    segment_four_length = (
        0 if yrs <= income_period else (yrs - income_period) * freq + 1
    )

    # calculate segment_two_length, start pct and end pct
    # segment two represents the period from 30 to 5 yrs from retirement
    segment_two_slope = (pct_5 - start_pct) / (25 * freq)
    segment_two_end_pct = pct_5 - segment_two_slope
    if income_period <= 5:
        segment_two_length = 0
        segment_two_start_pct = 0
    elif income_period >= 30:
        segment_two_length = 25 * freq
        segment_two_start_pct = start_pct
    else:
        segment_two_length = (income_period - 5) * freq
        segment_two_start_pct = pct_5 + ((income_period - 5) / 25 * (start_pct - pct_5))

    # calculate segment_three_length, start pct and end pct
    # segment three represents the period from 5 to 0 yrs from retirement
    segment_three_slope = (end_pct - pct_5) / (5 * freq)
    segment_three_end_pct = end_pct - segment_three_slope
    if income_period >= 5:
        segment_three_length = 5 * freq
        segment_three_start_pct = pct_5
    else:
        segment_three_length = income_period * freq
        segment_three_start_pct = end_pct + (income_period / 5 * (pct_5 - end_pct))

    # setup asset_mix arrays
    segment_one_array = np.full(segment_one_length, start_pct)
    segment_two_array = np.linspace(
        segment_two_start_pct, segment_two_end_pct, segment_two_length
    )
    segment_three_array = np.linspace(
        segment_three_start_pct, segment_three_end_pct, segment_three_length
    )
    segment_four_array = np.full(segment_four_length, end_pct)

    # concatenate the arrays into one single array
    stock_asset_mix_array = np.concatenate(
        (segment_one_array, segment_two_array, segment_three_array, segment_four_array)
    )
    bond_asset_mix_array = 1 - stock_asset_mix_array

    # add the stock and bond asset_mix arrays into a single multidimensional array
    result_array = np.column_stack((stock_asset_mix_array, bond_asset_mix_array))
    df = pd.DataFrame(result_array, columns=["stock", "bond"])

    return df


# def fund_projection(**kwargs):
#     config = DEFAULT_CONFIG.copy()
#     config.update(kwargs)

#     s_pct = config["s_pct"]
#     freq = config["freq"]
#     yrs = config["yrs"]
#     fund_value = config["fund_value"]

#     b_pct = 1 - s_pct
#     n_steps = freq * yrs
#     dt = 1 / freq
#     x0 = 100
#     n_scen = yrs * freq

#     # instantiate a new model with the required parameters
#     stock_model = pyesg.GeometricBrownianMotion(mu=0.10, sigma=0.15)
#     bond_model = pyesg.GeometricBrownianMotion(mu=0.05, sigma=0.05)

#     # run model for both equities and bonds
#     s_model_results = stock_model.scenarios(x0, dt, n_scen, n_steps)
#     b_model_results = bond_model.scenarios(x0, dt, n_scen, n_steps)

#     # create stock and bond index return arrays.
#     stock_return = s_model_results[:, 1:] / s_model_results[:, :-1]
#     bond_return = b_model_results[:, 1:] / b_model_results[:, :-1]

#     # set beginning of fund array to starting investment value
#     stock_array = np.insert(stock_return, 0, fund_value * s_pct, axis=1)
#     bond_array = np.insert(bond_return, 0, fund_value * b_pct, axis=1)

#     # the last return value is not used so we add a 1 to the end to return the array to its original length
#     ones_to_append = np.ones((stock_return.shape[0], 1), dtype=int)
#     stock_return = np.append(stock_return, ones_to_append, axis=1)
#     bond_return = np.append(bond_return, ones_to_append, axis=1)

#     # create pandas series for various calcs
#     invest_s = invest_series(**config)
#     asset_mix_s = asset_mix(**config)

#     # this is where the magic happens
#     # calc the fund value at each point in time, credit interest, add/withdraw from fund
#     for s, b, inv, alloc_s, alloc_b in zip(
#         stock_array, bond_array, invest_s, asset_mix_s["stock"], asset_mix_s["bond"]
#     ):
#         for i in range(1, len(s)):
#             s[i] = s[i - 1] * s[i]  # stock fund @t = stock fund @t-1 * stock return
#             b[i] = b[i - 1] * b[i]  # bond fund @t = bond fund @t-1 * bond return
#             total_fund = (
#                 s[i] + b[i] + inv[i - 1] / freq
#             )  # total fund = stock + bond fund +/- investment
#             s[i] = total_fund * alloc_s  # reallocate fund value to stock fund
#             b[i] = total_fund * alloc_b  # reallocate fund value to bond fund

#     total_fund = stock_array + bond_array
#     df = pd.DataFrame(total_fund.T)

#     return df
