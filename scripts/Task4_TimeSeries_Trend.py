import pandas as pd
import plotly.express as px
import streamlit as st
from datetime import datetime, timezone, timedelta
import os

st.set_page_config(page_title="Google Play Store Task 4", layout="wide")

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "data", "googleplaystore.csv")

if not os.path.exists(file_path):
    st.error("CSV file missing. Put googleplaystore.csv inside /data.")
    st.stop()

df = pd.read_csv(file_path)

df['Installs'] = df['Installs'].astype(str).str.replace('[+,]', '', regex=True)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')
df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')

df = df.dropna(subset=['Last Updated', 'Category', 'Installs'])

# ⛔️ NO WEIRD FILTERS
# ❌ No removing strings by starting letters
# ❌ No removing categories based on Hindi/Tamil mapping
# ❌ No removing thousands of rows by mistake

categories = df['Category'].unique()
selected_categories = st.sidebar.multiselect(
    "Select Categories",
    categories,
    default=list(categories)
)

min_date = df['Last Updated'].min()
max_date = df['Last Updated'].max()

start_date, end_date = st.sidebar.date_input("Select Date Range", [min_date, max_date])

filtered_df = df[
    (df['Category'].isin(selected_categories)) &
    (df['Last Updated'] >= pd.to_datetime(start_date)) &
    (df['Last Updated'] <= pd.to_datetime(end_date))
]

filtered_df['YearMonth'] = filtered_df['Last Updated'].dt.to_period('M')

agg_df = filtered_df.groupby(['YearMonth', 'Category'])['Installs'].sum().reset_index()
agg_df['YearMonth'] = agg_df['YearMonth'].dt.to_timestamp()

st.title("Google Play Store Install Trend Over Time")

fig = px.line(
    agg_df,
    x='YearMonth',
    y='Installs',
    color='Category',
    markers=True,
    title="Install Trends (Full Categories)"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Total Installs",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Top Apps")
top_apps = filtered_df.groupby(['Category','App'])['Installs'].sum().reset_index()
top_apps = top_apps.sort_values(['Category','Installs'], ascending=[True,False])
top5_apps = top_apps.groupby('Category').head(5)
st.dataframe(top5_apps)
