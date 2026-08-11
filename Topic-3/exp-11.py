text=input("Enter text: ")
pattern=input("Enter pattern: ")
positions=[]
comparisons=0
for i in range(len(text)-len(pattern)+1):
    j=0
    while j<len(pattern):
        comparisons+=1
        if text[i+j]!=pattern[j]:
            break
        j+=1
    if j==len(pattern):
        positions.append(i)
print("Positions:",positions)
print("Total comparisons:",comparisons)
