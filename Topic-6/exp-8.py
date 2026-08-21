d=0
def qs(a,l,h,dep):
    global d
    if l<h:
        d=max(d,dep)
        p=a[h];i=l-1
        for j in range(l,h):
            if a[j]<=p:
                i+=1;a[i],a[j]=a[j],a[i]
        i+=1;a[i],a[h]=a[h],a[i]
        qs(a,l,i-1,dep+1);qs(a,i+1,h,dep+1)

n=int(input())
a=list(map(int,input().split()))
qs(a,0,n-1,1)
print(*a,sep=",")
print("Max Depth :",d)
