n=int(input("enter the number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print("iterative factorial:",fact)
def factorial(num):
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)
print("Recursive factorial:",factorial(n))
