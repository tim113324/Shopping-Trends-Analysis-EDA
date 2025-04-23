# 🛍️ Shopping Trends Analysis (EDA)

This project analyzes a dataset of shopping trends, exploring various aspects such as customer demographics, purchase behavior, product categories, sales data, and more. The analysis uses Python libraries such as `pandas`, `numpy`, `matplotlib`, and `seaborn` for data manipulation and visualization. The results are presented through various charts and graphs to gain insights into shopping trends.

## 📦 Libraries Used

- `pandas`: Data manipulation and analysis  
- `numpy`: Numerical operations  
- `matplotlib`: Plotting and visualization  
- `seaborn`: Statistical data visualization  

## 📁 Dataset

The dataset used in this analysis is `shopping_trends_updated.csv`. It includes customer information, purchase amounts, product details, and other relevant data.

## 🧭 Steps Involved in the Analysis

### 1. **Data Inspection**
- Checked for nulls, duplicates, and outliers.
- Printed unique values for each column for distribution understanding.

### 2. **Demographic Analysis**
- **Gender Distribution:** Pie chart showing male vs. female customers.
- **Age Distribution by Gender:** Scatter plot across age groups.
- **Top 10 Locations:** Bar chart showing locations with highest purchases.

### 3. **Purchase Behavior Analysis**
- **Purchase Amount by Gender & Age Range**
- **Top 10 Products by Sales vs. Quantity**

### 4. **Product Analysis**
- **Top Categories, Sizes, and Colors:** Pie and bar charts.
- **Sales by Gender across Product Categories:** Stacked bar chart.

### 5. **Geographical Sales Performance**
- **Top 10 Locations by Total Purchase Amount**

### 6. **Shipping & Payment Preferences**
- **Shipping Methods** and **Payment Methods:** Pie charts.

### 7. **Subscription and Purchase Frequency**
- **Impact of Subscription on Purchase Frequency**

### 8. **Seasonal Sales Analysis**
- **Quarterly Trends:** Seasonal bar and line charts.

### 9. **Top 10 Products Performances Analysis**
- **Top 10 Products by Color Preference & Sales**
- **Top 10 Products by Category & Sales**
- **Top 10 Products by Purchase Frequency**
- **Top 10 Products - Seasonal Sales Trends**

### 10. **Product Reviews**
- **Top 10 Reviewed Products vs. Most Purchased**
- **Impact of Age and Gender on Review Scores**

### 11. **Discounts Impact on Purchase**
- **Effect of Discounts by Gender:** Stacked bar chart.

### 12. **Correlation Analysis**
- **Pearson Correlation Heatmap:** For numeric feature relationships.

## 📊 Insights & Conclusion

The analysis provides a **comprehensive overview** of shopping trends across:

- Different demographic groups (gender, age, location)
- Purchase behaviors (e.g., impact of subscription status, seasonal trends)
- Product preferences (e.g., categories, colors, sizes)
- Geographical sales patterns (locations with the highest purchases)
- Discounts' influence on purchase amounts

These insights can guide businesses in identifying customer patterns, improving marketing strategies, and optimizing inventory based on trends.

---

## ✨ Potential Extensions

- **Incorporate machine learning models** to predict future shopping trends, such as predictive modeling for popular products in upcoming seasons.
- **Perform customer segmentation** using clustering algorithms like k-means to better understand distinct consumer groups and their preferences.
- **Extend the dataset with time-series data** for forecasting future sales trends based on past purchase data.
- **Advanced visualizations** with interactive tools such as Plotly or dashboards with Flask/Dash to enhance user experience.

---

## 🛠️ How to Use

1. **Clone this repository:**

```bash
git clone https://github.com/tim113324/Shopping-Trends-Analysis-EDA-.git
```

2. **Install required dependencies:**

```bash
pip install pandas numpy matplotlib seaborn
```

3. **Make sure to download the shopping_trends_updated.csv dataset and place it in the same directory as the Python script (Shopping_trends_analysis.py).**

4. **Run the Python script**
