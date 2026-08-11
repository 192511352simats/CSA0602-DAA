from itertools import combinations
def total_value(items,values):
    return sum(values[i] for i in items)
def is_feasible(items,weights,capacity):
    return sum(weights[i] for i in items)<=capacity
weights=eval(input("Enter weights: "))
values=eval(input("Enter values: "))
capacity=int(input("Enter capacity: "))
best=[]
best_value=0
for r in range(len(weights)+1):
    for items in combinations(range(len(weights)),r):
        if is_feasible(items,weights,capacity):
            value=total_value(items,values)
            if value>best_value:
                best_value=value
                best=list(items)
print("Optimal Selection:",best)
print("Total Value:",best_value)
