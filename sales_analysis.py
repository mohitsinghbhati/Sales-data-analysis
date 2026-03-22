import pandas as pd

df = pd.read_csv('sales_data.csv')

total_revenue = df['Revenue'].sum()
print("Total Revenue:", total_revenue)

total_profit = df['Profit'].sum()
print("Total Profit:", total_profit)

top_product = df.groupby('Product_type')['Revenue'].sum().idxmax()
print("Top Product:", top_product)

client_revenue = df.groupby('Client')['Revenue'].sum()
print("\nRevenue by Client:\n", client_revenue)

df['Profit_Margin'] = df['Profit'] / df['Revenue']
avg_margin = df['Profit_Margin'].mean()
print("\nAverage Profit Margin:", avg_margin)

print("\n--- Analysis Completed Successfully ---")