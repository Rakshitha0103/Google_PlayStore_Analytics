import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import pytz


st.set_page_config(page_title="Google Play Store Analytics – Task 6", layout="wide")
st.title(" Google Play Store Analytics")
st.subheader("Stacked Area Chart of Cumulative Installs by Category")


ist = pytz.timezone('Asia/Kolkata')
current_time = datetime.now(ist)
st.write(f" Current IST time: {current_time.strftime('%I:%M %p')}")


test_mode = st.sidebar.checkbox(" Enable Test Mode (Bypass Time Restriction)", value=False)



try:
    df = pd.read_csv("googleplaystore.csv")
except FileNotFoundError:
    st.error(" File not found! Please make sure 'googleplaystore.csv' is in the same folder.")
    st.stop()


df = df.dropna(subset=["Rating", "Reviews", "Installs", "Category", "Size", "App"])


df = df[df["Rating"] >= 4.2]


df = df[~df["App"].str.contains(r'\d', na=False)]


df = df[df["Category"].str.startswith(('T', 'P'))]


df["Reviews"] = pd.to_numeric(df["Reviews"], errors='coerce')
df = df[df["Reviews"] > 1000]


def convert_size(size_str):
    try:
        if 'M' in size_str:
            return float(size_str.replace('M', '').strip())
        elif 'k' in size_str:
            return float(size_str.replace('k', '').strip()) / 1024
        else:
            return None
    except:
        return None

df["Size_MB"] = df["Size"].apply(convert_size)
df = df.dropna(subset=["Size_MB"])
df = df[(df["Size_MB"] >= 20) & (df["Size_MB"] <= 80)]


df["Installs"] = df["Installs"].replace('[+,]', '', regex=True).astype(float)


df["Last Updated"] = pd.to_datetime(df["Last Updated"], errors='coerce')
df = df.dropna(subset=["Last Updated"])


df["YearMonth"] = df["Last Updated"].dt.to_period("M").astype(str)


translations = {
    "Travel & Local": "Voyage et local (FR)",
    "Productivity": "Productividad (ES)",
    "Photography": "写真 (JP)"
}
df["Category"] = df["Category"].replace(translations)


grouped = df.groupby(["YearMonth", "Category"])["Installs"].sum().reset_index()


grouped = grouped.sort_values(by=["Category", "YearMonth"])
grouped["Cumulative_Installs"] = grouped.groupby("Category")["Installs"].cumsum()


grouped["MoM_Growth"] = grouped.groupby("Category")["Cumulative_Installs"].pct_change() * 100


grouped["Highlight"] = grouped["MoM_Growth"] > 25


if (16 <= current_time.hour < 18) or test_mode:
    st.success("The stacked area chart is visible (within 4 PM – 6 PM IST or Test Mode enabled).")

   
    fig = go.Figure()

    categories = grouped["Category"].unique()
    colors = [
        "#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3",
        "#a6d854", "#ffd92f", "#e5c494", "#b3b3b3"
    ]

    for i, category in enumerate(categories):
        cat_data = grouped[grouped["Category"] == category]
        color = colors[i % len(colors)]

        
        if cat_data["Highlight"].any():
            color = color.replace("66", "33")  

        fig.add_trace(go.Scatter(
            x=cat_data["YearMonth"],
            y=cat_data["Cumulative_Installs"],
            mode='lines',
            name=category,
            stackgroup='one',
            line=dict(width=0.5),
            fillcolor=color
        ))

    
    fig.update_layout(
        title="Cumulative Installs Over Time (by Category)",
        xaxis_title="Month-Year",
        yaxis_title="Cumulative Installs",
        hovermode="x unified",
        template="plotly",
        legend_title="App Category",
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning(" The stacked area chart is only visible between 4 PM – 6 PM IST.")

