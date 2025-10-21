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
df_reshaped = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')
df_reshaped.rename(columns={'Rank': 'year', 'State': 'state', 'Population': 'population'}, inplace=True)

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

#теплова карта

def make_heatmap(input_df, input_y, input_x, input_color, input_color_them
heatmap =alt.Chart(input_df).mark_rect().encode(y=alt. Y(f'(input_y):0', axis=alt.Axis (title="year", titleFonts
x=alt.X(f'(input_x}:0', axis=alt.Axis(title="", titleFontSize=
color=alt. Color (f'maxfinput_color]) :0',
Legend=None,
scale=alt.Scale(scheme=input_color_theme)) ,
stroke=alt.value('black'),
strokewidth=alt.value(0.25),
) .properties (width=900
). configure_axis (
LabelFontSize=12,
titleFontSize=12
# height=300
return heatmap
st.plotly_chart(fig, use_container_width=True)

# --- Підсумкова метрика ---
total_population = int(df_selected_year['population'].sum())
st.metric(label=f"Total US population in {selected_year}", value=f"{total_population:,}")

#хороплетна карта
def make_heatmap(input_df, input_y, input_x, input_color, input_color_them
heatmap = alt. Chart (input_df) mark_rect) . encode (
y=alt. Y(f'(input_y):0', axis=alt.Axis (title="year", titleFonts
x=alt.X(f'(input_x}:0', axis=alt.Axis(title="", titleFontSize=
color=alt. Color (f'maxfinput_color]) :0',
Legend=None,
scale=alt.Scale(scheme=input_color_theme)) ,
stroke=alt.value('black'),
strokewidth=alt.value(0.25),
) .properties (width=900
). configure_axis (
LabelFontSize=12,
titleFontSize=12
# height=300
return heatmap
