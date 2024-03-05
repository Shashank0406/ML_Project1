import pandas as pd


train_df = pd.read_csv("artifacts/train.csv")
test_df = pd.read_csv("artifacts/test.csv")

print(train_df)
print(test_df.head())