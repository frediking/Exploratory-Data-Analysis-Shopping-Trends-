#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Load all packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set a global seaborn theme with magma palette
sns.set_theme(style="darkgrid", palette="magma")


# In[5]:


# Load the dataset and display the first few rows
shopdata = pd.read_csv(r"C:\Users\ADMIN\Desktop\shopping_trends.csv")
shopdata.head()


# In[6]:


# Check number of rows and columns in dataset
shopdata.shape


# In[7]:


# Summary statistics of the dataset
shopdata.describe()


# In[8]:


# Get a concise summary of the DataFrame including data types and non-null count
shopdata.info()


# In[9]:


# Checking for missing values in each column
shopdata.isna().sum()


# In[10]:


# Checking for duplicate rows in the dataset
shopdata.duplicated().sum()


# In[11]:


# VISUALIZATION
# Histogram showing the frequency distribution of the Age
age_color = sns.color_palette("magma", 1)[0]
shopdata["Age"].plot(kind="hist", edgecolor="black", color=age_color)
plt.title("Histogram of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# In[12]:


# List all columns present in the dataset
shopdata.columns


# In[18]:


# Barplot of Gender Distribution
gender_counts = shopdata["Gender"].value_counts()
gender_colors = sns.color_palette("magma", len(gender_counts))
gender_counts.plot(kind="bar", color=gender_colors, edgecolor="black")
plt.title("Barplot of Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()


# In[21]:


# Calculate and display the top 2 categories with the highest average purchase amount
shopdata.groupby("Category")["Purchase Amount (USD)"].mean().sort_values(ascending= False).head(2)


# In[24]:


# Sorting dataset based on Review Rating in descending order 
shopdata.sort_values("Review Rating", ascending = False, inplace = True)
shopdata.head()


# In[26]:


# Pie chart to display the proportion of each subscription status.
subs_counts = shopdata["Subscription Status"].value_counts()
subs_colors = sns.color_palette("magma", len(subs_counts))
subs_counts.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=subs_colors)
plt.title("Pie Chart of Subscription Status")
plt.ylabel("")  # Hide default y-label
plt.savefig("Pie_Chart_of_Subscription_Status", dpi=300, bbox_inches ="tight")
plt.show()


# In[30]:


# Pie chart for top 5 colors by frequency (head of value counts)

top5_colors = shopdata["Color"].value_counts().head()
colors_palette = sns.color_palette("magma", len(top5_colors))
top5_colors.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=colors_palette)
plt.title("Top 5 Colors Distribution (Pie Chart)")
plt.ylabel("")
plt.savefig("Top 5 Colors Distribution (Pie Chart)", dpi=300, bbox_inches ="tight")
plt.show()


# In[34]:


# Scatter plot showing the relationship between Previous Purchases and Review Rating

scatter_color = sns.color_palette("magma", 1)[0]
shopdata.plot(x="Previous Purchases", y="Review Rating", kind="scatter", color=scatter_color)
plt.title("Scatter Plot: Previous Purchases vs. Review Rating")
plt.xlabel("Previous Purchases")
plt.ylabel("Review Rating")
plt.savefig("ScatterPlot_PreviousPurchases_vs_Review_Rating", dpi=300, bbox_inches ="tight")
plt.show()


# In[62]:


# Sum of Purchase Amounts grouped by Season
shopdata.groupby("Season")["Purchase Amount (USD)"].sum()


# In[36]:


# Boxplot of Purchase Amount by Frequency of Purchases
# Helps identify the distribution and outliers in purchase amounts across different purchase frequencies.

shopdata.boxplot(column="Purchase Amount (USD)", by="Frequency of Purchases", patch_artist=True,
                 boxprops=dict(facecolor=sns.color_palette("magma", 1)[0]))
plt.title("Boxplot of Purchase Amount by Frequency of Purchases")
plt.suptitle("")  # Remove automatic subtitle
plt.xlabel("Frequency of Purchases")
plt.ylabel("Purchase Amount (USD)")
plt.xticks(rotation=45, fontsize=8)
plt.savefig("Boxplot_of_Purchase_Amount_by_Frequency_of_Purchases", dpi=300, bbox_inches ="tight")
plt.show()


# In[28]:


# Compare Preferred Payment Method frequency (lowest vs. highest)
low = shopdata["Preferred Payment Method"].value_counts().sort_values(ascending= False).tail(1)
high = shopdata["Preferred Payment Method"].value_counts().sort_values(ascending= False).head(1)
print("Least frequent Preferred Payment Method:", low)
print("Most frequent Preferred Payment Method:", high)


# In[82]:


# Pivot Table: Average Purchase Amount by Location and Item Purchased
pd.pivot_table(shopdata, values = "Purchase Amount (USD)", index = "Location", columns = "Item Purchased", aggfunc= "mean")


# In[84]:


# Mean Purchase Amount by Size
shopdata.groupby("Size")["Purchase Amount (USD)"].mean()


# In[30]:


# Sum of Purchase Amount by Payment Method
shopdata.groupby("Payment Method")["Purchase Amount (USD)"].sum()


# In[90]:


# Mean Review Rating by Discount Applied
shopdata.groupby("Discount Applied")["Review Rating"].mean()


# In[92]:


# Count of Categories per Color 
shopdata.groupby("Color")["Category"].value_counts()


# In[94]:


# Median of Previous Purchases grouped by Frequency of Purchases
shopdata.groupby("Frequency of Purchases")["Previous Purchases"].median()


# In[96]:


# Mean Review Rating by Season
shopdata.groupby("Season")["Review Rating"].mean()


# In[38]:


# Bar plot counting the number of purchases per Season

season_counts = shopdata["Season"].value_counts()
season_colors = sns.color_palette("magma", len(season_counts))
season_counts.plot(kind="bar", color=season_colors, edgecolor="black")
plt.xlabel("Season")
plt.ylabel("Count")
plt.title("Count of Purchases in Each Season")
plt.savefig("Count_of_Purchases_in_Each_Season", dpi=300, bbox_inches ="tight")
plt.show()


# In[40]:


# Pie chart for distribution of Purchases by Category

cat_counts = shopdata["Category"].value_counts()
cat_colors = sns.color_palette("magma", len(cat_counts))
cat_counts.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=cat_colors)
plt.title("Distribution of Purchases by Category")
plt.ylabel("")
plt.savefig("Distribution_of_Purchases_by_Category(Pie_Chart)", dpi=300, bbox_inches ="tight")
plt.show()


# In[42]:


# Visualization: Boxplot of Review Rating Distribution by gender to show the spread and potential differences in review ratings between genders.
# -----------------------------------------------------------------------------
shopdata.boxplot(column="Review Rating", by="Gender", patch_artist=True,
                 boxprops=dict(facecolor=sns.color_palette("magma", 1)[0]))
plt.xlabel("Gender")
plt.ylabel("Review Rating")
plt.title("Review Rating Distribution by Gender")
plt.suptitle("")
plt.savefig("Review Rating Distribution by Gender", dpi=300, bbox_inches ="tight")
plt.show()


# In[44]:


# Histogram for Purchase Amount Distribution

hist_color = sns.color_palette("magma", 1)[0]
shopdata["Purchase Amount (USD)"].plot(kind="hist", bins=10, edgecolor="black", color=hist_color)
plt.xlabel("USD")
plt.ylabel("Frequency")
plt.title("Histogram of Purchase Amount Distribution")
plt.savefig("Histogram of Purchase Amount Distribution", dpi=300, bbox_inches ="tight")
plt.show()


# In[46]:


# Bar plot of Mean Review Rating for each Color

mean_reviewrating = shopdata.groupby("Color")["Review Rating"].mean()
color_bar = sns.color_palette("magma", len(mean_reviewrating))
mean_reviewrating.plot(kind="bar", color=color_bar, edgecolor="black")
plt.xlabel("Color")
plt.ylabel("Mean Review Rating")
plt.title("Mean Review Rating for Each Color")
plt.savefig("Mean Review Rating for Each Color", dpi=300, bbox_inches ="tight")
plt.show()


# In[48]:


# Visualization: Pie chart for Sum of Purchase Amount by Payment Method

pay_sum = shopdata.groupby("Payment Method")["Purchase Amount (USD)"].sum()
pay_colors = sns.color_palette("magma", len(pay_sum))
pay_sum.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=pay_colors)
plt.title("Sum of Purchase Amount by Payment Method")
plt.ylabel("")  
plt.savefig("Sum of Purchase Amount by Payment Method", dpi=300, bbox_inches ="tight")
plt.show()


# In[50]:


# Boxplot of Purchase Amount Distribution by Frequency of Purchases

shopdata.boxplot(column="Purchase Amount (USD)", by="Frequency of Purchases", patch_artist=True,
                 boxprops=dict(facecolor=sns.color_palette("magma", 1)[0]))
plt.xlabel("Frequency of Purchases")
plt.ylabel("Purchase Amount (USD)")
plt.title("Purchase Amount Distribution by Frequency of Purchases")
plt.xticks(rotation=45, fontsize=8)
plt.suptitle("")
plt.savefig("Purchase Amount Distribution by Frequency of Purchases", dpi=300, bbox_inches ="tight")
plt.show()


# In[54]:


# Pie chart for Sum(percentages) of Purchase Amount by Season

season_sum = shopdata.groupby("Season")["Purchase Amount (USD)"].sum()
season_sum_colors = sns.color_palette("magma", len(season_sum))
season_sum.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=season_sum_colors)
plt.xlabel("Season")
plt.ylabel(" ")
plt.title("Sum of Purchase Amount by Season")
plt.savefig("Sum of Purchase Amount by Season", dpi=300, bbox_inches ="tight")
plt.show()


# In[ ]:




