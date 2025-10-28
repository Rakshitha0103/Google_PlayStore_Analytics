import pandas as pd
import plotly.graph_objects as go
import datetime as dt
import pytz

# === Load Dataset ===
df = pd.read_csv(r"C:\Users\rraks\Downloads\archive\googleplaystore.csv")

# === Data Cleaning ===
df['Size'] = df['Size'].replace('Varies with device', None)
df = df.dropna(subset=['Size'])

# Convert Size to MB
def size_to_mb(size):
    try:
        size = str(size).strip()
        if 'M' in size:
            return float(size.replace('M', ''))
        elif 'k' in size or 'K' in size:
            return float(size.replace('k', '').replace('K', '')) / 1024
        else:
            return None
    except:
        return None

df['Size'] = df['Size'].apply(size_to_mb)
df = df.dropna(subset=['Size'])

# Clean Installs column
df['Installs'] = df['Installs'].str.replace('+', '', regex=False).str.replace(',', '', regex=False)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')
df = df.dropna(subset=['Installs'])

# Clean Reviews
df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')
df = df.dropna(subset=['Reviews'])

# Convert Last Updated
df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')
df = df.dropna(subset=['Last Updated'])

# === Apply Filters ===
df_filtered = df[
    (df['Rating'] >= 4.0) &
    (df['Size'] >= 10) &
    (df['Last Updated'].dt.month == 1)
]

# === Aggregate Data ===
category_stats = df_filtered.groupby('Category').agg({
    'Rating': 'mean',
    'Reviews': 'sum',
    'Installs': 'sum'
}).reset_index()

# === Top 10 Categories by Installs ===
top10 = category_stats.sort_values(by='Installs', ascending=False).head(10)

# === Time Restriction Setup ===
ist = pytz.timezone('Asia/Kolkata')
now_ist = dt.datetime.now(ist)

# Force show for testing (remove time restriction)
if True:
    # Create grouped bar chart
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=top10['Category'],
        y=top10['Rating'],
        name='Average Rating',
        marker_color='royalblue',
        text=top10['Rating'].round(2),
        textposition='auto'
    ))

    fig.add_trace(go.Bar(
        x=top10['Category'],
        y=top10['Reviews'],
        name='Total Reviews',
        marker_color='orange',
        text=top10['Reviews'].apply(lambda x: f"{x/1e6:.2f}M"),
        textposition='auto'
    ))

    # Chart Layout
    fig.update_layout(
        title='📊 Top 10 App Categories by Installs (Filtered by Rating ≥ 4, Size ≥ 10MB, January Updates)',
        xaxis_title='App Category',
        yaxis_title='Value',
        barmode='group',
        template='plotly_dark',
        title_x=0.5
    )

    # Show Chart in Browser
    fig.show()

    print(f"✅ Chart displayed (current IST time: {now_ist.strftime('%H:%M:%S')})")
else:
    print("⏰ This dashboard is available only between 3:00 PM and 5:00 PM IST.")
