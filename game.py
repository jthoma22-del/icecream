previous = input()
while True:
    word = input()
    if word[0].lower() != previous[-1].lower():
        break
    previous = word
print(f"Stop! You lost with  {word}")


previous_word = input()
word = input()

while word[0] == previous_word[-1]:
    previous_word = word
    word = input()

print(f"Stop! You lost with {word}.")

'''words = input().replace(",", " ").split()
for previous, word in zip(words, words[1:]):
    word = input()
    if word[0].lower() != previous[-1].lower():
        print(f"Stop! You lost with {word}")
        break

# This code wants you to print all the words which is not how the game works
# 

'''
