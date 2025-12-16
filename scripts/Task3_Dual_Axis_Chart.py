import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
import re

st.set_page_config(page_title="Google Play Store Analytics — Task 3", layout="wide")
st.title("Google Play Store Analytics — Task 3")
st.subheader("Average Installs vs Revenue (Free vs Paid)")

def parse_number(x):
    if pd.isna(x):
        return np.nan
    x = str(x).replace('+','').replace(',','').replace('$','').strip().lower()
    try:
        if x.endswith('k'):
            return float(x[:-1]) * 1_000
        if x.endswith('m'):
            return float(x[:-1]) * 1_000_000
        return float(x)
    except:
        return np.nan

def parse_android_ver(s):
    if pd.isna(s):
        return np.nan
    m = re.search(r"(\d+(\.\d+)?)", str(s))
    return float(m.group(1)) if m else np.nan

def parse_size(s):
    if pd.isna(s):
        return np.nan
    s = str(s).lower().strip()
    if s == "varies with device":
        return np.nan
    try:
        if s.endswith('m'):
            return float(s[:-1])
        if s.endswith('k'):
            return float(s[:-1]) / 1000
        return float(s)
    except:
        return np.nan

def load_data():
    possible_paths = [
        "data/googleplaystore.csv",
        "scripts/data/googleplaystore.csv",
        "./googleplaystore.csv"
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return pd.read_csv(path), path
    return None, None

df, csv_path = load_data()

if df is None:
    st.error("googleplaystore.csv not found in any valid directory.")
    st.stop()

df.columns = [c.strip() for c in df.columns]

df['Installs_parsed'] = df['Installs'].apply(parse_number)
df['Android_ver_parsed'] = df['Android_Ver'].apply(parse_android_ver) if 'Android_Ver' in df else np.nan
df['Size_M'] = df['Size'].apply(parse_size) if 'Size' in df else np.nan

if 'Revenue' in df.columns:
    df['Revenue_parsed'] = df['Revenue'].apply(parse_number)
elif 'Price' in df.columns:
    df['Price_parsed'] = df['Price'].apply(parse_number)
    df['Revenue_parsed'] = df['Installs_parsed'] * df['Price_parsed']
else:
    df['Revenue_parsed'] = np.nan

df['App_name_len'] = df['App'].astype(str).apply(len)
df['Type'] = df.get('Type', 'Free').fillna('Free')

def apply_filters(df):
    df = df.copy()
    for col in ['Installs_parsed','Revenue_parsed','Android_ver_parsed','Size_M']:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    min_installs = df['Installs_parsed'].quantile(0.25)
    min_revenue = df['Revenue_parsed'].quantile(0.25)
    min_size = df['Size_M'].quantile(0.25)

    return df[
        (df['Installs_parsed'] >= min_installs) &
        (df['Revenue_parsed'] >= min_revenue) &
        (df['Android_ver_parsed'] > 4.0) &
        (df['Size_M'] >= min_size) &
        (df['App_name_len'] <= 30)
    ]

filtered = apply_filters(df)

if filtered.empty:
    st.warning("No data left after filtering. Reverting to raw dataset.")
    filtered = df.copy()

if 'Category' not in filtered.columns:
    st.error("Column 'Category' not found in dataset.")
    st.stop()

top3 = filtered.groupby('Category')['Installs_parsed'].sum().nlargest(3).index.tolist()
df_top3 = filtered[filtered['Category'].isin(top3)]

summary = (
    df_top3.groupby(['Category','Type'])
    .agg(Avg_Installs=('Installs_parsed','mean'),
         Avg_Revenue=('Revenue_parsed','mean'))
    .reset_index()
)

cats = summary['Category'].unique().tolist()
fig = make_subplots(specs=[[{"secondary_y": True}]])
x, installs, revenue = [], [], []

for cat in cats:
    for typ in ['Free', 'Paid']:
        row = summary[(summary['Category']==cat) & (summary['Type']==typ)]
        x.append(f"{cat} - {typ}")
        installs.append(row['Avg_Installs'].iloc[0] if not row.empty else 0)
        revenue.append(row['Avg_Revenue'].iloc[0] if not row.empty else 0)

fig.add_trace(go.Bar(x=x, y=installs, name='Avg Installs'), secondary_y=False)
fig.add_trace(go.Scatter(x=x, y=revenue, mode='lines+markers', name='Avg Revenue'), secondary_y=True)
fig.update_layout(title='Average Installs vs Average Revenue (Free vs Paid Apps)', xaxis_title='Category - Type')
fig.update_yaxes(title_text="Average Installs", secondary_y=False)
fig.update_yaxes(title_text="Average Revenue", secondary_y=True)
st.plotly_chart(fig, use_container_width=True)
st.dataframe(summary)
