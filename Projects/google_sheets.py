import gspread
import pandas as pd
import seaborn as sns
import matplotlib
import datetime as dt

sa = gspread.service_account(
    filename="/Users/taylorcastillo/Documents/Python/keys/service_account.json")

sh = sa.open("Calorie Tracker")
wks = sh.worksheet("Form Responses 1")

df = pd.DataFrame(wks.get_all_values())
df.columns = df.iloc[0]

print(df["Timestamp"].to_string())
# print(df[0:5])

# print(df['Timestamp'])
# print(df.mean("Weight"))
sns.set_theme()

# Create a visualization
df_graph = sns.relplot(
    data=df,
    x=dt.datetime.strptime("Timestamp", "m/d/Y").strftime("%m/%d/%Y"), y="Weight", col="User"
    # , col="User"
)

matplotlib.pyplot.show()
# print(df.head())
