from src.data_cleaning import load_data, clean_data
from src.eda import run_eda
from src.clustering import elbow_method, apply_kmeans, plot_clusters

# Load data
df = load_data("data/Mall_Customers.csv")

# Clean data
df = clean_data(df)

# Run EDA
run_eda(df)

# Clustering
X = df[['Annual_Income', 'Spending_Score']]
elbow_method(X)

df, kmeans = apply_kmeans(df)

plot_clusters(df, kmeans)

# Save output
df.to_csv("outputs/segmented_data.csv", index=False)

print("✅ Project executed successfully!")