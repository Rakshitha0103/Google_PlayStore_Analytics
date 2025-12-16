#  Google Play Store Analytics

This project contains a complete set of analytics tasks developed during my **Data Analytics Internship**, based on the **Google Play Store dataset**.  
The project focuses on **data cleaning, analysis, and interactive visualization** using Python and Streamlit.

The main objective is to analyze app performance — including installs, ratings, reviews, revenue, and categories — and present insights through multiple dashboards with **time-based visibility controls**.

---

##  Project Structure

Google_PlayStore_Analytics/  
│  
├── data/  
│   └── googleplaystore.csv  
│  
├── scripts/  
│   ├── Task1_Grouped_Bar_Chart.py  
│   ├── Task2_Choropleth_Map.py  
│   ├── Task3_Dual_Axis_Chart.py  
│   ├── Task4_TimeSeries_Trend.py  
│   ├── Task5_Bubble_Chart.py  
│   └── Task6_Stacked_Area_Chart.py  
│  
├── images/  
│   ├── task_1.png  
│   ├── task_play_2.png  
│   ├── task_3.png  
│   ├── task_4-1.png  
│   ├── task_5-1.png  
│   └── task_6-1.png  
│  
├── requirements.txt  
├── README.md  
└── .gitignore  

---

##  Tools and Libraries Used

- Python  
- Pandas  
- NumPy  
- Plotly  
- Matplotlib  
- Seaborn  

- Streamlit  
- Pytz  
- Datetime  

---

##  Tasks Overview

### Task 1 – Grouped Bar Chart
- Compared **average rating** and **total reviews** for the top app categories by installs.  
- Filters applied:
  - Average rating > 4.0  
  - App size > 10 MB  
  - Last update in January  
- Displayed only between **3 PM and 5 PM IST**.

---

### Task 2 – Choropleth Map
- Created an interactive **Plotly Choropleth map** to visualize global installs by category.  
- Conditions applied:
  - Top 5 categories only  
  - Categories starting with **A, C, G, or S** excluded  
  - Highlighted installs > 1 million  
- Displayed only between **6 PM and 8 PM IST**.

---

### Task 3 – Dual Axis Chart
- Compared **average installs** and **average revenue** for **Free vs Paid apps**.  
- Filters applied:
  - Installs ≥ 10,000  
  - Revenue ≥ $10,000  
  - Android version > 4.0  
  - App size > 15 MB  
  - Content rating: Everyone  
  - App name length ≤ 30 characters  
- Displayed only between **1 PM and 2 PM IST**.

---

### Task 4 – Time Series Chart
- Visualized **total installs over time** segmented by category.  
- Highlighted **month-over-month growth > 20%**.  
- Category translations:
  - Beauty → Hindi  
  - Business → Tamil  
  - Dating → German  
- Displayed only between **6 PM and 9 PM IST**.

---

### Task 5 – Bubble Chart
- Analyzed the relationship between:
  - App size  
  - Average rating  
  - Total installs (bubble size)  
- Selected categories such as Game, Beauty, Business, Communication.  
- Game category highlighted distinctly.  
- Same translation logic as Task 4 applied.  
- Displayed only between **5 PM and 7 PM IST**.

---

### Task 6 – Stacked Area Chart
- Visualized **cumulative installs over time** by category.  
- Filters applied:
  - Rating ≥ 4.2  
  - Reviews > 1,000  
  - App size between 20 MB and 80 MB  
- Category translations:
  - Travel & Local → French  
  - Productivity → Spanish  
  - Photography → Japanese  
- Displayed only between **4 PM and 6 PM IST**.

---

##  How to Run the Project

1. Clone the repository  
2. Install dependencies from `requirements.txt`  
3. Run any task file using Streamlit  
4. Access the dashboard through the local Streamlit URL  

All generated charts and screenshots are stored in the `images/` folder.

---

## Notes

- Each task follows **strict time-based visibility rules**.  
- All scripts can be run independently.  
- The dataset is used strictly for learning and analysis purposes.

---

## Author

**Rakshitha S**  
Data Analytics Intern  

Email: srakshitha212@gmail.com  
LinkedIn: https://www.linkedin.com/in/rakshitha-s-a7b694319/  
GitHub: https://github.com/Rakshitha0103  

---

This README summarizes all six tasks completed under the **Google Play Store Analytics Internship Project**.
