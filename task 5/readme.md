# 📊 Google Play Store Analytics 

This project is part of my **Data Analytics Internship**, focusing on **real-world data cleaning, filtering, and interactive visualization** using the **Google Play Store dataset** from Kaggle.  
**Task 5** involves building a **Bubble Chart** to analyze the relationship between **app size**, **average rating**, and **total installs**.

---

## 🧩 Objective
To explore how **app size** correlates with **average user rating**, while factoring in **popularity (total installs)** and **app category**, helping to identify key patterns among top-performing apps.

---

## 🖼️ Dashboard Preview
Here’s the output dashboard for this task 👇  

![Google Play Store Dashboard](task%205%20-1.png)

---

## 🧮 Data Cleaning & Preparation
- Removed apps containing the letter **“S”** in their name.  
- Filtered categories: **Game**, **Beauty**, **Business**, **Comics**, **Communication**, **Dating**, **Entertainment**, **Social**, **Event**.  
- Converted **Size** to numeric MB values.  
- Cleaned numeric columns (**Rating**, **Reviews**, **Installs**) and converted **Installs** to numeric values.  
- Translated select categories for multilingual representation:  
  - **Beauty → सौंदर्य (Hindi)**  
  - **Business → வியாபாரம் (Tamil)**  
  - **Dating → Dating_DE (German placeholder)**  
- Filtered final dataset to include:  
  - **Rating > 3**  
  - **Reviews > 50**  
  - **Installs > 50 K**

---

## 📈 Methodology

### 1️⃣ Sidebar Filters  
- Users can select specific categories to display.  
- **Test Mode** allows chart visibility at any time for demo or debugging.  

### 2️⃣ Visualization  
- Created a **Bubble Chart** using **Plotly Express**:  
  - **X-axis:** App Size (MB)  
  - **Y-axis:** Average Rating  
  - **Bubble Size:** Number of Installs  
  - **Color:** App Category (Game category highlighted in pink)  
  - Interactive hover displays app name and metrics.  

### 3️⃣ Time-Based Restriction  
- Chart visible **only between 5 PM and 7 PM IST**.  
- Outside that window, a warning message is displayed.  
- **Test Mode** bypasses the time restriction for presentation purposes.  

---

## 🖼️ Output Preview
- Each bubble represents an app.  
- **Bubble size → popularity (installs)**.  
- **Pink bubbles → Game category.**  
- X-axis shows App Size and Y-axis shows Average Rating.  
- Interactive hover and legend make the chart intuitive and dynamic.  

---

## 🛠️ Tools & Libraries
- **Python 3**  
- **Pandas** · **Plotly Express** · **Streamlit**  
- **Datetime** · **Pytz**

---

## 📊 Key Insights
- Larger apps don’t always mean higher ratings — lightweight apps can perform equally well.  
- The **Game category**, highlighted in pink, shows both high installs and ratings.  
- Translating categories adds global context to data storytelling.  
- Time-restricted dashboards enhance real-time simulation scenarios.  

---

## 👩‍💻 Author
**Rakshitha S**  
_Data Analytics Intern_  

📧 **Email:** srakshitha212@gmail.com  
🔗 **LinkedIn:** [linkedin.com/in/rakshitha-s-a7b694319](https://www.linkedin.com/in/rakshitha-s-a7b694319/)  
🐙 **GitHub:** [Rakshitha0103](https://github.com/Rakshitha0103)

---

*This README documents **Task 5** of the **Google Play Store Analytics Internship Project**.*
