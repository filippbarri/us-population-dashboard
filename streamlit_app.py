# Імпорт бібліотек
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

# --- Конфігурація сторінки ---
st.set_page_config(
    page_title="US Population Dashboard",
    page_icon="🌎",
    layout="wide",
    initial_sidebar_state="expanded"
)

alt.themes.enable("dark")

# --- Завантаження даних ---
df_reshaped = pd.read_csv('data/us-population-2010-2019-reshaped.csv')

# --- Бокова панель ---
with st.sidebar:
    st.title("📊 US Population Dashboard")

    # список років у зворотному порядку
    year_list = list(df_reshaped['year'].unique())[::-1]

    # вибір року
    selected_year = st.selectbox('Select a year', year_list, index=len(year_list)-1)
    df_selected_year = df_reshaped.query('year == @selected_year')

    # вибір кольорової теми
    color_theme_list = ['blues', 'viridis', 'greens', 'inferno', 'magma', 'plasma']
    color_theme = st.selectbox('Select color theme', color_theme_list)

# --- Основна частина сторінки ---
st.title(f"📈 Population of US States in {selected_year}")

# Візуалізація Altair
chart = alt.Chart(df_selected_year).mark_bar().encode(
    x=alt.X('state:N', sort='-y', title='State'),
    y=alt.Y('population:Q', title='Population'),
    color=alt.Color('population:Q', scale=alt.Scale(scheme=color_theme))
).properties(
    width=900,
    height=500
)

st.altair_chart(chart, use_container_width=True)

# Візуалізація Plotly (додатково)
fig = px.choropleth(
    df_selected_year,
    locations='state',
    locationmode="USA-states",
    color='population',
    color_continuous_scale=color_theme,
    scope="usa",
    title=f"US States Population in {selected_year}"
)

st.plotly_chart(fig, use_container_width=True)

# --- Підсумкова метрика ---
total_population = int(df_selected_year['population'].sum())
st.metric(label=f"Total US population in {selected_year}", value=f"{total_population:,}")
