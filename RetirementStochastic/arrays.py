import numpy as np

def age_array(age = 30, periods_per_year = 12, years = 40):
    age_array = np.ones(periods_per_year * years + 1) / periods_per_year
    age_array[0] = age
    age_array = np.cumsum(age_array)
    return age_array

def salary_array(salary = 100000, salary_growth = .04, periods_per_year = 12, years = 40):
    salary_growth_per_period = (1+salary_growth)**(1/periods_per_year)-1
    salary_growth_array = np.ones(periods_per_year * years) * (1+salary_growth_per_period)
    salary_growth_array[0] = salary
    salary_array = np.cumprod(salary_growth_array)
    return salary_array

def invest_array(salary_array = salary_array(), invest_pct = .15, periods_per_year = 12):
    invest_pct_per_period = invest_pct / periods_per_year
    invest_array = salary_array * invest_pct_per_period
    return invest_array