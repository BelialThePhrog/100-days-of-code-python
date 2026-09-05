import numpy as np
import pandas as pd
from numpy.random import randn

# --- 1. Pandas Series ---
labels = ["a", "b", "c"]
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {"a": 10, "b": 20, "c": 30}

print("Series from Dictionary:")
print(pd.Series(d))

ser1 = pd.Series([1, 2, 3, 4], ["USA", "Germany", "USSR", "Japan"])
ser2 = pd.Series([1, 2, 5, 4], ["USA", "Germany", "Italy", "Japan"])
print("\nSeries Addition (Handling NaN):")
print(ser1 + ser2)

# --- 2. Pandas DataFrames & Selection ---
np.random.seed(101)
df = pd.DataFrame(randn(5, 4), ["A", "B", "C", "D", "E"], ["W", "X", "Y", "Z"])

print("\nOriginal DataFrame:")
print(df)

df["Q"] = df["W"] + df["Y"]
print("\nDataFrame after adding column 'Q':")
print(df)

print("\nBoolean Masking (df['W'] > 0 & df['Y'] > 1):")
print(df[(df["W"] > 0) & (df["Y"] > 1)])

# --- 3. Missing Data ---
print("\nDropping rows with NaN (thresh=2):")
print(df.dropna(thresh=2))
print("\nFilling NaN values:")
print(df.fillna(value="LOL"))

# --- 4. Concatenation, Merging, and Joining ---
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3']}, index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'], 'B': ['B4', 'B5', 'B6', 'B7']}, index=[4, 5, 6, 7])

print("\nConcatenated DataFrames:")
print(pd.concat([df1, df2]))

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'], 'A': ['A0', 'A1', 'A2', 'A3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'], 'C': ['C0', 'C1', 'C2', 'C3']})

print("\nMerged DataFrames (Inner Join on 'key'):")
print(pd.merge(left, right, how="inner", on="key"))

# --- 5. Operations & Pivot Tables ---
df_ops = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xyz']})

def square(x):
    return x**2

print("\nApplied Function (Square col1):")
print(df_ops["col1"].apply(square))
print("\nValue Counts for col2:")
print(df_ops['col2'].value_counts())

data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
        'D': [1, 3, 2, 5, 4, 1]}
df_pivot = pd.DataFrame(data)

print("\nPivot Table:")
print(df_pivot.pivot_table(values='D', index=['A', 'B'], columns=['C']))

# --- 6. Data Input and Output ---
# Note: Ensure "example" (CSV) and "Excel_Sample.xlsx" exist in the directory before running.
try:
    df_csv = pd.read_csv("example")
    df_csv.to_csv("My_output.csv", index=False)
    
    df_excel = pd.read_excel("Excel_Sample.xlsx")
    print("\nSuccessfully read Excel file:")
    print(df_excel)
except FileNotFoundError:
    print("\nSample files not found. Skipping File I/O operations.")
