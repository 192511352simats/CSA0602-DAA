def search(names, key):
    for i in range(len(names)):
        if names[i].lower() == key.lower():
            print("Name found at position", i + 1)
            return
    print("Name not found")

n = int(input("Enter number of names: "))
names = []

for i in range(n):
    names.append(input("Enter name: "))

key = input("Enter name to search: ")

search(names, key)
