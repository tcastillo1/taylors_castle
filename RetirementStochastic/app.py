# import numpy as np
import pandas as pd
# import pyesg
import streamlit as st
from functions import age_series
# from asset_mix import asset_mix
from RetirementStochastic.main import retirement_analysis


st.title("Retirement Planner 👦")

# User inputs
yrs = st.sidebar.number_input("Enter Number of Projection Years:", min_value=0, max_value=100, value=65)
age = st.sidebar.number_input("Enter your current age:", min_value=0, max_value=100, value=35)
ret_age = st.sidebar.number_input("Enter your retirement age:", min_value=0, max_value=100, value=50)
salary = st.sidebar.number_input("Enter your current salary:", min_value=0, max_value=100000000, value=100000)
fund_value = st.sidebar.number_input("Enter your current retirement fund value:", min_value=0, max_value=100000000, value=100000)
ret_inc = st.sidebar.number_input("Enter your planned retirement income:", min_value=0, max_value=100000000, value=100000)

age_series = age_series(freq=1, age=age, yrs=yrs)

# Button to trigger analysis
if st.button("Run Analysis"):
    data = retirement_analysis(yrs, age, ret_age, salary, fund_value, ret_inc)
    data.index = age_series
    st.write(data)
    st.line_chart(data)