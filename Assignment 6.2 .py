import pandas as pd 

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

# Create second DataFrame
df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Score': [85, 90, 95]
})

inner_merge = pd.merge(df1, df2, on='ID', how='inner')
print("\nInner Merge:")
print(inner_merge)

left_join = pd.merge(df1, df2, on='ID', how='left')
print("\nLeft Join:")
print(left_join)

right_join = pd.merge(df1, df2, on='ID', how='right')
print("\nRight Join:")
print(right_join)

df1_index = df1.set_index('ID')
df2_index = df2.set_index('ID')

index_join = df1_index.join(df2_index, how='right')
print("\nIndex-Based Right Join using join():")
print(index_join)
