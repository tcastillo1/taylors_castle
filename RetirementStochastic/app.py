import pandas as pd
import streamlit as st
from functions import age_series
from main import retirement_analysis

st.title("Retirement Planner 📘")

# User inputs
age = st.sidebar.number_input("Enter your current age:", min_value=0, max_value=100, value=35)
ret_age = st.sidebar.number_input("Enter your retirement age:", min_value=0, max_value=100, value=65)
yrs = st.sidebar.number_input("Enter Number of Projection Years:", min_value=0, max_value=100, value=85-age)
salary = st.sidebar.number_input("Enter your current salary:", min_value=0, max_value=100000000, value=100000)
fund_value = st.sidebar.number_input("Enter your current retirement fund value:", min_value=0, max_value=100000000, value=100000)
ret_inc = st.sidebar.number_input("Enter your planned retirement income:", min_value=0, max_value=100000000, value=150000)

age_series = age_series(freq=1, age=age, yrs=yrs)

# Button to trigger analysis
if st.button("Run Simulation"):
    data = retirement_analysis(yrs, age, ret_age, salary, fund_value, ret_inc)
    data.index = age_series
    st.line_chart(data, x_label="Age", y_label="Fund Value")
    st.write(data)
    