total_revenue = 0
total_cost = 0
total_profit = 0

best_item = None
highest_profit = 0


with open('data/inventory.csv') as file:

    next(file)

    for line in file:

        column = line.strip().split(',') #DO NOT FORGET THE SPLIT!!


        item = column[0]
        cost = int(column[1])
        selling_price = int(column[2])
        quantity = int(column[3])

        revenue  = selling_price * quantity
        cost_total = cost * quantity
        profit = revenue - cost_total

        # ✅ accumulate totals INSIDE loop
        # ✔️For loops dont have the same 'Reset' characteristic as While loops 
        total_revenue += revenue
        total_cost += cost_total
        total_profit += profit

        # ✔️ find best item since we're Streaming(processing data row-by-row) this is code as per row
        if profit > highest_profit:
            highest_profit = profit
            best_item = item


print('=== BUSINESS SUMMARY ===')
print('Total Revenue: ', total_revenue)
print('Total Cost:', total_cost)
print('Total Profit:', total_profit)
print('Most Profitable Item:', best_item)
print('Profit Generated:', highest_profit)