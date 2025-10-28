# 📊 Google Play Store Analytics – Task 1

This project is part of my **Data Analytics Internship**, focusing on **real-world data cleaning, filtering, and visualization** using the **Google Play Store dataset** from Kaggle.  
**Task 1** involves creating an **interactive grouped bar chart** that compares the **average user rating** and **total review count** across the **Top 10 app categories** by total installs.

---

## 🧩 Objective
To analyze which app categories achieve both **high user satisfaction (ratings)** and **strong user engagement (reviews)** among the most-installed apps.

---

## 🖼️ Dashboard Preview
Here’s the output dashboard for this task 👇  

![Google Play Store Dashboard](task%203-1.png)

> The chart displays two bars per category:  
> - 🟦 **Average Rating**  
> - 🟧 **Total Reviews**

This visualization highlights which app categories balance **popularity** (installs + reviews) and **quality** (ratings).

---

## ⚙️ Data Cleaning & Preparation
- Replaced `"Varies with device"` in the `Size` column with NaN.  
- Converted size units (`k`, `M`) to **numeric MB values**.  
- Removed formatting symbols (`+`, `,`) from `Installs`.  
- Converted `Installs`, `Reviews`, and `Rating` to numeric data types.  
- Parsed `Last Updated` into proper datetime objects.  
- Dropped incomplete or invalid rows.  

---

## 📈 Methodology
### 1️⃣ Filtering Criteria  
- `Rating ≥ 4.0`  
- `Size ≥ 10 MB`  
- `Last Updated` in **January**

### 2️⃣ Grouping & Aggregation  
- Grouped by `Category`.  
- Computed:  
  - **Average Rating**  
  - **Total Reviews**  
  - **Total Installs**  
- Selected **Top 10 Categories** by total installs.  

### 3️⃣ Visualization  
- Created a **Grouped Bar Chart** using **Plotly Express**.  
- Compared **Average Rating (blue)** vs **Total Reviews (orange)**.  
- Added dynamic hover labels, axis titles, and legend.  
- Integrated optional **time-based condition**: chart visible **only between 3 PM – 5 PM IST** for dashboard simulation.

---

## 🛠️ Tools & Libraries
- **Python 3**  
- **Pandas** · **NumPy** · **Datetime** · **Pytz**  
- **Plotly Express** (for advanced interactive visualization)

---

## 💡 Key Insight
Top app categories often maintain both **high engagement** and **high user ratings**, proving that user satisfaction is a key driver of sustained app popularity on the Play Store.

---

## 👩‍💻 Author
**Rakshitha S**  
_Data Analytics Intern_  

📧 **Email:** srakshitha212@gmail.com  
🔗 **LinkedIn:** [linkedin.com/in/rakshitha-s-a7b694319](https://www.linkedin.com/in/rakshitha-s-a7b694319/)  
🐙 **GitHub:** [Rakshitha0103](https://github.com/Rakshitha0103)

---

*This README documents **Task 1** of the **Google Play Store Analytics Internship Project**.*
