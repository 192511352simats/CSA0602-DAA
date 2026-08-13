n=int(input())
a=list(map(int,input().split()))
key=int(input())
l,h=0,n-1
c=0
while l<=h:
    c+=1
    m=(l+h)//2
    if a[m]==key:
        print("Element found")
        print("Iterations =",c)
        break
    elif key>a[m]:
        l=m+1
    else:
        h=m-1
else:
    print("Element not found")
    print("Iterations =",c)
