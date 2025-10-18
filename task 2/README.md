# 🌍 Google Play Store Analytics – Task 2

This task extends the Google Play Store Analytics project by creating an **interactive choropleth map** using Python and Plotly to visualize global installs by app category.  
It demonstrates advanced data filtering, conditional logic, and geographic storytelling through data.

---

## 🧩 Objective
To analyze global installs of the most popular app categories and highlight categories with exceptionally high user engagement.

---

## ⚙️ Key Steps
1. **Dataset:** Kaggle – Google Play Store Apps  
2. **Preprocessing:**
   - Cleaned and standardized critical columns (`Size`, `Installs`, `Reviews`, `Last Updated`).
   - Removed non‑numeric characters (`+`, `,`) and converted sizes into MB.  
   - Ensured consistent numeric data types across variables.
3. **Filtering:**
   - Excluded categories whose names start with **A**, **C**, **G**, or **S**.  
   - Selected only the **Top 5 categories** by total installs.  
   - Marked categories where installs exceed **1 million (1 M)**.  
4. **Mapping:**
   - Used Plotly Express `choropleth` to build an interactive world map.  
   - Assigned each top category a representative country for visual demonstration.  
   - Color intensity represents total installs; hover labels show category names.  
5. **Dynamic Visibility:**  
   - Included a time‑based condition (6 PM – 8 PM IST) to display the map only during a specific window for dashboard simulation.

---

## 🖼️ Output
A Plotly‑based interactive world map highlighting:
- **Top 5 app categories** after filtering.  
- **Countries** corresponding to those categories.  
- **Highlight** for categories with installs > 1 M.  
- Smooth hover effects and legend explaining intensity = install volume.

---

## 🛠️ Tools & Libraries
- Python 3  
- Pandas · NumPy · Datetime · Pytz  
- Plotly Express (for interactive visualization)  

---

## 📊 Key Insight
High‑install categories consistently dominate multiple regions and demonstrate wide global appeal, highlighting the scalability potential of entertainment and communication apps across markets.

---

## 👩‍💻 Author
**Rakshitha S**  
*Data Analytics Intern*

📧 **Email:** srakshitha212@gmail.com  
🔗 **LinkedIn:** [linkedin.com/in/rakshitha‑s‑a7b694319](https://www.linkedin.com/in/rakshitha-s-a7b694319/)  
🐙 **GitHub:** [Rakshitha0103](https://github.com/Rakshitha0103)

---

*This README documents Task 2 of the Google Play Store Analytics Internship Project.*