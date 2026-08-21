def qs(a,l,h,k):
    p=a[h];i=l
    for j in range(l,h):
        if a[j]<=p:
            a[i],a[j]=a[j],a[i];i+=1
    a[i],a[h]=a[h],a[i]
    if i==k:return a[i]
    if k<i:return qs(a,l,i-1,k)
    return qs(a,i+1,h,k)

n=int(input())
a=list(map(int,input().split()))
k=int(input())
print(qs(a,0,n-1,k-1))
