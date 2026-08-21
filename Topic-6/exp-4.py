import time
def ms(a):
    if len(a)>1:
        m=len(a)//2
        x=a[:m];y=a[m:]
        ms(x);ms(y)
        i=j=k=0
        while i<len(x) and j<len(y):
            if x[i]<=y[j]:a[k]=x[i];i+=1
            else:a[k]=y[j];j+=1
            k+=1
        while i<len(x):a[k]=x[i];i+=1;k+=1
        while j<len(y):a[k]=y[j];j+=1;k+=1
n=int(input())
a=list(map(int,input().split()))
s=time.perf_counter()
ms(a)
e=time.perf_counter()
print(*a,sep=",")
print("Time Taken :",e-s,"sec")
