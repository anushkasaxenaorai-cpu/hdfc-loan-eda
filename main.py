import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv(r"Loan payments data.csv")

print(dataset.head(10))
print(dataset.tail(10))

print("\nShape:", dataset.shape)

missing = dataset.isnull().sum()
print("\nMissing values:\n", missing)

print("\nTotal missing values:", missing.sum())

print("\nMissing %:\n", (missing / len(dataset)) * 100)

sns.heatmap(dataset.isnull(), cbar=False)
plt.show()