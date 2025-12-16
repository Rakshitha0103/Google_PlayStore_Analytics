import pandas as pd
import plotly.express as px
import streamlit as st
from datetime import datetime
import pytz
import os

st.set_page_config(page_title="Google Playstore Analytics — Task 2", layout="wide")
st.title("Google Playstore Analytics — Task 2")
st.subheader("Choropleth Map of Installs by Category")


possible_paths = [
    "data/googleplaystore.csv",
    "scripts/data/googleplaystore.csv",
    "../data/googleplaystore.csv",
    "./googleplaystore.csv"
]

file_path = None
for p in possible_paths:
    if os.path.exists(p):
        file_path = p
        break

if file_path is None:
    st.error("googleplaystore.csv was not found in expected directories.")
    st.stop()

df = pd.read_csv(file_path)


required_cols = ['Category', 'Installs']
if not all(col in df.columns for col in required_cols):
    st.error("Dataset is missing required columns: Category or Installs.")
    st.stop()


df = df.dropna(subset=['Category', 'Installs'])
df['Installs'] = (
    df['Installs']
    .astype(str)
    .str.replace('+', '', regex=False)
    .str.replace(',', '', regex=False)
)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')
df = df.dropna(subset=['Installs'])


df = df[~df['Category'].str.startswith(('A', 'C', 'G', 'S'))]
top_categories = df.groupby('Category')['Installs'].sum().nlargest(5).index
df_top = df[df['Category'].isin(top_categories)]

country_map = {
    'ENTERTAINMENT': 'USA',
    'TOOLS': 'IND',
    'LIFESTYLE': 'GBR',
    'BUSINESS': 'CAN',
    'FAMILY': 'AUS',
    'HEALTH_AND_FITNESS': 'BRA',
    'EDUCATION': 'JPN',
    'FINANCE': 'DEU',
    'TRAVEL_AND_LOCAL': 'FRA',
    'PHOTOGRAPHY': 'SGP'
}

df_top['Country'] = df_top['Category'].map(country_map).fillna('USA')
agg = df_top.groupby(['Country', 'Category'])['Installs'].sum().reset_index()

# time-based display control
ist = pytz.timezone("Asia/Kolkata")
current_time = datetime.now(ist).time()
start_time = datetime.strptime("18:00", "%H:%M").time()
end_time = datetime.strptime("20:00", "%H:%M").time()

st.write("Current IST time:", datetime.now(ist).strftime('%I:%M %p'))

if start_time <= current_time <= end_time:
    fig = px.choropleth(
        agg,
        locations='Country',
        color='Installs',
        hover_name='Category',
        color_continuous_scale='Viridis',
        projection='natural earth',
        title='Global Installs by App Category'
    )
    fig.update_layout(
        geo=dict(showframe=False, showcoastlines=True),
        coloraxis_colorbar=dict(title="Total Installs", tickformat=".0f")
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("The map is visible only between 6 PM and 8 PM IST.")
