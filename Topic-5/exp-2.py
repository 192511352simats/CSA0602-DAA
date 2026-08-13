n=int(input())
a=list(map(int,input().split()))
key=int(input())
l,h=0,n-1
ans=-1
while l<=h:
    m=(l+h)//2
    if a[m]==key:
        ans=m
        break
    elif key>a[m]:
        l=m+1
    else:
        h=m-1
print("Index =",ans)
