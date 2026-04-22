from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_output_dir():
    os.makedirs("../outputs/plots", exist_ok=True)


def elbow_method(X):
    wcss = []

    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, random_state=42)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    plt.figure(figsize=(8,5))
    plt.plot(range(1,11), wcss, marker='o')
    plt.title("Elbow Method")
    plt.xlabel("Number of Clusters")
    plt.ylabel("WCSS")
    plt.savefig("../outputs/plots/elbow.png")
    plt.close()


def apply_kmeans(df):
    X = df[['Annual_Income', 'Spending_Score']]

    kmeans = KMeans(n_clusters=5, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X)

    return df, kmeans


def plot_clusters(df, kmeans):
    create_output_dir()

    plt.figure(figsize=(10,6))

    sns.scatterplot(
        x='Annual_Income',
        y='Spending_Score',
        hue='Cluster',
        palette='Set1',
        data=df,
        s=100
    )

    # Plot centroids
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:,0], centers[:,1],
                c='black', s=200, marker='X', label='Centroids')

    plt.title("Customer Segmentation (K-Means)")
    plt.legend()
    plt.savefig("../outputs/plots/clusters.png")
    plt.close()