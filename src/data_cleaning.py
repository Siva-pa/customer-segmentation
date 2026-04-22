import pandas as pd

def load_data(path):
    """
    Load dataset from given path
    """
    df = pd.read_csv(path)
    return df


def clean_data(df):
    """
    Perform data cleaning:
    - Rename columns
    - Remove duplicates
    - Handle missing values
    - Encode categorical variables
    """
    # Rename columns
    df.columns = ['CustomerID', 'Gender', 'Age', 'Annual_Income', 'Spending_Score']

    # Drop duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    # Encode Gender
    df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

    return df