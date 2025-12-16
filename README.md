# 📘 Google Play Store Analytics

This project is based on real-time Google Play Store data analytics.  
It was developed as part of my internship to explore how to perform data cleaning, analysis, and visualization using Python.

The main goal is to analyze app performance on the Google Play Store — including installs, ratings, reviews, and categories — and to visualize patterns using different types of charts.

---

## 📂 Project Structure

Google_PlayStore_Analytics/
│
├── data/
│ └── googleplaystore.csv
│
├── scripts/
│ ├── Task1_Grouped_Bar_Chart.py
│ ├── Task2_Choropleth_Map.py
│ ├── Task3_Dual_Axis_Chart.py
│ ├── Task4_Streamlit_App.py
│ ├── Task5_Bubble_Chart.py
│ └── Task6_Stacked_Area_Chart.py
│
├── images/
│ ├── task1_bar_chart.png
│ ├── task2_choropleth.png
│ ├── task3_dual_axis.png
│ ├── task4_streamlit.png
│ ├── task5_bubble.png
│ └── task6_area_chart.png
│
├── requirements.txt
├── README.md
└── .gitignore


---

## 🧠 Tools and Libraries Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Plotly  
- Streamlit  
- Pytz  

---

## 🧩 Tasks Overview

### Task 1 – Grouped Bar Chart
Compared the **average rating** and **total reviews** for the top 10 app categories by installs.  
Only categories with:
- average rating above 4.0  
- size above 10MB  
- last update in January  
are included.  
This graph is visible only between **3 PM and 5 PM IST**.

---

### Task 2 – Choropleth Map
Created an interactive map using Plotly to visualize global installs by category.  
Only top 5 categories are shown, and categories starting with **A, C, G, or S** are excluded.  
Displayed only between **6 PM and 8 PM IST**.

---

### Task 3 – Dual Axis Chart
Compared **average installs and revenue** for free vs paid apps in the top 3 categories.  
Applied multiple filters (installs > 10,000, revenue > $10,000, Android version > 4.0, etc.).  
Shown only between **1 PM and 2 PM IST**.

---

### Task 4 – Time Series Chart
Plotted total installs over time segmented by app category.  
Highlighted growth >20% month-over-month.  
Also includes translations:
- Beauty → हिंदी (Hindi)  
- Business → தமிழ் (Tamil)  
- Dating → Deutsch (German)  
Visible only between **6 PM and 9 PM IST**.

---

### Task 5 – Bubble Chart
Analyzed relationship between **app size** and **rating** with bubble size as installs.  
Included only selected categories like Game, Beauty, Business, Communication, etc.  
Game category is highlighted in pink.  
Includes same translation logic as Task 4.  
Visible only between **5 PM and 7 PM IST**.

---

### Task 6 – Stacked Area Chart
Shows cumulative installs over time for each category.  
Included only apps with rating ≥ 4.2, reviews > 1000, and size between 20MB–80MB.  
Translated:
- Travel & Local → French  
- Productivity → Spanish  
- Photography → Japanese  
Displayed only between **4 PM and 6 PM IST**.

---

## ⚙️ How to Run

1. Clone the repository  
   ```bash
   git clone https://github.com/yourusername/Google_PlayStore_Analytics.git
   cd Google_PlayStore_Analytics

2. Install dependencies
    ```bash
    pip install -r requirements.txt

3. Run any task file
    ```bash
    streamlit run scripts/Task4_Streamlit_App.py

4. For the Streamlit dashboard
    ```bash
    streamlit run scripts/Task4_Streamlit_App.py

## Output Examples

    All generated charts and screenshots are stored in the images/ folder

##  Notes

- The project follows time-based conditions as mentioned in each task.  
- Each script can be run independently.  
- The dataset is used from Google Play Store data for analysis purposes only.

---

## 👩‍💻 Author

**Rakshitha**  
Data Analytics Intern  

📧 **Email:** [srakshitha212@gmail.com](mailto:srakshitha212@gmail.com)  
🔗 **LinkedIn:** [linkedin.com/in/rakshitha-s-a7b694319](https://linkedin.com/in/rakshitha-s-a7b694319)  
🐙 **GitHub:** [Rakshitha0103](https://github.com/Rakshitha0103)

