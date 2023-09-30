import numpy as np
import pandas as pd
import random

def age_series(age = 30, periods_per_year = 12, years = 40):
    age_array = np.ones(periods_per_year * years + 1) / periods_per_year
    age_array[0] = age
    age_array = np.cumsum(age_array)
    age_series = pd.Series(age_array, name='age')
    return age_series

def salary_series(salary = 100000, salary_growth = .04, periods_per_year = 12, years = 40, age = 30, ret_age = 65):
    income_period = ret_age - age
    salary_growth_per_period = (1+salary_growth)**(1/periods_per_year)-1
    salary_growth_array = np.ones(periods_per_year * years + 1) * (1+salary_growth_per_period)
    salary_growth_array[0] = salary
    salary_array = np.cumprod(salary_growth_array)
    salary_array[(income_period*periods_per_year):] = 0
    salary_series = pd.Series(salary_array, name='salary')
    return salary_series

def invest_series(salary_s = None, invest_pct = .15, periods_per_year = 12, withdraw_amount = 100000, age = 30, ret_age = 65):
    income_period = ret_age - age
    if salary_s is None:
        salary_s = salary_series()
    invest_pct_per_period = invest_pct / periods_per_year
    invest = salary_s * invest_pct_per_period
    invest[income_period*periods_per_year:] = -1 * withdraw_amount / periods_per_year
    invest.name = 'invest'
    return invest

def mortality_sim(age = 32, ret_age = 65, sex = 'F', smoker = 'NS', n_scenarios = 1000, mi = .99):
    
    mort_df = pd.read_csv('MortalityTables/cso2017.csv')
    mort_df = mort_df.set_index(['Sex', 'SmokingStatus', 'IssueAge'])
    row = mort_df.loc[(sex, smoker, ret_age)]
    arr = np.empty(n_scenarios)

    for n in range(n_scenarios):
        d = 0
        j = ret_age
        i = row[d]/1000 * (mi ** (j - age))
        while random.random() > i:
            j += 1
            d +=1
            if d < len(row):  # Check if index is out of range
                i = row[d]/1000 * (mi ** (j - age))
            else:
                break
        arr[n] = j

    df = pd.DataFrame(arr, columns=['age_at_death'])

    return df