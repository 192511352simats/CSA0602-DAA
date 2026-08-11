text=input("Enter text: ")
pattern=input("Enter pattern: ")
comparisons=0
for i in range(len(text)-len(pattern)+1):
    for j in range(len(pattern)):
        comparisons+=1
        if text[i+j]!=pattern[j]:
            break
print("Comparisons:",comparisons)
if comparisons==len(pattern):
    print("Best Case")
else:
    print("Average/Worst Case")
