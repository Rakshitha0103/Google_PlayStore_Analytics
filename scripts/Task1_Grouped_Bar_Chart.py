import pandas as pd
import plotly.graph_objects as go
import datetime as dt
import pytz
import streamlit as st
import os

st.set_page_config(page_title="Google Playstore Analytics", layout="wide")
st.title("Google Playstore Analytics — Task 1")

file_path = r"C:\Users\rraks\Downloads\Google_PlayStore-main\Google_PlayStore-main\data\googleplaystore.csv"

if not os.path.exists(file_path):
    st.error("googleplaystore.csv not found at the specified path")
    st.stop()

df = pd.read_csv(file_path)

df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df = df.dropna(subset=['Rating'])

df['Size'] = df['Size'].replace('Varies with device', None)
df = df.dropna(subset=['Size'])

def size_to_mb(size):
    size = str(size).strip()
    if 'M' in size:
        return float(size.replace('M', ''))
    if 'k' in size or 'K' in size:
        return float(size.replace('k', '').replace('K', '')) / 1024
    return None

df['Size'] = df['Size'].apply(size_to_mb)
df = df.dropna(subset=['Size'])

df['Installs'] = df['Installs'].str.replace('+', '', regex=False)
df['Installs'] = df['Installs'].str.replace(',', '', regex=False)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')
df = df.dropna(subset=['Installs'])

df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')
df = df.dropna(subset=['Reviews'])

df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')
df = df.dropna(subset=['Last Updated'])

df_filtered = df[
    (df['Rating'] >= 4.0) &
    (df['Size'] >= 10) &
    (df['Last Updated'].dt.month == 1)
]

category_stats = df_filtered.groupby('Category').agg(
    Average_Rating=('Rating', 'mean'),
    Total_Reviews=('Reviews', 'sum'),
    Total_Installs=('Installs', 'sum')
).reset_index()

top10 = category_stats.sort_values(
    by='Total_Installs',
    ascending=False
).head(10)

ist = pytz.timezone('Asia/Kolkata')
current_time = dt.datetime.now(ist)
hour = current_time.hour

if 15 <= hour < 17:
    fig = go.Figure()

    fig.add_bar(
        x=top10['Category'],
        y=top10['Average_Rating'],
        name='Average Rating'
    )

    fig.add_bar(
        x=top10['Category'],
        y=top10['Total_Reviews'],
        name='Total Reviews'
    )

    fig.update_layout(
        title='Top 10 App Categories by Installs (Rating ≥ 4, Size ≥ 10MB, January Updates)',
        barmode='group',
        xaxis_title='Category',
        yaxis_title='Value',
        title_x=0.5
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Graph not available. Please view between 3 PM and 5 PM IST.")

st.write(f"Current IST Time: {current_time.strftime('%H:%M:%S')}")
