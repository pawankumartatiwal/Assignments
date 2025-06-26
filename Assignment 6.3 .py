import pandas as pd

dfA = pd.DataFrame({'ID': [1, 2], 'Math': [70, 80]})
dfB = pd.DataFrame({'ID': [3, 4], 'Math': [60, 75]})
dfC = pd.DataFrame({'ID': [1, 2, 3, 4], 'English': [88, 76, 90, 85]})


concat_df = pd.concat([dfA, dfB])
print("\nConcatenated DataFrame (dfA + dfB):")
print(concat_df)


final_merge = pd.merge(concat_df, dfC, on='ID')
print("\nFinal Merged DataFrame with dfC:")
print(final_merge)




# Difference between df.join() and pd.merge() :
print("""
Main Differences:

1. df.join():
   - Used to join on index by default.
   - Simpler syntax for index-based joins.
   - Can also join on columns if specified.

2. pd.merge():
   - More flexible.
   - Allows joins on any column(s).
   - Supports inner, left, right, outer joins.

Use merge() when you need full control over join conditions. Use join() when working with indexes.
""")
