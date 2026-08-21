T=4
def ins(a):
    for i in range(1,len(a)):
        x=a[i];j=i-1
        while j>=0 and a[j]>x:
            a[j+1]=a[j];j-=1
        a[j+1]=x

def ms(a):
    if len(a)<=T:
        ins(a);return
    m=len(a)//2
    x=a[:m];y=a[m:]
    ms(x);ms(y)
    i=j=k=0
    while i<len(x) and j<len(y):
        if x[i]<=y[j]:a[k]=x[i];i+=1
        else:a[k]=y[j];j+=1
        k+=1
    a[k:]=x[i:]+y[j:]

n=int(input())
a=list(map(int,input().split()))
ms(a)
print(*a,sep=",")
