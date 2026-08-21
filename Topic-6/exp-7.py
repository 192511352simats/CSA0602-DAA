def ms(a):
    if len(a)<=1:return a,0
    m=len(a)//2
    x,c1=ms(a[:m]);y,c2=ms(a[m:]);i=j=c=0;r=[]
    while i<len(x) and j<len(y):
        if x[i]<=y[j]:r.append(x[i]);i+=1
        else:r.append(y[j]);j+=1;c+=len(x)-i
    return r+x[i:]+y[j:],c+c1+c2

n=int(input())
a=list(map(int,input().split()))
a,c=ms(a)
print("Sorted :",*a,sep=" ")
print("Inversions :",c)
