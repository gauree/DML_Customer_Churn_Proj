import pandas as pd
from sklearn.model_selection import train_test_split
import os

def preprocess():
    # Load raw data
    df = pd.read_csv("data/raw/customer_churn.csv")

    # Example cleaning steps - you can modify based on your dataset
    df = df.dropna()        # remove missing rows
    df = df.drop_duplicates()

    # Train-test split
    train, test = train_test_split(df, test_size=0.2, random_state=42)

    # Ensure folder exists
    os.makedirs("data/processed", exist_ok=True)

    # Save outputs
    train.to_csv("data/processed/train.csv", index=False)
    test.to_csv("data/processed/test.csv", index=False)

    print("Preprocessing complete!")

if __name__ == "__main__":
    preprocess()
