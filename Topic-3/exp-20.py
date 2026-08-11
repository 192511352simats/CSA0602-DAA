text=input("Enter text: ")
pattern=input("Enter pattern: ")
positions=[]
comparisons=0
for i in range(len(text)-len(pattern)+1):
    print("Shift",i,":",text[i:i+len(pattern)],end=" -> ")
    j=0
    while j<len(pattern):
        comparisons+=1
        if text[i+j]!=pattern[j]:
            break
        j+=1
    if j==len(pattern):
        positions.append(i)
        print("Match")
    else:
        print("Mismatch")
print("Occurrences:",positions)
print("Total comparisons:",comparisons)
print("Best Case: O(n)")
print("Worst Case: O(n*m)")
print("Space Complexity: O(1)")
