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
# Розрахунок метрик
data['growth'] = data.groupby('state')['population'].pct_change() * 100
latest_year = data['year'].max()
latest_data = data[data['year'] == latest_year]

st.metric("📊 Середній приріст населення (%)", f"{data['growth'].mean():.2f}%")
st.metric("🏆 Штат-лідер за приростом", latest_data.sort_values('population', ascending=False).iloc[0]['state'])
import pandas as pd

# 1. Завантаження
data = pd.read_csv("us_population.csv")

# 2. Огляд структури
st.write("📄 Перші рядки даних", data.head())

# 3. Перевірка пропусків
st.write("🔍 Пропущені значення:", data.isna().sum())

# 4. Базова статистика
st.write("📊 Описова статистика:", data.describe())

# 5. Темп приросту
data['growth_rate'] = data.groupby('state')['population'].pct_change() * 100
import altair as alt

chart = alt.Chart(data).mark_line(point=True).encode(
    x="year:O",
    y="population:Q",
    color="state:N",
    tooltip=["state", "year", "population"]
)
st.altair_chart(chart, use_container_width=True)
top_states = data[data["year"] == 2019].sort_values("population", ascending=False).head(5)
st.bar_chart(top_states.set_index("state")["population"])
