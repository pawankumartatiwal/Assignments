import pandas as pd

# List of date-strings
date_strings = ['2024-01-01', '2024-02-01', '2024-03-01']

# Convert to datetime
date_series = pd.to_datetime(date_strings)

# Show the timeseries
print("Timeseries:")
print(date_series)
