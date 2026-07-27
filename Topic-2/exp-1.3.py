def reorder_shelf(books):
    arr = books.copy()
    n = len(arr)
    moves = 0
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            moves += 1

    return arr, moves

n = int(input("Enter the number of books: "))

books = []
print("Enter the Book IDs:")
for i in range(n):
    book_id = int(input(f"Book ID {i + 1}: "))
    books.append(book_id)


ordered_books, moves = reorder_shelf(books)

print("\nBooks after Reordering:")
print(ordered_books)
print("Number of Physical Moves:", moves)
