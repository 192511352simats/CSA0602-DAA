c=0
def merge(a,l,m,h):
    global c
    x=a[l:m+1];y=a[m+1:h+1];i=j=0;r=[]
    while i<len(x) and j<len(y):
        c+=1
        if x[i]<=y[j]:r.append(x[i]);i+=1
        else:r.append(y[j]);j+=1
    r+=x[i:]+y[j:]
    a[l:h+1]=r

def ms(a,l,h):
    if l<h:
        m=(l+h)//2
        ms(a,l,m);ms(a,m+1,h);merge(a,l,m,h)

n=int(input())
a=list(map(int,input().split()))
ms(a,0,n-1)
print(*a,sep=",")
print("Comparisons :",c)
