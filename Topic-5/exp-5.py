n=int(input())
a=list(map(int,input().split()))
key=int(input())
l,h=0,n-1
ans=-1
while l<=h:
    m=(l+h)//2
    if a[m]==key:
        ans=m
        l=m+1
    elif key>a[m]:
        l=m+1
    else:
        h=m-1
if ans!=-1:
    print("Last occurrence at index",ans)
else:
    print("Element not found")
