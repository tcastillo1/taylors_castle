import streamlit as st
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import plotly.express as px
import altair as alt

# Load iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target_names[iris.target]

# Matplotlib Line Chart
fig, ax = plt.subplots()
ax.plot(df['sepal length (cm)'], df['sepal width (cm)'], color='blue', alpha=0.7)
ax.set_title("Sepal Length vs Width (Matplotlib)")
ax.set_xlabel("Sepal Length (cm)")
ax.set_ylabel("Sepal Width (cm)")
st.pyplot(fig)

# Seaborn Line Chart
fig2, ax2 = plt.subplots()
sns.lineplot(x='sepal length (cm)', y='sepal width (cm)', data=df, hue='target', ax=ax2)
ax2.set_title("Sepal Length vs Width (Seaborn)")
st.pyplot(fig2)

# Plotly Line Chart
fig3 = px.line(df, x='sepal length (cm)', y='sepal width (cm)', color='target')
fig3.update_layout(title="Sepal Length vs Width (Plotly)", title_x=0.5)
st.plotly_chart(fig3)

# Altair Line Chart
chart = alt.Chart(df).mark_line().encode(
    x='sepal length (cm)',
    y='sepal width (cm)',
    color='target'
).properties(
    title="Sepal Length vs Width (Altair)"
)
st.altair_chart(chart, use_container_width=True)
