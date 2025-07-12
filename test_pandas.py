import pandas as pd

# Sample data
data = {
    'Name': ['Shannu', 'Arjun', 'Diya'],
    'Marks': [88, 76, 93]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("✅ Pandas is working fine! Here's your table:\n")
print(df)
