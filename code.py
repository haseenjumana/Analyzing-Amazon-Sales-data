import pandas as pd
# Load a CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\juman\Downloads\Amazon Sales data.csv")

# Display the first few rows of the DataFrame
print(df.head())

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Year-Month'] = df['Order Date'].dt.to_period('M')

# Monthly Sales
monthly_sales = df.groupby(['Year', 'Month'])['Total Profit'].sum().reset_index()

# Yearly Sales
yearly_sales = df.groupby('Year')['Total Profit'].sum().reset_index()

# Year-Month Sales
year_month_sales = df.groupby('Year-Month')['Total Profit'].sum().reset_index()

import matplotlib.pyplot as plt
import seaborn as sns

# Monthly Sales Trend
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='Month', y='Total Profit', hue='Year')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.show()

# Yearly Sales Trend
plt.figure(figsize=(12, 6))
sns.barplot(data=yearly_sales, x='Year', y='Total Profit')
plt.title('Yearly Sales Trend')
plt.xlabel('Year')
plt.ylabel('Total Profit')
plt.show()

df['Year-Month'] = df['Year-Month'].astype(str)

import seaborn as sns
import matplotlib.pyplot as plt

# Convert Year-Month to string format
year_month_sales['Year-Month'] = year_month_sales['Year-Month'].astype(str)

# Plot the data
plt.figure(figsize=(14, 7))
sns.lineplot(data=year_month_sales, x='Year-Month', y='Total Profit')
plt.title('Year-Month Sales Trend')
plt.xlabel('Year-Month')
plt.ylabel('Total Profit')
plt.xticks(rotation=90)
plt.show()

