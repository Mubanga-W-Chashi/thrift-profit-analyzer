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

# ✅ Ranking products by Profit
top_items = df.sort_values(by='profit', ascending=False)

print("\n=== TOP PERFORMERS ===")
print(top_items[['item', 'profit']])

# ✅ Business flags
def classify_profit(profit):
    if profit > 200:
        return 'HIGH'
    elif profit > 100:
        return 'MEDIUM'
    else:
        return 'LOW'

df['performance'] = df['profit'].apply(classify_profit)

print('\n=== PERFORMANCE CLASSIFICATION ===')
print(df[['item', 'profit', 'performance']])


high_performers = df[df['performance'] == 'HIGH']
medium_performers = df[df['performance'] == 'MEDIUM']

print('\nHigh performing items:')
print(high_performers['item'])

print('\nMedium performing items:')
print(medium_performers['item'])


# ✅ Best items by Margin

df['margin'] = df['selling_price'] - df['cost']

best_margin = df.loc[df['margin'].idxmax()]
best_volume = df.loc[df['quantity'].idxmax()]

print("\nBest margin item:", best_margin["item"])
print("Best volume item:", best_volume["item"])

print('\n=== FULL DATASET ===')
print(df)
