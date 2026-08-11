text=input("Enter text: ").lower()
pattern=input("Enter pattern: ").lower()
position=-1
for i in range(len(text)-len(pattern)+1):
    j=0
    while j<len(pattern) and text[i+j]==pattern[j]:
        j+=1
    if j==len(pattern):
        position=i
        break
print("Pattern found at position:",position)
