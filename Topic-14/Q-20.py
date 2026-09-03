def best_fit(items, capacity):

    bins = []
    remaining_space = []

    for item in items:

        best_bin = -1
        minimum_space = float("inf")

        # Find the best bin
        for i in range(len(bins)):

            if remaining_space[i] >= item:

                space_after = remaining_space[i] - item

                if space_after < minimum_space:
                    minimum_space = space_after
                    best_bin = i

        # If no suitable bin exists
        if best_bin == -1:

            bins.append([item])
            remaining_space.append(capacity - item)

        else:

            bins[best_bin].append(item)
            remaining_space[best_bin] -= item

    return bins


# User Input
capacity = int(input("Enter bin capacity: "))

n = int(input("Enter number of items: "))

items = []

print("Enter the items:")

for i in range(n):
    item = int(input(f"Item {i + 1}: "))
    items.append(item)


bins = best_fit(items, capacity)

print("\nBins:")

for i in range(len(bins)):
    print(f"Bin {i + 1}:", *bins[i])

print("\nTotal Bins Used =", len(bins))
