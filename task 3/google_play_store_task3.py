import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
import re

st.set_page_config(page_title=" Google Play Store Analytics", layout="wide")

# ---------- Helper parsing ----------
def parse_number(x):
    if pd.isna(x): return np.nan
    x = str(x).replace('+','').replace(',','').replace('$','').strip().lower()
    try:
        if x.endswith('k'): return float(x[:-1]) * 1_000
        if x.endswith('m'): return float(x[:-1]) * 1_000_000
        return float(x)
    except:
        return np.nan

def parse_android_ver(s):
    if pd.isna(s): return np.nan
    m = re.search(r"(\d+(?:\.\d+)?)", str(s))
    return float(m.group(1)) if m else np.nan

def parse_size(s):
    if pd.isna(s): return np.nan
    s = str(s).lower().strip()
    if s in ("varies with device", ""): return np.nan
    try:
        if s.endswith('m'): return float(s[:-1])
        if s.endswith('k'): return float(s[:-1]) / 1000
        return float(s)
    except:
        return np.nan

# ---------- Load Data ----------
def load_data(path):
    if not os.path.exists(path):
        st.error("❌ CSV file not found. Please check the file path.")
        return pd.DataFrame()

    df = pd.read_csv(path)
    df.columns = [c.strip() for c in df.columns]

    # Parse columns if present
    if 'Installs' in df.columns:
        df['Installs_parsed'] = df['Installs'].apply(parse_number)
    else:
        df['Installs_parsed'] = np.nan

    if 'Android_Ver' in df.columns:
        df['Android_ver_parsed'] = df['Android_Ver'].apply(parse_android_ver)
    else:
        df['Android_ver_parsed'] = np.nan

    if 'Size' in df.columns:
        df['Size_M'] = df['Size'].apply(parse_size)
    else:
        df['Size_M'] = np.nan

    # Revenue logic — if no column, create one
    if 'Revenue' in df.columns:
        df['Revenue_parsed'] = df['Revenue'].apply(parse_number)
    elif 'Price' in df.columns:
        df['Price_parsed'] = df['Price'].apply(parse_number)
        df['Revenue_parsed'] = df['Installs_parsed'] * df['Price_parsed']
    else:
        df['Revenue_parsed'] = np.nan

    # App name length
    df['App_name_len'] = df['App'].astype(str).apply(len)

    # Clean type column
    if 'Type' in df.columns:
        df['Type'] = df['Type'].fillna('Free')
    else:
        df['Type'] = 'Free'

    return df

# ---------- Filter & Chart ----------
def apply_filters(df):
    if df.empty: 
        return df

    df = df.copy()

    # Fill missing numeric values
    for col in ['Installs_parsed', 'Revenue_parsed', 'Android_ver_parsed', 'Size_M']:
        if col not in df.columns:
            df[col] = np.nan
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # Adaptive thresholds to prevent zero data
    min_installs = df['Installs_parsed'].quantile(0.25)
    min_revenue = df['Revenue_parsed'].quantile(0.25)
    min_size = df['Size_M'].quantile(0.25)

    df_filtered = df[
        (df['Installs_parsed'] >= min_installs) &
        (df['Revenue_parsed'] >= min_revenue) &
        (df['Android_ver_parsed'] > 4.0) &
        (df['Size_M'] >= min_size) &
        (df['App_name_len'] <= 30)
    ]

    return df_filtered

def build_chart(summary_df):
    cats = summary_df['Category'].unique().tolist()
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    x, installs, revenue = [], [], []

    for cat in cats:
        for typ in ['Free', 'Paid']:
            row = summary_df[(summary_df['Category']==cat) & (summary_df['Type']==typ)]
            x.append(f"{cat} - {typ}")
            installs.append(row['Avg_Installs'].iloc[0] if not row.empty else 0)
            revenue.append(row['Avg_Revenue'].iloc[0] if not row.empty else 0)

    fig.add_trace(go.Bar(x=x, y=installs, name='Avg Installs'), secondary_y=False)
    fig.add_trace(go.Scatter(x=x, y=revenue, mode='lines+markers', name='Avg Revenue'), secondary_y=True)
    fig.update_layout(title='Average Installs vs Average Revenue (Free vs Paid Apps)', 
                      xaxis_title='Category - Type', barmode='group', template='plotly_white')
    fig.update_yaxes(title_text="Average Installs", secondary_y=False)
    fig.update_yaxes(title_text="Average Revenue", secondary_y=True)
    return fig

# ---------- Main ----------
def main():
    st.title(" Google Play Store Data Analytics")

    path = r"C:\Users\rraks\OneDrive\Desktop\Google_PlayStore_Analytics\task 3\googleplaystore.csv"
    df = load_data(path)

    if df.empty:
        st.stop()

    st.success(f" Loaded {len(df)} rows")

    filtered = apply_filters(df)
    st.info(f"Rows after filtering: {len(filtered)}")

    if filtered.empty:
        st.warning(" No data left after filtering — showing partial dataset instead.")
        filtered = df.copy()

    # Determine top 3 categories by installs
    if 'Category' not in filtered.columns:
        st.error(" No 'Category' column found in dataset.")
        st.stop()

    top3 = filtered.groupby('Category')['Installs_parsed'].sum().nlargest(3).index.tolist()
    st.write("Top 3 Categories:", ', '.join(top3))

    df_top3 = filtered[filtered['Category'].isin(top3)]

    summary = (
        df_top3.groupby(['Category','Type'])
        .agg(Avg_Installs=('Installs_parsed','mean'),
             Avg_Revenue=('Revenue_parsed','mean'))
        .reset_index()
    )

    fig = build_chart(summary)
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(summary)

if __name__ == "__main__":
    main()
