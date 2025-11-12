# Google Play Store Analytics

This repository contains the complete set of projects completed during my **Data Analytics Internship**, where I analyzed and visualized data from the **Google Play Store dataset** (sourced from Kaggle).  

Across six tasks, I performed data cleaning, transformation, and built multiple interactive dashboards using **Python**, **Pandas**, **Plotly**, and **Streamlit** to derive insights about app performance, growth patterns, and user engagement.

---

## Project Overview

The project is divided into six main tasks, each focusing on a specific analytical objective and visualization technique.

---

### Task 1: Basic Data Exploration  
**Objective:**  
Understand the Google Play Store dataset and prepare it for analysis.

**Key Steps:**  
- Removed duplicates and handled missing values.  
- Performed descriptive statistics on key columns.  
- Identified top-rated apps and popular categories.  
- Explored relationships between reviews, installs, and ratings.  

**Outcome:**  
A clean and structured dataset ready for further visualization.

**Dashboard Preview:**  
![Google Play Store Dashboard](task_1.png)

---

### Task 2: Exploratory Data Analysis (EDA)  
**Objective:**  
Gain deeper insights into app performance and category distribution.

**Key Steps:**  
- Visualized rating distributions and install trends.  
- Compared free vs paid app performance.  
- Identified outliers and correlation between app size, installs, and rating.  

**Outcome:**  
Clear understanding of how different features influence app success.

**Dashboard Preview:**  
![Google Play Store Dashboard](task_play_2.png)

---

### Task 3: Category-Wise Dashboard  
**Objective:**  
Build an interactive Streamlit dashboard for installs per category.

**Key Steps:**  
- Aggregated total installs by category.  
- Highlighted categories with more than 50,000 average installs.  
- Added filters for app type and rating range.  
- Enabled user-driven interaction and insights.  

**Outcome:**  
An interactive category dashboard to explore installs by type and rating range.

**Dashboard Preview:**  
![Google Play Store Dashboard](task_play_3_page-0001.jpg)

---

### Task 4: Installs Over Time Dashboard  
**Objective:**  
Track total installs over time by category and identify significant growth periods.

**Key Steps:**  
- Filtered apps by specific criteria (name patterns, category initials, review count).  
- Calculated month-over-month growth percentage.  
- Highlighted months with over 20% growth.  
- Built an interactive Plotly line chart in Streamlit with time-based visibility.  

**Outcome:**  
Interactive dashboard showing install growth trends with data download options.

**Dashboard Preview:**  
![Google Play Store Dashboard](task_4-1.png)

---

### Task 5: Bubble Chart Analysis  
**Objective:**  
Analyze the relationship between app size, average rating, and total installs.

**Key Steps:**  
- Cleaned and filtered the dataset (rating > 3, reviews > 50, installs > 50K).  
- Converted size and installs into numeric values.  
- Built a Bubble Chart using Plotly Express.  
- Visualized app popularity (bubble size) by category and rating.  
- Added visibility logic between 5 PM and 7 PM IST with a test mode.  

**Outcome:**  
Dynamic bubble chart identifying how app size and ratings influence popularity.

**Dashboard Preview:**  
![Google Play Store Dashboard](task_5-1.png)

---

### Task 6: Cumulative Installs (Stacked Area Chart)  
**Objective:**  
Visualize cumulative installs over time and highlight growth trends.

**Key Steps:**  
- Filtered apps (rating ≥ 4.2, reviews > 1,000, size 20–80 MB, categories starting with T or P).  
- Translated selected categories for localization.  
- Aggregated installs by month and category.  
- Highlighted >25% month-over-month growth with color intensity.  
- Built a stacked area chart using Plotly and Streamlit.  
- Restricted dashboard visibility between 4 PM and 6 PM IST.  

**Outcome:**  
Interactive time-series visualization showing cumulative installs and category performance.

**Dashboard Preview:**  
![Google Play Store Dashboard](task_6-1.png)

---

## Tools and Libraries
- **Python 3**  
- **Pandas**  
- **NumPy**  
- **Plotly / Plotly Express**  
- **Streamlit**  
- **Datetime, Pytz**

---

## Key Learnings and Insights
- Clean data enables more reliable trend analysis and forecasting.  
- Visualization helps identify growth periods and performance gaps quickly.  
- Interactive dashboards enhance user understanding of complex datasets.  
- Multilingual category translation improves accessibility and presentation.  
- Time-based access logic adds practical control for live dashboards.

---

## How to Run

Follow these steps to run the project locally:

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Rakshitha0103/Google_PlayStore_Analytics.git
   ```

2. **Navigate into the project directory**  
   ```bash
   cd Google_PlayStore_Analytics
   ```

3. **Install dependencies**  
   Make sure you have Python 3.10+ installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run any task using Streamlit**  
   Example for Task 1:
   ```bash
   streamlit run google_play_store_task1.py
   ```

5. **Access the dashboard**  
   Once the Streamlit app launches, open the local URL (usually `http://localhost:8501/`) in your browser to explore the dashboard.


## Author
**Rakshitha S**  
*Data Analytics Intern*  

📧 **Email:** srakshitha212@gmail.com  
🔗 **LinkedIn:** [linkedin.com/in/rakshitha-s-a7b694319](https://www.linkedin.com/in/rakshitha-s-a7b694319/)  
🐙 **GitHub:** [Rakshitha0103](https://github.com/Rakshitha0103)

---

*This README summarizes all six tasks completed under the Google Play Store Analytics Internship Project.*
