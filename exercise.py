import pandas as pd

file_path = 'superstore.csv'
df = pd.read_csv(file_path, encoding='ISO-8859-1')

df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')


df['Sales'] = df['Sales'].fillna(0)

region_category_sales = df.groupby(['Region', 'Category'])['Sales'].sum().reset_index()

print("\nSales by Region and Category:\n", region_category_sales)

df['Month'] = df['Order Date'].dt.to_period('M')

pivot_monthly_sales = df.pivot_table(values='Sales', index='Month', aggfunc='sum')

print("\nMonthly Sales Trends:\n", pivot_monthly_sales)


pivot_monthly_sales = pivot_monthly_sales.fillna(0)

print("\nUpdated Monthly Sales Trends (missing data filled):\n", pivot_monthly_sales)
