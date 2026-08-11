text=input("Enter text: ")
pattern=input("Enter pattern: ")
positions=[]
for i in range(len(text)-len(pattern)+1):
    j=0
    while j<len(pattern) and text[i+j]==pattern[j]:
        j+=1
    if j==len(pattern):
        positions.append(i)
        result="Match"
    else:
        result="Mismatch"
    print("Alignment:",i+1,"Result:",result)
print("Positions:",positions)
