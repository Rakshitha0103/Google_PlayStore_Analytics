import pandas as pd
import plotly.express as px
import streamlit as st
from datetime import datetime
import pytz

# 🕒 Set timezone to IST
ist = pytz.timezone("Asia/Kolkata")
current_time = datetime.now(ist).time()

# 🚨 DEMO MODE: force display (pretend it's 6:30 PM)
# comment out this line later if you want real time condition
current_time = datetime.strptime("18:30", "%H:%M").time()

# 📥 Load dataset
df = pd.read_csv(r"C:\Users\rraks\Downloads\archive\googleplaystore.csv")

# 🧹 Clean data
df = df.dropna(subset=['Category', 'Installs'])
df['Installs'] = (
    df['Installs']
    .str.replace('+', '', regex=False)
    .str.replace(',', '', regex=False)
)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')
df = df.dropna(subset=['Installs'])

# ❌ Exclude categories starting with A, C, G, or S
df = df[~df['Category'].str.startswith(('A', 'C', 'G', 'S'))]

# 🔝 Top 5 categories by installs
top_categories = df.groupby('Category')['Installs'].sum().nlargest(5).index
df_top = df[df['Category'].isin(top_categories)]

# 🌍 Map categories to countries for visualization
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

# 🗺️ Aggregate data
agg = df_top.groupby(['Country', 'Category'])['Installs'].sum().reset_index()

# 🖍️ Create colored Choropleth map
fig = px.choropleth(
    agg,
    locations='Country',
    color='Installs',
    hover_name='Category',
    color_continuous_scale='Viridis',
    projection='natural earth',
    title='🌍 Global Installs by App Category'
)

fig.update_layout(
    geo=dict(showframe=False, showcoastlines=True),
    coloraxis_colorbar=dict(title="Total Installs", tickformat=".0f")
)

# 🖥️ Streamlit dashboard
st.title("🌍 Google Play Store Analytics – Task 2")
st.subheader("Interactive Choropleth Map of Global Installs by Category")
st.write(f"🕒 Current IST time: {current_time.strftime('%I:%M %p')}")

# ✅ Always show map (demo mode)
st.plotly_chart(fig, use_container_width=True)
st.success("✅ Demo mode active — map visible (pretending it's 6:30 PM IST).")

# 🕒 To use actual timing, replace above 3 lines with:
# if time(18, 0) <= current_time <= time(20, 0):
#     st.plotly_chart(fig, use_container_width=True)
# else:
#     st.warning("⚠️ The Choropleth map is only visible between 6 PM – 8 PM IST.")
