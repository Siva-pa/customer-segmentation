import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid", palette="muted")

def create_output_dir():
    os.makedirs("../outputs/plots", exist_ok=True)


def plot_age_distribution(df):
    plt.figure(figsize=(8,5))
    sns.histplot(df['Age'], kde=True)
    plt.title("Age Distribution")
    plt.savefig("../outputs/plots/age_distribution.png")
    plt.close()


def plot_income_vs_spending(df):
    plt.figure(figsize=(8,5))
    sns.scatterplot(
        x='Annual_Income',
        y='Spending_Score',
        hue='Gender',
        palette='coolwarm',
        data=df
    )
    plt.title("Income vs Spending Score")
    plt.savefig("../outputs/plots/income_spending.png")
    plt.close()


def plot_correlation(df):
    plt.figure(figsize=(6,4))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title("Feature Correlation")
    plt.savefig("../outputs/plots/correlation.png")
    plt.close()


def run_eda(df):
    create_output_dir()
    plot_age_distribution(df)
    plot_income_vs_spending(df)
    plot_correlation(df)