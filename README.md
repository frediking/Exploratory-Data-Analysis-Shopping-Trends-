# Shopping Trends - Exploratory Data Analysis (EDA)

## Overview
This project explores shopping trends using a dataset containing **3,900 customer transactions**. The dataset includes information on **age, gender, purchased items, categories, payment methods, discounts, previous purchases, and more**. The goal is to uncover patterns in shopping behavior through **descriptive statistics and visualizations**.

---

## Table of Contents
- [Dataset Overview](#dataset-overview)
- [Exploratory Data Analysis](#exploratory-data-analysis)
  - [Data Summary](#data-summary)
  - [Missing Values & Duplicates](#missing-values--duplicates)
  - [Univariate Analysis](#univariate-analysis)
  - [Bivariate Analysis](#bivariate-analysis)
  - [Key Insights](#key-insights)
- [Visualizations](#visualizations)
- [Findings & Insights](#findings--insights)
- [Conclusion](#conclusion)
- [Files & Reports](#files--reports)
- [Next Steps](#next-steps)
- [How to Run the Project](#how-to-run-the-project)

---

## Data Source : Kaggle Datasets



## Dataset Overview
- **Total records:** 3,900  
- **Total columns:** 19  
- **Columns Description:**  
  - **Customer ID:** Unique identifier for each customer  
  - **Age, Gender:** Demographics  
  - **Item Purchased, Category:** Type of product bought  
  - **Purchase Amount (USD):** Transaction value  
  - **Location:** U.S. state where the purchase was made  
  - **Size, Color:** Product attributes  
  - **Season:** When the purchase was made  
  - **Review Rating:** Customer rating (1–5 scale)  
  - **Subscription Status:** Indicates if the customer is subscribed  
  - **Payment Method & Preferred Payment Method:** How the customer paid  
  - **Shipping Type:** Standard, Express, etc.  
  - **Discount Applied & Promo Code Used:** Promotions  
  - **Previous Purchases & Frequency of Purchases:** Shopping history  

---

## Exploratory Data Analysis  

### Data Summary  
We started by loading and summarizing the dataset:  
- **Shape of the dataset:** `(3,900, 19)`  
- **Data types:** Integer, float, and categorical  
- **Statistical summary:**  
  - **Average purchase amount:** `$59.76`  
  - **Average review rating:** `3.75`  
  - **Average previous purchases per customer:** `25`  

---

### Missing Values & Duplicates  
- **Missing Values:** **0%** across all columns  
- **Duplicate Records:** **0**  

This confirms the dataset is clean and well-structured.

---

### Univariate Analysis  
We analyzed individual variables to understand their distributions.  

#### Age Distribution  
- Customers are **18 to 70 years old**, with a median age of **44**.  
- Most shoppers are in the **30–57 age range**.  

#### Gender Distribution  
- The dataset contains **both male and female shoppers** (exact proportions visualized in bar charts).  

#### Purchase Amount Distribution  
- Most purchases fall within the `$20-$100` range.  
- The highest purchase amount was **$100**, while the lowest was **$20**.  

#### Subscription Status  
- Majority of customers are **non-subscribers**, shown through a pie chart.  

#### Seasonality  
- **Fall had the highest total sales ($60,018)**, followed by Spring.  
- **Summer had the lowest total sales ($55,777)**.  

---

### Bivariate Analysis  
We explored relationships between different variables.

#### Top-Spending Categories  
- **Footwear and Clothing** had the highest average purchase amount (`~$60`).  

#### Impact of Discounts on Review Ratings  
- Customers who **did not use discounts** gave slightly higher review ratings (`3.75` vs. `3.73`).  

#### Gender-Based Ratings  
- We analyzed whether male and female customers rated products differently using a **boxplot**.  

#### Color Preferences  
- The top 5 most purchased colors were analyzed in a pie chart.  

#### Season & Purchase Behavior  
- Purchases were **evenly distributed across seasons**, with Fall having a slight edge.  

#### Payment Method Trends  
- **PayPal (677 transactions) was the most common**, while **Bank Transfers (612 transactions) were the least used**.  

---

## Visualizations  
We created various plots to analyze shopping trends:  

✅ **Histograms:** Age & Purchase Amount Distribution  
✅ **Bar Charts:** Gender & Season-wise Purchases  
✅ **Pie Charts:** Subscription Status, Color Preferences, Category Distribution  
✅ **Scatter Plots:** Previous Purchases vs. Review Rating  
✅ **Boxplots:** Purchase Amount by Frequency of Purchases  

> All visualizations were styled using the **Seaborn "magma" theme**.

---

## Findings & Insights  

### 🛍️ Key Shopping Trends  
- **Age Group 30-57** dominates shopping.  
- **Footwear & Clothing have the highest spending.**  
- **Fall is the most profitable season.**  
- **Subscribers vs. Non-subscribers show similar purchase amounts.**  
- **PayPal is the most used payment method.**  
- **Colors like Maroon, Gray, and Black are preferred.**  

### 📊 Interesting Insights  
- **Review Ratings** are **similar across all seasons** (`3.72 - 3.79`).  
- **Discounts don't strongly impact review ratings.**  
- **Frequent shoppers (weekly) tend to spend slightly more.**  
- **People from Georgia, Illinois, and Texas spend the most.**  

---

## Conclusion  
This EDA provided **valuable insights into customer shopping behaviors**. The findings can help in:  
✅ **Personalized marketing strategies** based on top-selling items & colors  
✅ **Optimizing seasonal promotions** (Fall had the highest sales)  
✅ **Encouraging PayPal usage** (most preferred payment method)  
✅ **Understanding discount impact on customer satisfaction**  

---

## Files & Reports  
- **shopping_trends.csv** → Raw dataset  
- **shoppingtrendsEDA1.0 (1)** → Python code & analysis  
- **Plots/** → All visualization(png files) in repo  

---

## How to Run the Project  

1. **Clone the Repository **  
   ```bash
   git clone https://github.com/frediking/Exploratory-Data-Analysis-Shopping-Trends-.git
   
   ```

2. **Install Dependencies**  
   Ensure you have Python installed, then install required libraries:  
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```

3. **Run the Python Script**  
   Execute the script to perform EDA and generate visualizations:  
   ```bash
   shoppingtrendsEDA1.0 (1).py
   ```

4. **View Outputs**  
   - The script will generate statistical summaries and visualizations.  
   - Saved plots can be found in the repository.  
   - The processed dataset (if modified) will be saved as `cleaned_shopping_trends.csv`.  

---

## Next Steps  
🔹 **Predictive Modeling** – Can we forecast purchases using ML?  
🔹 **Customer Segmentation** – Clustering customers based on purchase behavior.  
🔹 **A/B Testing Strategies** – Evaluating promotions & discount impact.  

---

## Author  
📌 **Project by Fredinard Ohene-Addo**  
📌 **Email:** fredinardohenea@gmail.com  
📌 **GitHub:** https://github.com/frediking 
