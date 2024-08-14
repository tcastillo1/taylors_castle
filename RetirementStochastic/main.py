import os
import numpy as np
import pandas as pd
import pyesg
import streamlit as st
from functions import invest_series, salary_series, age_series, mortality_sim
from asset_mix import asset_mix

class Retirement_Analysis:
    def __init__(self, yrs, age, ret_age, salary, fund_value, ret_inc):
        self.yrs = yrs
        self.age = age
        self.ret_age = ret_age
        self.salary = salary
        self.fund_value = fund_value
        self.ret_inc = ret_inc
        self.fund_projection()

    def fund_projection(self):
        # projection inputs
        yrs = self.yrs              # number of yrs to project
        freq = 1                    # number of periods per year
        n_scen = 1000                # number of scenarios

        # demographic inputs
        age = self.age               # starting age
        sex = 'M'                    # sex
        smoker = 'NS'                # SM for smoker NS for non-smoker
        ret_age = self.ret_age       # age at which time investments into retirement fund cease and withdrawals begin
        mi = .99                     # mortality improvement

        # fund inputs
        fund_value = self.fund_value # starting value of retirement fund
        ret_inc = self.ret_inc       # desired annual retirement income
        salary = self.salary         # starting salary
        salary_growth = .045         # annual salary growth rate
        invest_pct = .15             # pct of salary to be invested in retirement
        inflation = .02              # annual inflation assumption
        s_pct = .80                  # starting pct of funds to be invested in stocks
        b_pct = 1 - s_pct            # starting pct of funds to be invested in bonds
        pct_5 = .55                  # pct of funds to be invested in stocks 5 yrs out from retirement
        s_pct_end = .1               # pct of funds to be invested in stocks at and during retirement
        b_pct_end = 1 - s_pct_end    # pct of funds to be invested in bonds at and during retirement

        # model inputs
        x0 = 100.0                  # the start value of our process
        dt = 1/freq                 # the length of each timestep in yrs
        n_steps = freq * yrs        # the number of time steps per scenario
        # random_state = 259        # optional random_state for reproducibility

        config = {
            'yrs':yrs,
            'freq':freq,
            'n_scen':n_scen,
            'age':age,
            'sex':sex,
            'smoker':smoker,
            'ret_age':ret_age,
            'mi':mi,   
            'fund_value':fund_value,
            'ret_inc':ret_inc,
            'salary':salary,
            'salary_growth':salary_growth,
            'invest_pct':invest_pct,
            'inflation':inflation,
            's_pct':s_pct,
            'b_pct':b_pct,
            'pct_5':pct_5,
            's_pct_end':s_pct_end,
            'b_pct_end':b_pct_end,
            'x0':x0,
            'dt':dt,
            'n_steps':n_steps
        }

        # instantiate a new model with the required parameters
        stock_model = pyesg.GeometricBrownianMotion(mu=0.10, sigma=0.15)
        bond_model = pyesg.GeometricBrownianMotion(mu=0.05, sigma=0.05)

        # run model for both equities and bonds
        s_model_results = stock_model.scenarios(x0, dt, n_scen, n_steps)
        b_model_results = bond_model.scenarios(x0, dt, n_scen, n_steps)

        # create stock and bond index return arrays. 
        stock_return = s_model_results[:, 1:] / s_model_results[:, :-1]
        bond_return = b_model_results[:, 1:] / b_model_results[:, :-1]

        # set beginning of fund array to starting investment value
        stock_array = np.insert(stock_return, 0, fund_value * s_pct, axis=1)
        bond_array = np.insert(bond_return, 0, fund_value * b_pct, axis=1)

        # the last return value is not used so we add a 1 to the end to return the array to its original length
        ones_to_append = np.ones((stock_return.shape[0], 1), dtype=int)
        stock_return = np.append(stock_return, ones_to_append, axis=1)
        bond_return = np.append(bond_return, ones_to_append, axis=1)

        # create pandas series for various calcs
        salary_s = salary_series(**config)

        invest_s = invest_series(salary_s=salary_s, **config)
        invest_s = np.tile(invest_s, (n_scen, 1))

        mortality_s = mortality_sim(**config)

        asset_mix_sb = asset_mix(**config)
        asset_mix_s = np.tile(asset_mix_sb['stock'], (n_scen, 1))
        asset_mix_b = np.tile(asset_mix_sb['bond'], (n_scen, 1))

        # this is where the magic happens
        # calc the fund value at each point in time, credit interest, add/withdraw from fund
        for s, b, inv, alloc_s, alloc_b in zip(stock_array, bond_array, invest_s, asset_mix_s, asset_mix_b):
            for i in range(1, len(s)):      
                s[i] = s[i-1] * s[i]                            # stock fund @t = stock fund @t-1 * stock return
                b[i] = b[i-1] * b[i]                          # bond fund @t = bond fund @t-1 * bond return
                total_fund = s[i] + b[i] + inv[i-1]/freq   # total fund = stock + bond fund +/- investment
                s[i] = total_fund * alloc_s[i]                     # reallocate fund value to stock fund
                b[i] = total_fund * alloc_b[i]                     # reallocate fund value to bond fund

        total_fund = stock_array + bond_array

        df = pd.DataFrame(total_fund.T)

        # Extract the final row
        final_row = df.iloc[-1, :]

        # Rank the columns based on the values in the final row
        ranked_columns = final_row.rank().sort_values()

        # Determine the 5th, 50th, and 95th percentiles
        n = len(ranked_columns)
        p5 = int(0.05 * (n - 1))
        p50 = int(0.50 * (n - 1))
        p95 = int(0.95 * (n - 1))

        percentile_indices = [p5, p50, p95]
        percentile_columns = ranked_columns.iloc[percentile_indices].index

        # Select the percentile columns from the dataframe
        selected_df = df[percentile_columns]

        # Rename columns
        selected_df.columns = ["5th Percentile", "50th Percentile", "95th Percentile"]

        return selected_df

def retirement_analysis(yrs, age, ret_age, salary, fund_value, ret_inc):
    analysis = Retirement_Analysis(yrs, age, ret_age, salary, fund_value, ret_inc)
    return analysis.fund_projection()