import pandas as pd
import plotly.express as px
import streamlit as st
from datetime import datetime, timezone, timedelta
import os

# --- Helper function to convert Size to MB ---
def size_to_mb(x):
    try:
        if pd.isna(x) or x.lower() == 'varies with device':
            return None
        x = str(x).lower().strip()
        if x.endswith('m'):
            return float(x[:-1])
        if x.endswith('k'):
            return float(x[:-1]) / 1024
        return float(x)
    except:
        return None

# --- Streamlit page config ---
st.set_page_config(page_title="Google Play Store Bubble Chart", layout="wide")
st.sidebar.title("Filters")
test_mode = st.sidebar.checkbox("Test Mode (show chart anytime)", value=True)

# --- CSV file path ---
data_file = os.path.join("data", "googleplaystore.csv")

# --- Check if file exists ---
if not os.path.exists(data_file):
    st.error("CSV file not found. Make sure 'googleplaystore.csv' is inside the 'data' folder.")
    st.stop()

# --- Load CSV ---
df = pd.read_csv(data_file)

if df.empty:
    st.error("CSV file is empty. Check the file content.")
    st.stop()

# --- Clean and preprocess data ---
df = df.dropna(subset=['App','Category','Rating','Installs','Size'])

# Remove apps starting with 'S' (optional filter)
df = df[~df['App'].str.contains('S', case=False, na=False)]

# Translate some categories
translation_map = {
    'Beauty': 'सौंदर्य', 
    'Business': 'வியாபாரம்', 
    'Dating': 'Dating_DE'
}
df['Category_Translated'] = df['Category'].replace(translation_map)

# Convert numeric columns
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')

# Clean Installs column
df['Installs'] = df['Installs'].astype(str).str.replace('[+,]', '', regex=True)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

# Convert Size to MB
df['Size_MB'] = df['Size'].apply(size_to_mb)

# Drop rows with missing numeric values
df = df.dropna(subset=['Rating','Reviews','Installs','Size_MB'])

# --- Sidebar filters ---
all_categories = df['Category_Translated'].unique()
selected_categories = st.sidebar.multiselect("Select Categories", all_categories, default=list(all_categories))

df_filtered = df[df['Category_Translated'].isin(selected_categories)]

# Optional numeric filters
df_filtered = df_filtered[
    (df_filtered['Rating'] > 3.0) & 
    (df_filtered['Reviews'] > 50) & 
    (df_filtered['Installs'] > 5000)  # Reduced to avoid blank chart
]

# --- Page Title ---
st.title("Google Play Store Bubble Chart")

# --- IST time calculation ---
now_utc = datetime.now(timezone.utc)
now_ist = now_utc + timedelta(hours=5, minutes=30)
current_hour_ist = now_ist.hour
st.write(f"Current IST time: {now_ist.strftime('%I:%M %p')}")

# --- Show chart only between 5 PM – 7 PM IST or test_mode ---
if test_mode or (17 <= current_hour_ist <= 19):
    if df_filtered.empty:
        st.warning("No apps match the selected filters. Adjust sidebar options.")
        st.dataframe(df.head(20))  # Show some data for reference
    else:
        fig = px.scatter(
            df_filtered,
            x='Size_MB',
            y='Rating',
            size='Installs',
            color='Category_Translated',
            hover_name='App',
            size_max=60,
            title="App Size vs Rating (Bubble size = Installs)"
        )

        fig.update_layout(
            xaxis_title="App Size (MB)",
            yaxis_title="Average Rating",
            legend_title="Category",
            hovermode="closest"
        )

        st.plotly_chart(fig, use_container_width=True)

        # Optional: show top apps in table
        top_apps = df_filtered.sort_values('Installs', ascending=False).head(10)
        st.subheader("Top 10 Apps by Installs")
        st.dataframe(top_apps[['App','Category_Translated','Rating','Reviews','Installs','Size_MB']])
else:
    st.warning(f"Graph available only between 5 PM and 7 PM IST. Current IST hour: {current_hour_ist}")
