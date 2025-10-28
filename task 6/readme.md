# 📊 Google Play Store Analytics 

This project is part of my **Data Analytics Internship**, focusing on **real-world data cleaning, filtering, and visualization** using the **Google Play Store dataset** from Kaggle.  
**Task 6** involves building a **stacked area chart** to visualize the **cumulative number of installs over time** for each app category, applying multiple data-driven filters and time-based visibility logic.

---

## 🧩 Objective
To explore how installs have accumulated over time across different app categories and highlight months with significant growth (> 25% month-over-month) — while ensuring category translation and dynamic visibility within a time window.

---

## 🖼️ Dashboard Preview
Here’s the output dashboard for this task 👇  
---

## ⚙️ Data Cleaning & Preparation
- Filtered **apps** with:
  - Average Rating ≥ 4.2  
  - **No numbers** in app name  
  - **Reviews > 1,000**  
  - **App Size** between 20 MB and 80 MB  
  - **Category** starting with **T** or **P**
- Cleaned and standardized numeric columns (`Installs`, `Reviews`, `Size`).
- Parsed `Last Updated` into datetime objects.
- Aggregated total installs per **month** and **category**.

---

## 🌐 Category Translation
To enhance localization and readability:
- **Travel & Local** → *Voyage et Localisation* (French)  
- **Productivity** → *Productividad* (Spanish)  
- **Photography** → *写真* (Japanese)

---

## 📈 Methodology
1. **Data Filtering** – Applied conditions for rating, name pattern, category prefix, size, and reviews.  
2. **Aggregation** – Grouped installs by `YearMonth` and `Category`.  
3. **Growth Highlighting** – Increased color intensity for any month showing > 25% MoM growth.  
4. **Visualization** – Created a **Stacked Area Chart** using Plotly Express.  
5. **Dynamic Visibility** – Chart displayed **only between 4 PM and 6 PM IST**, hidden otherwise for dashboard realism.

---

## 🖼️ Output Preview
- Stacked color bands representing each app category’s cumulative installs.  
- Enhanced color intensity during > 25% growth months.  
- Hover tooltips showing exact values and category names.  
- Translated legend for international readability.  
- Responsive and interactive chart layout.

---

## 🛠️ Tools & Libraries
- **Python 3**  
- **Pandas** · **NumPy** · **Datetime** · **Pytz**  
- **Plotly Express** (for interactive visualization)  
- **Streamlit** (for dashboard deployment)

---

## 💡 Key Insights
- Categories starting with *T* or *P* showed consistent install growth.  
- High ratings (> 4.2) correlate with strong long-term install performance.  
- Significant growth periods (> 25%) were captured clearly via color intensity changes.  
- Multilingual legend enhances accessibility for global audiences.

---

## 👩‍💻 Author
**Rakshitha S**  
*Data Analytics Intern*  

📧 **Email:** srakshitha212@gmail.com  
🔗 **LinkedIn:** [linkedin.com/in/rakshitha-s-a7b694319](https://www.linkedin.com/in/rakshitha-s-a7b694319/)  
🐙 **GitHub:** [Rakshitha0103](https://github.com/Rakshitha0103)

---

*This README documents **Task 6** of the Google Play Store Analytics Internship Project.*
