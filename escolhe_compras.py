prices = input().split(",")
for i in range(len(prices)):
    prices[i] = int(prices[i])
items = input().split(",")
budget_per_item = int(input())

affordable_items = []
cant_afford = 0
total_needed = 0


for ind, price in enumerate(prices):
    if price <= budget_per_item:
        affordable_items.append(items[ind])
        total_needed += price
cant_afford = len(items) - len(affordable_items)




print("Can buy:", affordable_items)
print("Total budget needed:", total_needed)
print("Can't afford:", cant_afford)
