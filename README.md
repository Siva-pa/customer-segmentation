# 🧠 Customer Segmentation Analysis using K-Means Clustering

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Machine Learning](https://img.shields.io/badge/ML-KMeans-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Project Overview

This project performs **Customer Segmentation Analysis** using **K-Means Clustering** to identify distinct customer groups based on their income and spending behavior.  
The objective is to enable **data-driven marketing strategies**, improve customer targeting, and optimize business decisions.

---

## 🎯 Key Objective

- Segment customers into meaningful groups  
- Understand customer behavior patterns  
- Enable targeted marketing strategies  
- Improve customer engagement and revenue  

---

## 📊 Dataset Information

- **Dataset Name:** Mall Customers Dataset  
- **Total Records:** 200  
- **Features:**
  - CustomerID  
  - Gender  
  - Age  
  - Annual Income (k$)  
  - Spending Score (1–100)  

---

## ⚙️ Tech Stack

- **Programming Language:** Python  
- **Libraries Used:**
  - Pandas  
  - NumPy  
  - Matplotlib  
  - Seaborn  
  - Plotly  
  - Scikit-learn  

---

## 🏗️ Project Structure

```bash
customer-segmentation-analysis/
│── data/
│   └── Mall_Customers.csv
│
│── notebooks/
│   └── customer_segmentation.ipynb
│
│── src/
│   ├── data_cleaning.py
│   ├── eda.py
│   └── clustering.py
│
│── outputs/
│   ├── plots/
│   └── segmented_data.csv
│
│── main.py
│── requirements.txt
│── README.md

```
# 🔍 Workflow
1. Data Cleaning
Removed duplicates and handled missing values
Converted categorical variables (Gender → numerical)
2. Exploratory Data Analysis (EDA)
Age distribution analysis
Income vs Spending behavior
Correlation analysis
3. Clustering
Applied Elbow Method to determine optimal clusters
Implemented K-Means Clustering (k = 5)
4. Visualization
Professional static visualizations (Seaborn, Matplotlib)
Interactive visualization using Plotly
# 📈 Visualizations
📊 Age Distribution

💰 Income vs Spending Score

📉 Elbow Method

🎯 Customer Segments

# 🔍 Key Insights
Identified 5 distinct customer segments based on income and spending behavior
High-income customers are split into high spenders and low spenders
Younger customers tend to have higher spending scores
Gender has minimal impact on purchasing behavior
# 💼 Business Impact
Enables targeted marketing campaigns for different customer groups
Identifies high-value customers for premium services
Helps convert high-income low-spending customers into active buyers
Improves marketing ROI using data-driven strategies
Supports customer retention and engagement strategies
# 🚀 How to Run the Project
1. Clone the Repository
```
git clone https://github.com/your-username/customer-segmentation-analysis.git
cd customer-segmentation-analysis
```
2. Install Dependencies
```
pip install -r requirements.txt
```
3. Run the Project
```
python main.py
```
# 📊 Output
Segmented dataset:
outputs/segmented_data.csv
Generated plots:
outputs/plots/
# 🔮 Future Enhancements
Deploy as Streamlit Web Application
Implement Advanced Clustering (DBSCAN, Hierarchical)
Integrate with Power BI Dashboard
Use larger real-world datasets
# 👨‍💻 Author

Siva Kishore

# 📜 License

This project is licensed under the MIT License.

⭐ Support

If you found this project helpful, please ⭐ the repository!
