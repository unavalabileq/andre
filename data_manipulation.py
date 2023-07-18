import pandas as pd

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('data.csv')

# Print the first 5 rows of the DataFrame
print(df.head())

# Check the shape of the DataFrame
print(df.shape)

# Check the data types of the columns
print(df.dtypes)

# Check the summary statistics of the numeric columns
print(df.describe())

# Drop the rows with missing values
df.dropna(inplace=True)

# Remove duplicates from the DataFrame
df.drop_duplicates(inplace=True)

# Filter the DataFrame by a condition
df_filtered = df[df['column_name'] > 10]

# Sort the DataFrame by a column in ascending order
df_sorted = df.sort_values('column_name')

# Group the DataFrame by a column and calculate the mean of another column
df_grouped = df.groupby('column_name')['other_column'].mean()

# Save the modified DataFrame as a new CSV file
df.to_csv('modified_data.csv', index=False)