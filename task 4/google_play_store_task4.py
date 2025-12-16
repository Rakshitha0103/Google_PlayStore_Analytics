import pandas as pd
import plotly.express as px
import streamlit as st
from datetime import datetime, timezone, timedelta


file_path = r"C:\Users\rraks\Downloads\archive\googleplaystore.csv"  # Update if needed
df = pd.read_csv(file_path)


df = df[~df['App'].str.startswith(('x','y','z'))]
df = df[~df['App'].str.contains('S', case=False, na=False)]
df = df[df['Category'].str.startswith(('E','C','B'))]

df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')
df = df[df['Reviews'] > 500]


translation_map = {
    'Beauty': 'सौंदर्य',        # Hindi
    'Business': 'வியாபாரம்',   # Tamil
    'Dating': 'Dating_DE'       # German
}
df['Category_Translated'] = df['Category'].replace(translation_map)


df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True).astype(float)
df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')
df = df.dropna(subset=['Last Updated'])


st.set_page_config(page_title="Google Play Store Analytics", layout="wide")
st.sidebar.title("Filters")


categories = df['Category_Translated'].unique()
selected_categories = st.sidebar.multiselect("Select Categories", categories, default=list(categories))


min_date = df['Last Updated'].min()
max_date = df['Last Updated'].max()
start_date, end_date = st.sidebar.date_input("Select Date Range", [min_date, max_date])


filtered_df = df[
    (df['Category_Translated'].isin(selected_categories)) &
    (df['Last Updated'] >= pd.to_datetime(start_date)) &
    (df['Last Updated'] <= pd.to_datetime(end_date))
]


filtered_df['YearMonth'] = filtered_df['Last Updated'].dt.to_period('M')
agg_df = filtered_df.groupby(['YearMonth','Category_Translated'])['Installs'].sum().reset_index()
agg_df['YearMonth'] = agg_df['YearMonth'].dt.to_timestamp()
agg_df['Pct_Change'] = agg_df.groupby('Category_Translated')['Installs'].pct_change()


st.title("Real-time Google Play Store Data Analytics")


now_utc = datetime.now(timezone.utc)
now_ist = now_utc + timedelta(hours=5, minutes=30)
current_hour_ist = now_ist.hour

if 18 <= current_hour_ist <= 21:
    highlight_growth = st.checkbox("Highlight >20% MoM Growth", value=True)
    
    fig = px.line(
        agg_df, 
        x='YearMonth', 
        y='Installs', 
        color='Category_Translated', 
        markers=True,
        title="Total Installs Over Time by App Category",
        labels={'YearMonth':'Month','Installs':'Total Installs'}
    )
    
    
    if highlight_growth:
        for cat in agg_df['Category_Translated'].unique():
            data = agg_df[agg_df['Category_Translated']==cat]
            for i in range(1,len(data)):
                if data['Pct_Change'].iloc[i] > 0.2:
                    fig.add_vrect(
                        x0=data['YearMonth'].iloc[i-1], 
                        x1=data['YearMonth'].iloc[i],
                        fillcolor="LightSalmon", opacity=0.3, layer="below", line_width=0
                    )

    fig.update_traces(
        hovertemplate="<b>%{fullData.name}</b><br>Month: %{x|%Y-%m}<br>Total Installs: %{y:,}<br>MoM Growth: %{customdata:.1%}",
        customdata=agg_df['Pct_Change']
    )
    fig.update_layout(
        xaxis=dict(dtick="M1", tickformat="%Y-%m"),
        hovermode="x unified",
        legend_title="App Category"
    )
    
    st.plotly_chart(fig, use_container_width=True)

    
    st.subheader("Top 5 Apps per Category")
    top_apps = filtered_df.groupby(['Category_Translated','App'])['Installs'].sum().reset_index()
    top_apps = top_apps.sort_values(['Category_Translated','Installs'], ascending=[True,False])
    top5_apps = top_apps.groupby('Category_Translated').head(5)
    st.dataframe(top5_apps)
    
   
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Filtered Data",
        data=csv,
        file_name='filtered_google_playstore.csv',
        mime='text/csv'
    )

else:
    st.warning(f"Graph available only between 6 PM and 9 PM IST. Current IST hour: {current_hour_ist}")
