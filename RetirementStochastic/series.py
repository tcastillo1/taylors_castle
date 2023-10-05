import numpy as np
import pandas as pd
import random


def age_series(age=30, freq=12, yrs=40, **kwargs):
    """Produces an array that denotes the age at each period"""
    age_array = np.ones(freq * yrs + 1) / freq
    age_array[0] = age
    age_array = np.cumsum(age_array)
    age_s = pd.Series(age_array, name="age")
    return age_s


def salary_series(
    salary=100000, salary_growth=0.04, freq=12, yrs=40, age=30, ret_age=65, **kwargs
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
    freq=12,
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
        salary_s = salary_series()
    invest_pct_per_period = invest_pct / freq
    invest = salary_s * invest_pct_per_period
    invest[income_period * freq :] = -1 * ret_inc / freq
    invest.name = "invest"
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
