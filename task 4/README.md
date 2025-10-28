📊 Google Play Store Analytics – Task 4

This project is part of my Data Analytics Internship, focusing on real-world data analysis, interactive visualization, and dashboard creation using the Google Play Store dataset from Kaggle.
Task 4 involves building an interactive Streamlit dashboard to analyze total installs over time by app category, highlight significant growth periods, and provide filters and top app insights.

🧩 Objective

To explore trends in app installs across categories, identify periods of significant growth (>20% month-over-month), and highlight top-performing apps, while enabling users to interact with the dataset through filters and downloads.

🧮 Data Cleaning & Preparation

Filtered app names not starting with x, y, z and not containing "S".

Filtered app categories starting with E, C, or B.

Only included apps with reviews > 500.

Translated categories for better readability:

Beauty → सौंदर्य (Hindi)

Business → வியாபாரம் (Tamil)

Dating → Dating_DE (German placeholder)

Cleaned Installs column by removing + and , and converting to numeric.

Converted Last Updated to datetime objects and dropped invalid rows.

Aggregated total installs by month and category.

Calculated month-over-month percentage change for growth analysis.

📈 Methodology

Filtering & Aggregation

Users can filter apps by category and date range.

Data aggregated by month (YearMonth) and category.

MoM growth percentage calculated for each category.

Interactive Visualization

Built with Plotly and displayed in Streamlit.

Line chart shows total installs over time.

Highlight >20% MoM growth periods with shaded areas (toggle via checkbox).

X-axis: Month | Y-axis: Total installs | Legend: App categories (translated).

Top Apps Table

Displays top 5 apps per selected category by total installs.

Download Option

Filtered data can be downloaded as CSV for further analysis.

Time-Based Restriction

Graph visible only between 6 PM and 9 PM IST, otherwise a warning message is shown.

🖼️ Output Preview

Interactive line chart with different colors for each category.

Shaded areas highlight periods with significant growth (>20% MoM).

Top 5 apps table shows most popular apps in each selected category.

Sidebar filters allow category selection and date range adjustment.

Download button provides filtered dataset for offline use.

🛠️ Tools & Libraries

Python 3

Pandas

Plotly

Streamlit

📊 Key Insights

Categories with high total installs often show significant growth periods, highlighting emerging popular apps.

Interactive filters allow identifying top apps per category in a selected time range.

Translation of categories improves readability and accessibility for multi-lingual users.

The dashboard demonstrates how real-time analytics and interactivity enhance data exploration in app ecosystems.

👩‍💻 Author

Rakshitha S
Data Analytics Intern
Email: srakshitha212@gmail.com