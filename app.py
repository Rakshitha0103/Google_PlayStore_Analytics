

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime, timezone, timedelta
import pytz
import os
import re


st.set_page_config(page_title="Google Playstore Analytics", layout="wide")
st.title("Google Playstore Analytics Dashboard")



DATA_PATH = os.path.join("data", "googleplaystore.csv")

if not os.path.exists(DATA_PATH):
    st.error("googleplaystore.csv not found inside the data folder")
    st.stop()

df = pd.read_csv(DATA_PATH)

df.columns = [c.strip() for c in df.columns]



def parse_installs(x):
    try:
        return float(str(x).replace('+','').replace(',',''))
    except:
        return np.nan


def parse_size(x):
    try:
        if pd.isna(x) or str(x).lower() == 'varies with device':
            return np.nan
        x = str(x).lower()
        if x.endswith('m'):
            return float(x[:-1])
        if x.endswith('k'):
            return float(x[:-1]) / 1024
        return float(x)
    except:
        return np.nan


def parse_android(x):
    if pd.isna(x):
        return np.nan
    m = re.search(r"(\d+(\.\d+)?)", str(x))
    return float(m.group(1)) if m else np.nan


def parse_price(x):
    try:
        return float(str(x).replace('$',''))
    except:
        return 0.0


df['Installs'] = df['Installs'].apply(parse_installs)
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')
df['Size_MB'] = df['Size'].apply(parse_size)
df['Android_Ver_Num'] = df['Android_Ver'].apply(parse_android) if 'Android_Ver' in df else np.nan
df['Price_Num'] = df['Price'].apply(parse_price) if 'Price' in df else 0.0

df = df.dropna(subset=['Category','Installs'])

ist = pytz.timezone('Asia/Kolkata')
current_time = datetime.now(ist)
st.write(f"Current IST Time: {current_time.strftime('%I:%M %p')}")


st.header("Task 1: Top Categories – Ratings vs Reviews")

if 15 <= current_time.hour < 17:
    df1 = df.dropna(subset=['Rating','Size_MB','Last Updated'])
    df1['Last Updated'] = pd.to_datetime(df1['Last Updated'], errors='coerce')

    df1 = df1[(df1['Rating'] >= 4.0) & (df1['Size_MB'] >= 10) & (df1['Last Updated'].dt.month == 1)]

    agg1 = df1.groupby('Category').agg(
        Avg_Rating=('Rating','mean'),
        Total_Reviews=('Reviews','sum'),
        Total_Installs=('Installs','sum')
    ).reset_index().sort_values('Total_Installs', ascending=False).head(10)

    fig1 = go.Figure()
    fig1.add_bar(x=agg1['Category'], y=agg1['Avg_Rating'], name='Average Rating')
    fig1.add_bar(x=agg1['Category'], y=agg1['Total_Reviews'], name='Total Reviews')

    fig1.update_layout(barmode='group', title='Top 10 Categories (January Updates)')
    st.plotly_chart(fig1, use_container_width=True)
else:
    st.info("Task 1 visible between 3 PM and 5 PM IST")



st.header("Task 2: Global Installs Choropleth")

if 18 <= current_time.hour <= 20:
    df2 = df.copy()
    df2 = df2[~df2['Category'].str.startswith(('A','C','G','S'))]

    top5 = df2.groupby('Category')['Installs'].sum().nlargest(5).index
    df2 = df2[df2['Category'].isin(top5)]

    country_map = {
        'ENTERTAINMENT': 'USA', 'TOOLS': 'IND', 'BUSINESS': 'CAN',
        'FAMILY': 'AUS', 'LIFESTYLE': 'GBR'
    }

    df2['Country'] = df2['Category'].map(country_map).fillna('USA')
    agg2 = df2.groupby(['Country','Category'])['Installs'].sum().reset_index()

    fig2 = px.choropleth(
        agg2,
        locations='Country',
        color='Installs',
        hover_name='Category',
        projection='natural earth'
    )
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("Task 2 visible between 6 PM and 8 PM IST")



st.header("Task 3: Avg Installs vs Revenue (Free vs Paid)")

if 13 <= current_time.hour < 14:
    df3 = df.copy()
    df3['Revenue'] = df3['Installs'] * df3['Price_Num']
    df3['App_Len'] = df3['App'].astype(str).apply(len)

    df3 = df3[(df3['Installs'] >= 10000) &
              (df3['Revenue'] >= 10000) &
              (df3['Android_Ver_Num'] > 4.0) &
              (df3['Size_MB'] > 15) &
              (df3['Content Rating'] == 'Everyone') &
              (df3['App_Len'] <= 30)]

    top3 = df3.groupby('Category')['Installs'].sum().nlargest(3).index
    df3 = df3[df3['Category'].isin(top3)]

    summary = df3.groupby(['Category','Type']).agg(
        Avg_Installs=('Installs','mean'),
        Avg_Revenue=('Revenue','mean')
    ).reset_index()

    fig3 = make_subplots(specs=[[{"secondary_y": True}]])

    fig3.add_bar(x=summary['Category'], y=summary['Avg_Installs'], name='Avg Installs')
    fig3.add_scatter(x=summary['Category'], y=summary['Avg_Revenue'], name='Avg Revenue', secondary_y=True)

    st.plotly_chart(fig3, use_container_width=True)
else:
    st.info("Task 3 visible between 1 PM and 2 PM IST")



st.header("Task 4: Install Trends Over Time")

df4 = df.dropna(subset=['Last Updated'])
df4['Last Updated'] = pd.to_datetime(df4['Last Updated'], errors='coerce')
df4['YearMonth'] = df4['Last Updated'].dt.to_period('M').dt.to_timestamp()

agg4 = df4.groupby(['YearMonth','Category'])['Installs'].sum().reset_index()

fig4 = px.line(agg4, x='YearMonth', y='Installs', color='Category', markers=True)
st.plotly_chart(fig4, use_container_width=True)



st.header("Task 5: Bubble Chart – Size vs Rating")

if 17 <= current_time.hour <= 19:
    df5 = df.dropna(subset=['Rating','Reviews','Installs','Size_MB'])
    df5 = df5[(df5['Rating'] > 3) & (df5['Reviews'] > 50) & (df5['Installs'] > 5000)]

    fig5 = px.scatter(
        df5,
        x='Size_MB',
        y='Rating',
        size='Installs',
        color='Category',
        hover_name='App'
    )
    st.plotly_chart(fig5, use_container_width=True)
else:
    st.info("Task 5 visible between 5 PM and 7 PM IST")



st.header("Task 6: Cumulative Installs Stacked Area")

if 16 <= current_time.hour < 18:
    df6 = df.dropna(subset=['Last Updated'])
    df6['Last Updated'] = pd.to_datetime(df6['Last Updated'], errors='coerce')
    df6['YearMonth'] = df6['Last Updated'].dt.to_period('M').astype(str)

    agg6 = df6.groupby(['YearMonth','Category'])['Installs'].sum().reset_index()
    agg6['Cumulative'] = agg6.groupby('Category')['Installs'].cumsum()

    fig6 = go.Figure()
    for cat in agg6['Category'].unique():
        data = agg6[agg6['Category'] == cat]
        fig6.add_trace(go.Scatter(
            x=data['YearMonth'],
            y=data['Cumulative'],
            stackgroup='one',
            name=cat
        ))

    st.plotly_chart(fig6, use_container_width=True)
else:
    st.info("Task 6 visible between 4 PM and 6 PM IST")
