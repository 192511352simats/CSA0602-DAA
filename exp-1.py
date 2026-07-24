n=int(input("enter the element:"))
arr=[]
count=0
print("Enter the array element:")
for i in range(n):
    arr.append(int(input()))
key=int(input("Enter the key serach:"))
found=False
for i in range(len(arr)):
    if arr[i]==key:
        print("Key found at index.")
        count=i+1
        print(count)
        found=True
        break
if not found:
    print("key not found")
