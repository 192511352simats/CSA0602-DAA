def first_fit_decreasing(items, capacity):
    # Sort items in decreasing order
    items.sort(reverse=True)

    bins = []

    for item in items:
        placed = False

        for bin in bins:
            if sum(bin) + item <= capacity:
                bin.append(item)
                placed = True
                break

        if not placed:
            bins.append([item])

    return items, bins


# User Input
capacity = int(input("Enter bin capacity: "))

n = int(input("Enter number of items: "))

items = []

print("Enter the items:")
for i in range(n):
    item = int(input(f"Item {i + 1}: "))
    items.append(item)


sorted_items, bins = first_fit_decreasing(items, capacity)

print("\nSorted Items:")
print(sorted_items)

print("\nBins:")

for i in range(len(bins)):
    print(f"Bin {i + 1}:", *bins[i])

print("\nTotal Bins Used =", len(bins))
