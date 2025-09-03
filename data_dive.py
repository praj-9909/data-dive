import pandas as pd
import matplotlib.pyplot as plt

# Load sample data (replace 'sample.csv' with your file)
df = pd.read_csv('sample.csv')

# Show basic info
print(df.head())
print(df.describe())

# Remove duplicates and missing values
df = df.drop_duplicates()
df = df.dropna()

# Simple visualization
plt.hist(df[df.columns])
plt.xlabel(df.columns)
plt.ylabel('Frequency')
plt.title('Sample Data Histogram')
plt.show()
