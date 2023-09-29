import numpy as np
import pandas as pd
import random

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

    return arr
