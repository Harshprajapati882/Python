import pandas as pd
import numpy as np

# 1. Creating Pandas Data Structures
print("1. Creating Pandas Data Structures")

# Creating a Series from a list
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(f"Pandas Series:\n{s}")

# Creating a DataFrame from a dictionary of objects
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'age': [25, 30, 35, 40, 42],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)
print(f"\nPandas DataFrame:\n{df}")


# 2. Viewing Data
print("\n2. Viewing Data")

# Display the top rows
print(f"Top 2 rows (head):\n{df.head(2)}")

# Display the bottom rows
print(f"\nBottom 2 rows (tail):\n{df.tail(2)}")

# Display the index, columns, and underlying NumPy data
print(f"\nDataFrame index: {df.index}")
print(f"DataFrame columns: {df.columns}")
print(f"Underlying NumPy data:\n{df.to_numpy()}")

# Get a quick statistical summary of your data
print(f"\nStatistical summary (describe):\n{df.describe()}")

# Transposing your data
print(f"\nTransposed DataFrame:\n{df.T}")


# 3. Selection
print("\n3. Selection")

# Selecting a single column, which yields a Series
print(f"Selecting the 'name' column:\n{df['name']}")

# Selecting via [], which slices the rows
print(f"\nSlicing rows 0 to 2:\n{df[0:3]}")

# Selection by label (loc)
print(f"\nSelecting row with label 0 (loc):\n{df.loc[0]}")
print(f"\nSelecting rows 0 and 1 (loc):\n{df.loc[0:1]}")

# Selecting on a multi-axis by label
print(f"\nSelecting rows 0-2 and columns 'name' and 'age' (loc):\n{df.loc[0:2, ['name', 'age']]}")

# Selection by position (iloc)
print(f"\nSelecting row at position 3 (iloc):\n{df.iloc[3]}")
print(f"\nSelecting rows 1-2 and columns 0-1 (iloc):\n{df.iloc[1:3, 0:2]}")

# Boolean indexing
print(f"\nSelecting rows where age > 30:\n{df[df['age'] > 30]}")


# 4. Handling Missing Data
print("\n4. Handling Missing Data")
data_with_nan = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [10, 20, 30, 40]
}
df_nan = pd.DataFrame(data_with_nan)
print(f"DataFrame with NaN values:\n{df_nan}")

# Drop rows with any missing data
print(f"\nDropping rows with NaN:\n{df_nan.dropna(how='any')}")

# Fill missing data with a value
print(f"\nFilling NaN with value -99:\n{df_nan.fillna(value=-99)}")

# Check for NaN values
print(f"\nIs NaN? (boolean mask):\n{pd.isna(df_nan)}")


# 5. Operations
print("\n5. Operations")

# Stats
print(f"Mean of all columns:\n{df.mean(numeric_only=True)}")
print(f"\nMean of 'age' column: {df['age'].mean()}")

# Applying functions to the data
# The following will not work because the columns are of different types
# print(df.apply(np.cumsum))
print(f"\nApplying lambda to 'age' column (age + 10):\n{df['age'].apply(lambda x: x + 10)}")

# Grouping
print("\nGrouping by 'city' and getting size:")
# Let's add more data for a better grouping example
df_grouped = pd.concat([df, pd.DataFrame({'name': ['Frank'], 'age': [30], 'city': ['Chicago']})], ignore_index=True)
print(df_grouped.groupby('city').size())


# 6. Merging and Joining
print("\n6. Merging and Joining")

# Concat
df1 = pd.DataFrame({'A': ['A0', 'A1'], 'B': ['B0', 'B1']})
df2 = pd.DataFrame({'A': ['A2', 'A3'], 'B': ['B2', 'B3']})
concatenated = pd.concat([df1, df2])
print(f"Concatenated DataFrame:\n{concatenated}")

# Merge (similar to SQL join)
left = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'A': ['A0', 'A1', 'A2']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K3'], 'B': ['B0', 'B1', 'B3']})
merged = pd.merge(left, right, on='key', how='left')
print(f"\nMerged DataFrame (left join):\n{merged}")


# 7. Reading and Writing Data
print("\n7. Reading and Writing Data")
# Note: These lines are commented out to prevent file system operations during automated runs.
# To test, uncomment them and ensure you have a 'temp_data' directory.

# Create a temporary directory if it doesn't exist
# import os
# if not os.path.exists('temp_data'):
#     os.makedirs('temp_data')

# Writing to a CSV file
# df.to_csv('temp_data/my_data.csv')
print("df.to_csv('my_data.csv')  # Example of writing to CSV")

# Reading from a CSV file
# df_from_csv = pd.read_csv('temp_data/my_data.csv', index_col=0)
# print(f"\nDataFrame read from CSV:\n{df_from_csv}")
print("pd.read_csv('my_data.csv') # Example of reading from CSV")
