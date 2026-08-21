def merge(a,l,m,h):
    x=a[l:m+1];y=a[m+1:h+1];i=j=0;r=[]
    while i<len(x) and j<len(y):
        if x[i]<=y[j]:r.append(x[i]);i+=1
        else:r.append(y[j]);j+=1
    r+=x[i:]+y[j:];a[l:h+1]=r

def ms(a,l,h):
    if l<h:
        m=(l+h)//2
        ms(a,l,m);ms(a,m+1,h);merge(a,l,m,h)

def qs(a,l,h):
    if l<h:
        p=a[h];i=l-1
        for j in range(l,h):
            if a[j]<=p:i+=1;a[i],a[j]=a[j],a[i]
        i+=1;a[i],a[h]=a[h],a[i]
        qs(a,l,i-1);qs(a,i+1,h)

n=int(input())
a=list(map(int,input().split()))
b=a.copy()
ms(a,0,n-1);qs(b,0,n-1)
print("Sorted :",*a,sep=" ")
print("Merge Space : O(n)")
print("Quick Space : O(log n) average")
