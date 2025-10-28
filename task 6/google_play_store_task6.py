import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import pytz

# ------------------------------------------
# 🧠 Title and Setup
# ------------------------------------------
st.set_page_config(page_title="Google Play Store Analytics – Task 6", layout="wide")
st.title("📈 Google Play Store Analytics")
st.subheader("Stacked Area Chart of Cumulative Installs by Category")

# ------------------------------------------
# 🕒 Current IST Time and Test Mode
# ------------------------------------------
ist = pytz.timezone('Asia/Kolkata')
current_time = datetime.now(ist)
st.write(f"🕒 Current IST time: {current_time.strftime('%I:%M %p')}")

# Test Mode switch (for previewing outside 4–6 PM)
test_mode = st.sidebar.checkbox("✅ Enable Test Mode (Bypass Time Restriction)", value=False)

# ------------------------------------------
# 📂 Load Data
# ------------------------------------------
try:
    df = pd.read_csv("googleplaystore.csv")
except FileNotFoundError:
    st.error("❌ File not found! Please make sure 'googleplaystore.csv' is in the same folder.")
    st.stop()

# ------------------------------------------
# 🧹 Data Cleaning & Filters
# ------------------------------------------
# Drop rows with missing critical data
df = df.dropna(subset=["Rating", "Reviews", "Installs", "Category", "Size", "App"])

# Filter 1: Rating >= 4.2
df = df[df["Rating"] >= 4.2]

# Filter 2: App names that do not contain any numbers
df = df[~df["App"].str.contains(r'\d', na=False)]

# Filter 3: App categories that start with “T” or “P”
df = df[df["Category"].str.startswith(('T', 'P'))]

# Filter 4: Reviews > 1000
df["Reviews"] = pd.to_numeric(df["Reviews"], errors='coerce')
df = df[df["Reviews"] > 1000]

# Filter 5: Size between 20 MB and 80 MB
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

# Clean and convert installs
df["Installs"] = df["Installs"].replace('[+,]', '', regex=True).astype(float)

# Convert and clean 'Last Updated'
df["Last Updated"] = pd.to_datetime(df["Last Updated"], errors='coerce')
df = df.dropna(subset=["Last Updated"])

# Create month-year column
df["YearMonth"] = df["Last Updated"].dt.to_period("M").astype(str)

# ------------------------------------------
# 🌐 Translate Category Names in Legend
# ------------------------------------------
translations = {
    "Travel & Local": "Voyage et local (FR)",
    "Productivity": "Productividad (ES)",
    "Photography": "写真 (JP)"
}
df["Category"] = df["Category"].replace(translations)

# ------------------------------------------
# 📊 Aggregate installs per month and category
# ------------------------------------------
grouped = df.groupby(["YearMonth", "Category"])["Installs"].sum().reset_index()

# Calculate cumulative installs over time
grouped = grouped.sort_values(by=["Category", "YearMonth"])
grouped["Cumulative_Installs"] = grouped.groupby("Category")["Installs"].cumsum()

# ------------------------------------------
# 📈 Calculate Month-over-Month Growth (%)
# ------------------------------------------
grouped["MoM_Growth"] = grouped.groupby("Category")["Cumulative_Installs"].pct_change() * 100

# Identify months where total installs increased >25%
grouped["Highlight"] = grouped["MoM_Growth"] > 25

# ------------------------------------------
# 🕒 Time Restriction (4 PM – 6 PM IST)
# ------------------------------------------
if (16 <= current_time.hour < 18) or test_mode:
    st.success("✅ The stacked area chart is visible (within 4 PM – 6 PM IST or Test Mode enabled).")

    # ------------------------------------------
    # 📉 Create Stacked Area Chart
    # ------------------------------------------
    fig = go.Figure()

    categories = grouped["Category"].unique()
    colors = [
        "#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3",
        "#a6d854", "#ffd92f", "#e5c494", "#b3b3b3"
    ]

    for i, category in enumerate(categories):
        cat_data = grouped[grouped["Category"] == category]
        color = colors[i % len(colors)]

        # Increase color intensity if any month has >25% MoM growth
        if cat_data["Highlight"].any():
            color = color.replace("66", "33")  # Darken the color slightly

        fig.add_trace(go.Scatter(
            x=cat_data["YearMonth"],
            y=cat_data["Cumulative_Installs"],
            mode='lines',
            name=category,
            stackgroup='one',
            line=dict(width=0.5),
            fillcolor=color
        ))

    # Layout customization
    fig.update_layout(
        title="📊 Cumulative Installs Over Time (by Category)",
        xaxis_title="Month-Year",
        yaxis_title="Cumulative Installs",
        hovermode="x unified",
        template="plotly",
        legend_title="App Category",
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("⚠️ The stacked area chart is only visible between 4 PM – 6 PM IST.")

