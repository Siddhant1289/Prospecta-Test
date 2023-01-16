import csv
import pandas as pd

# Read input CSV file
with open('input.csv', 'r') as f:
    reader = csv.reader(f)
    input_data = [row for row in reader]

# Convert input data to a pandas DataFrame
df = pd.DataFrame(input_data)

# Perform calculations on the DataFrame
df = df.applymap(lambda x: eval(x) if x.startswith('=') else x)

# Write output CSV file
df.to_csv('output.csv', index=False)
