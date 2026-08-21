a=list(map(int,input().split()))
b=list(map(int,input().split()))
i=j=0;r=[]
while i<len(a) and j<len(b):
    if a[i]<=b[j]:r.append(a[i]);i+=1
    else:r.append(b[j]);j+=1
r+=a[i:]+b[j:]
print(*r,sep=",")
