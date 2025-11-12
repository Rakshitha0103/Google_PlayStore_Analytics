# Google Play Store Analytics – Task 3

This task is a part of the Google Play Store Analytics project.  
The goal was to build a real-time Streamlit dashboard that compares the average installs and average revenue of Free and Paid apps within the Top 3 categories.

The dashboard includes advanced filters, a time-based condition, and a dual-axis chart that gives a clear comparison between installs and revenue.

------------------------------------------------------------

## What I Built

I created a dual-axis chart that shows how Free and Paid apps perform in terms of installs and revenue.  
The dashboard automatically identifies the Top 3 app categories and displays both metrics side by side.  
It is visible only between 1 PM and 2 PM IST. Outside this time window, a message appears instead of the chart.

### Dashboard Preview

Here’s the dashboard output for this task:

![Google Play Store Dashboard](task%20play%203_page-0001.jpg)

------------------------------------------------------------

## Steps I Followed

1. Dataset: Google Play Store Apps dataset (googleplaystore.csv) from Kaggle.

2. Data Preprocessing:
   - Cleaned and formatted columns like Installs, Revenue, Android Version, Size, Content Rating, and App Name.
   - Converted text formats like "1,000,000+" to 1000000 and "19M" to 19.
   - Removed rows with missing or non-numeric values.

3. Applied Filters:
   - Installs greater than or equal to 10,000
   - Revenue greater than or equal to 10,000
   - Android version greater than 4.0
   - App size greater than 15 MB
   - Content rating equal to "Everyone"
   - App name not longer than 30 characters (including spaces and symbols)

4. Analysis:
   - Found the Top 3 categories based on total installs after filtering.
   - Calculated the average installs and average revenue for both Free and Paid apps within those categories.

5. Visualization:
   - Created a dual-axis chart using Plotly.
     - Bars show Average Installs.
     - Line shows Average Revenue.
   - X-axis represents Category and App Type (Free or Paid).
   - Left Y-axis shows Average Installs, and the Right Y-axis shows Average Revenue.

6. Time Restriction:
   - The dashboard displays the chart only between 1 PM and 2 PM IST.
   - At other times, it shows the message "Dashboard available only between 1 PM and 2 PM IST."

7. Real-Time Effect:
   - Added an auto-refresh feature to simulate live updates during the active time period.

------------------------------------------------------------

## Key Insights

Free apps have a much higher number of installs, while Paid apps generate higher average revenue.  
This shows the trade-off between reaching more users and earning more revenue per user.

------------------------------------------------------------

## Tools and Libraries Used

- Python 3  
- Pandas  
- NumPy  
- Datetime and Pytz  
- Plotly and Plotly Graph Objects  
- Streamlit for the dashboard interface

------------------------------------------------------------

## Author

Rakshitha S  
Data Analytics Intern  

Email: srakshitha212@gmail.com  
LinkedIn: https://www.linkedin.com/in/rakshitha-s-a7b694319/  
GitHub: https://github.com/Rakshitha0103

------------------------------------------------------------

This README describes Task 3 of the Google Play Store Analytics project – Real-Time Dashboard Implementation.
