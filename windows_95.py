'''
Joshua Thomas
Section 16
This progam takes input from the user to determine if the created  windows key satisfies two conditions:
The length of the key must be a multiple of 3.
Every third digit (the 3rd, 6th, 9th, ...) must be even.
'''

key = input()
valid = len(key) % 3 == 0


for digit in key[2::3]:
    if int(digit) % 2 != 0:
        valid = False
if valid:
    print("Welcome! Booting the system!")

else:
    print("Invalid key! The authorities have been notified.")
vowels = "aeiouyAEIOUY"


def eLatinTrans(sentence):
    mySent = (sentence).split(" ")
    print(mySent)
    eLatin = ""
    for word in mySent:
        n = 1
        up = False
        cap = False

        if word.isupper():
            up = True
        if word.istitle():
            cap = True
        pre = ""
        for char in range(len(word)):
            if word[char].isalpha() or word[char].isdigit():
                break
            pre += word[:char+1]
            word = word[char+1:]

        pos = ""
        for char in range(len(word)-1, 0, -1):
            if word[char].isalpha() or word[char].isdigit():
                break
            pos = word[char:]+pos
            word = word[:char]

        if word[0] in vowels:
            word += "yay"

        if word[0:n].isdigit() == True:
            n += 1
            word = word+" "

        elif word[0] not in vowels and word[1] in vowels:
            word = word[1:]+word[0] + "ay"

        elif word[0:n] not in vowels:
            n += 1
            word = word[n:]+word[0:n]+"ay"

        if up:
            word = word.upper()

        if cap:
            word = word.title()

        eLatin += pre+word+pos+" "
    return eLatin