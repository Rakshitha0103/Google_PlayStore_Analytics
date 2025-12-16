# Google Play Store Analytics – Task 1

This project is part of my Data Analytics Internship, focusing on real-world data cleaning, filtering, and visualization using the Google Play Store dataset from Kaggle. 
Task 1 involves creating a grouped bar chart that compares the average user rating and total review count across the top 10 app categories by total installs.

------------------------------------------------------------

## Objective

To analyze which app categories achieve both high user satisfaction (ratings) and strong user engagement (reviews) among the most-installed apps.

------------------------------------------------------------

## Dashboard Preview

Here is the output dashboard for this task:

![Google Play Store Dashboard](task_1.png)

------------------------------------------------------------

## Data Cleaning and Preparation

- Replaced "Varies with device" in the Size column with NaN.
- Converted size units (k, M) into numeric MB values.
- Removed formatting characters (+, ,) from the Installs column.
- Converted Installs, Reviews, and Rating into numeric data types.
- Parsed Last Updated into proper datetime format.
- Dropped incomplete or invalid rows to ensure accurate analysis.

------------------------------------------------------------

## Methodology

### Filtering Criteria
- Rating ≥ 4.0  
- Size ≥ 10 MB  
- Last Updated in January

### Grouping and Aggregation
- Grouped data by Category.
- Calculated:
  - Average Rating
  - Total Reviews
  - Total Installs
- Selected the top 10 categories based on total installs.

### Visualization
- Built a grouped bar chart using Plotly Express.
- Compared Average Rating and Total Reviews side by side.
- Added interactive hover labels, titles, and legends.
- Included a time-based condition: the chart is visible only between 3 PM and 5 PM IST, simulating a real-time dashboard.

------------------------------------------------------------

## Tools and Libraries Used

- Python 3  
- Pandas  
- NumPy  
- Datetime  
- Pytz  
- Plotly Express

------------------------------------------------------------

## Key Insight

Top-performing app categories show a balance between user satisfaction (high ratings) and engagement (high review counts). 
This highlights how quality and active user feedback contribute to app success in the Play Store ecosystem.

------------------------------------------------------------

## Author

Rakshitha S  
Data Analytics Intern  

Email: srakshitha212@gmail.com  
LinkedIn: https://www.linkedin.com/in/rakshitha-s-a7b694319/  
GitHub: https://github.com/Rakshitha0103

------------------------------------------------------------

This README documents Task 1 of the Google Play Store Analytics Internship Project.
