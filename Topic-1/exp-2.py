def binary(arr,low,high,key):
    if low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            return binary(arr,low,mid-1,key)
        else:
            return binary(arr,mid+1,high,key)
        return-1
arr=list(map(int,input("Enter the sorted array:").split()))
key=int(input("enter key:"))
result=binary(arr,0,len(arr)-1,key)
if result!=-1:
    print("key found at index",result)
else:
    print("key not found")
