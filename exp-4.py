n=int(input("Enter the number of terms:"))
a,b=0,1
print("Fibonaaci series:")
for i in range(n):
    print(a,end="")
    a,b=b,a+b
