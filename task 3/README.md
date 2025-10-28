
# 📈 Google Play Store Analytics – Task 3

This task enhances the Google Play Store Analytics project by building a **real-time Streamlit dashboard** that compares **average installs** and **average revenue** for **Free vs Paid** apps across the **Top 3 categories**.
It demonstrates advanced filtering, time-based visualization control, and live analytical insight generation.

---

## 🧩 Objective

To create a dual-axis chart that visualizes the relationship between **installs and revenue** for free and paid apps, while applying multiple data-driven filters and a real-time display condition.

---

## 🖼️ Dashboard Preview
Here’s the output dashboard for this task 👇  

![Google Play Store Dashboard](task%203-1.png)


## ⚙️ Key Steps

1. **Dataset:** Kaggle – Google Play Store Apps (`googleplaystore.csv`)
2. **Preprocessing:**

   * Parsed and cleaned columns (`Installs`, `Revenue`, `Android Version`, `Size`, `Content Rating`, `App Name`).
   * Standardized formats for installs (`1,000,000+` → `1000000`) and size (`19M` → `19`).
   * Handled missing or non-numeric values gracefully.
3. **Filtering Criteria:**

   * **Installs ≥ 10,000**
   * **Revenue ≥ 10,000**
   * **Android Version > 4.0**
   * **App Size > 15 MB**
   * **Content Rating = ‘Everyone’**
   * **App Name ≤ 30 characters** (including spaces and symbols)
4. **Analysis:**

   * Determined the **Top 3 categories** by total installs after filtering.
   * Computed average installs and average revenue for Free vs Paid apps within those categories.
5. **Visualization:**

   * Used Plotly to build a **dual-axis chart** (Avg Installs = bars, Avg Revenue = line).
   * X-axis → Category and App Type (Free/Paid).
   * Left Y-axis → Average Installs.
   * Right Y-axis → Average Revenue.
6. **Dynamic Condition:**

   * Dashboard displays the chart **only between 1 PM and 2 PM IST**.
   * Outside this time window, a placeholder message appears instead of the chart.
7. **Real-Time Simulation:**

   * Integrated auto-refresh capability to simulate live data updates during the active window.

---

## 🖼️ Output

A Streamlit-based dashboard showing:

* **Dual-axis comparison** of Average Installs vs Average Revenue.
* **Top 3 App Categories** identified automatically.
* **Dynamic chart visibility** restricted to the 1 PM – 2 PM IST window.
* Responsive, interactive Plotly chart with hover details and clear legends.

---

## 🛠️ Tools & Libraries

* Python 3
* Pandas · NumPy · Datetime · Pytz
* Plotly · Plotly Graph Objects
* Streamlit (for dashboard UI)

---

## 📊 Key Insight

Free apps dominate in install volume, whereas paid apps yield significantly higher average revenue.
This contrast illustrates the trade-off between **user reach and monetization efficiency** in mobile app markets.

---


## 👩‍💻 Author

**Rakshitha S**
*Data Analytics Intern*

📧 **Email:** [srakshitha212@gmail.com](mailto:srakshitha212@gmail.com)
🔗 **LinkedIn:** [linkedin.com/in/rakshitha-s-a7b694319](https://www.linkedin.com/in/rakshitha-s-a7b694319/)
🐙 **GitHub:** [Rakshitha0103](https://github.com/Rakshitha0103)

---

*This README documents Task 3 of the Google Play Store Analytics Internship Project.*


