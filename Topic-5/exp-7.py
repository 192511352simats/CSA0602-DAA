def mm(a,l,h):
    if l==h:return a[l],a[l]
    m=(l+h)//2
    x,y=mm(a,l,m)
    p,q=mm(a,m+1,h)
    return min(x,p),max(y,q)
n=int(input())
a=list(map(int,input().split()))
mn,mx=mm(a,0,n-1)
print("Minimum Mark =",mn)
print("Maximum Mark =",mx)
