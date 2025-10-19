import streamlit as st
import pandas as pd
import altair as alt

st.title("📊 Population Dashboard: USA 2010–2019")

# Завантаження даних
data = pd.read_csv("https://raw.githubusercontent.com/datasets/population/master/data/population.csv")
data = data[data['Country Name'] == 'United States']
data = data[(data['Year'] >= 2010) & (data['Year'] <= 2019)]

# Візуалізація
chart = alt.Chart(data).mark_line(point=True).encode(
    x="Year:O",
    y="Value:Q",
    tooltip=["Year", "Value"]
)
st.altair_chart(chart, use_container_width=True)

st.metric("📈 Середнє населення", f"{data['Value'].mean():,.0f}")
