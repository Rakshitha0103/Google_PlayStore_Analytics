📊 Google Play Store Bubble Chart – Task 5

This project is part of my Data Analytics Internship, focusing on real-world data cleaning, filtering, and interactive visualization using the Google Play Store dataset from Kaggle.
Task 5 involves building a bubble chart to analyze the relationship between app size, average rating, and total installs.

🧩 Objective

To visually explore how app size correlates with average user rating, while factoring in popularity (installs) and app category, helping to identify patterns among top-performing apps.

🧮 Data Cleaning & Preparation

Removed apps containing the letter “S” in their name.

Filtered categories: Game, Beauty, Business, Comics, Communication, Dating, Entertainment, Social, Event.

Converted size to numeric MB values.

Cleaned numeric columns (Rating, Reviews, Installs) and converted Installs to numbers.

Applied translations for certain categories:

Beauty → सौंदर्य (Hindi)

Business → வியாபாரம் (Tamil)

Dating → Dating_DE (German placeholder)

Filtered apps for meaningful analysis: Rating > 3, Reviews > 50, Installs > 50k.

📈 Methodology

Sidebar Filters

Users can select categories to display.

Test mode enables chart visibility at any time.

Visualization

Bubble Chart using Plotly:

X-axis: App Size (MB)

Y-axis: Average Rating

Bubble size: Number of installs

Color: App category (Game category highlighted in pink)

Interactive hover shows app names.

Time Restriction

Chart is available only between 5 PM and 7 PM IST for real-time constraints.

Test mode bypasses this restriction for development/demo purposes.

🖼️ Output Preview

Each bubble represents an app.

Size of the bubble indicates popularity (installs).

Pink bubbles highlight the Game category.

X-axis shows app size; Y-axis shows average rating.

🛠️ Tools & Libraries

Python 3

Pandas

Plotly

Streamlit

👩‍💻 Author

Rakshitha S
Email: srakshitha212@gmail.com

Data Analytics Intern