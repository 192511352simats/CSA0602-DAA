c=0
def qs(a,l,h):
    global c
    if l<h:
        p=a[h];i=l-1
        for j in range(l,h):
            c+=1
            if a[j]<=p:
                i+=1;a[i],a[j]=a[j],a[i]
        i+=1;a[i],a[h]=a[h],a[i]
        qs(a,l,i-1);qs(a,i+1,h)

n=int(input())
a=list(map(int,input().split()))
qs(a,0,n-1)
print(*a,sep=",")
print("Comparisons :",c)
