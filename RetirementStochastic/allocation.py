import numpy as np
from series import age_series
import pandas as pd


# this function produces a two-dimensional numpy array of shape 2 x n, where n represents
# the total number of periods in the projection. the first row represents the age array beginning
# at the starting age and ending after n yrs. the second row represents the allocation array that
# defines the pct of the investment fund to be invested in stocks at each period.
def allocation(
    start_pct=0.90,  # pct invested in equities at the start of the projection
    pct_5=0.55,  # pct invested in equities 5 yrs out from retirement
    end_pct=0.40,  # pct invested in equities at retirement
    age=30,  # age at the start of the projection
    ret_age=65,  # retirement age and the age at which the end allocation pct is reached
    freq=12,  # the number of periods in a year
    yrs=40,  # length of the projection in yrs
    **kwargs
):
    # income_period represents the number of income earning yrs
    income_period = ret_age - age

    # segment_one_length represents the number of periods at the initial constant allocation
    segment_one_length = 0 if income_period <= 30 else (income_period - 30) * freq

    # segment_four_length represents the number of periods at the ending constant allocation
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

    # setup allocation arrays
    segment_one_array = np.full(segment_one_length, start_pct)
    segment_two_array = np.linspace(
        segment_two_start_pct, segment_two_end_pct, segment_two_length
    )
    segment_three_array = np.linspace(
        segment_three_start_pct, segment_three_end_pct, segment_three_length
    )
    segment_four_array = np.full(segment_four_length, end_pct)

    # concatenate the arrays into one single array
    equity_allocation_array = np.concatenate(
        (segment_one_array, segment_two_array, segment_three_array, segment_four_array)
    )
    bond_allocation_array = 1 - equity_allocation_array

    # add the age, equity and bond allocation arrays into a single multidimensional array
    result_array = np.column_stack((equity_allocation_array, bond_allocation_array))
    df = pd.DataFrame(result_array, columns=["equity", "bond"])
    return df
