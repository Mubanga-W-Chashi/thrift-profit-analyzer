import pandas as pd

df = pd.read_csv("data/inventory.csv")

df['revenue'] = df['selling_price'] * df['quantity']
df['cost_total'] = df['cost'] * df['quantity']
df['profit'] = df['revenue'] - df['cost_total']

total_revenue = df['revenue'].sum()
total_cost = df['cost_total'].sum()
total_profit = df['profit'].sum()

# df[total_revenue]
best_row = df.loc[df['profit'].idxmax()]
best_item = best_row['item']
highest_profit = best_row['profit']


print('===  BUSINESS SUMMARY ===')
print('Total Revenue: ', total_revenue)
print('Total Cost: ', total_cost)
print('Total Profit: ', total_profit)
print('Most Profitable Item: ', best_item)
print('Profit Generated : ', highest_profit)

print('\n=== FULL DATASET ===')
print(df)
