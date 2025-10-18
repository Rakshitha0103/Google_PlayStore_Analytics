# 📊 Google Play Store Analytics – Task 1

This project is part of my Data Analytics Internship, focusing on real‑world data cleaning, filtering, and visualization using the **Google Play Store dataset** from Kaggle.  
**Task 1** involves building a grouped bar chart that compares the **average user rating** and **total review count** across the **Top 10 app categories** by number of installs.

---

## 🧩 Objective
To identify which app categories maintain strong user satisfaction (high ratings) while generating the highest user engagement (large review counts).

---

## 🧮 Data Cleaning & Preparation
- Replaced `"Varies with device"` entries in the `Size` column with NaN values.  
- Converted size units (`k`, `M`) to numeric values in MB.  
- Removed formatting characters (`+`, `,`) from `Installs`.  
- Converted `Installs`, `Reviews`, and `Rating` columns to numeric data types.  
- Parsed the `Last Updated` column to proper datetime objects.  
- Dropped rows containing critical missing values.  

---

## 📈 Methodology
1. **Filtering Criteria**
   - Rating ≥ 4.0  
   - Size ≥ 10 MB  
   - Last updated in January  

2. **Grouping & Aggregation**
   - Grouped by `Category`  
   - Calculated average `Rating`, total `Reviews`, and total `Installs`.  
   - Selected Top 10 categories (sorted by `Installs`).  

3. **Visualization**
   - Built a **Grouped Bar Chart** using Matplotlib.  
   - Compared **Average Rating** vs **Total Reviews** for the Top 10 Categories.  
   - Added clear labels, color theme, and legend for professional presentation.  

---

## 🖼️ Output Preview
Two bars for each category:
- 💚 Green → Average Rating  
- 🟡 Gold → Total Reviews  

This visualization quickly highlights categories excelling in both popularity and user satisfaction.

---

## 🛠️ Tools & Libraries
- Python 3  
- Pandas  
- NumPy  
- Matplotlib

---

## 📊 Key Insight
App categories with high install counts often maintain strong ratings (> 4 ⭐), indicating that quality and popularity are not mutually exclusive within the Play Store ecosystem.

---

## 👩‍💻 Author
**Rakshitha S**  
Data Analytics Intern  

---

*This README documents Task 1 of the Google Play Store Analytics Internship Project.*