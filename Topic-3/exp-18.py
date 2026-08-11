text=input("Enter text: ")
pattern1=input("Enter successful pattern: ")
pattern2=input("Enter unsuccessful pattern: ")
def brute(text,pattern):
    count=0
    for i in range(len(text)-len(pattern)+1):
        j=0
        while j<len(pattern):
            count+=1
            if text[i+j]!=pattern[j]:
                break
            j+=1
        if j==len(pattern):
            return count
    return count
print("Successful search:",brute(text,pattern1))
print("Unsuccessful search:",brute(text,pattern2))
