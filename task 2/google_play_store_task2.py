import pandas as pd
import plotly.express as px
import streamlit as st
from datetime import datetime
import pytz

ist = pytz.timezone("Asia/Kolkata")
current_time = datetime.now(ist).time()

file_path = r"C:\Users\rraks\OneDrive\Desktop\Google_PlayStore_Analytics\task 2\googleplaystore.csv"

try:
    df = pd.read_csv(file_path)
except pd.errors.EmptyDataError:
    st.error("The CSV file is empty or corrupted.")
    st.stop()
except FileNotFoundError:
    st.error("File not found. Please check the path.")
    st.stop()

required_cols = ['Category', 'Installs']
if not all(col in df.columns for col in required_cols):
    st.error("The dataset is missing required columns (Category, Installs).")
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

start_time = datetime.strptime("18:00", "%H:%M").time()
end_time = datetime.strptime("20:00", "%H:%M").time()

st.title("Google Play Store Analytics ")
st.subheader("Interactive Choropleth Map of Global Installs by Category")
st.write(f"Current IST time: {datetime.now(ist).strftime('%I:%M %p')}")

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
