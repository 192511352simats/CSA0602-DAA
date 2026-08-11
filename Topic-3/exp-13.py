text=input("Enter text: ")
pattern=input("Enter pattern: ")
for i in range(len(text)-len(pattern)+1):
    comparisons=0
    result="Match"
    for j in range(len(pattern)):
        comparisons+=1
        if text[i+j]!=pattern[j]:
            result="Mismatch"
            break
    print("Shift:",i,"Comparisons:",comparisons,"Result:",result)
