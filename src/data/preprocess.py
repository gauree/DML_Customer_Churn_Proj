import os
import pandas as pd
from sklearn.model_selection import train_test_split

def get_root():
    return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

def preprocess():
    root = get_root()
    raw_path = os.path.join(root, "data", "raw", "customer_churn.csv")

    df = pd.read_csv(raw_path)

    if "customerID" in df.columns:
        df = df.drop(columns=["customerID"])

    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    df = df.dropna()
    df = df.drop_duplicates()

    target_col = "Churn"
    if target_col not in df.columns:
        raise ValueError("Churn column 'Churn' not found in dataset")

    train_df, test_df = train_test_split(
        df, test_size=0.2, random_state=42, stratify=df[target_col]
    )

    processed_dir = os.path.join(root, "data", "processed")
    os.makedirs(processed_dir, exist_ok=True)

    train_path = os.path.join(processed_dir, "train.csv")
    test_path = os.path.join(processed_dir, "test.csv")

    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)

print("Preprocessing complete: train.csv and test.csv created")

if __name__ == "__main__":
    preprocess()
