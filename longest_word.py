words=input()
longest_word=""
while words!="done":
    if len(words)>len(longest_word):
            longest_word=words
    words=input()
print(longest_word)
    
