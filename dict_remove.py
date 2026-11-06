

'''
Joshua Thomas
Section 16
The program takes a sentence and a letter from the user and removes all instances
of that letter from the sentence and prints the new sentence.

 '''
def remover(line, to_remove):
    new_list = []
    for letter in line:
        if letter not in to_remove:
            new_list.append(letter)
    return "".join(new_list)


if __name__ == "__main__":
    # finish this code: put your while loop to read user input here
    while True:
        sentence = input()
        if sentence == "stop":
            break
        letter_to_remove = input().lower()
        print(remover(sentence, letter_to_remove))


'''
def remover(line, to_remove):
    return "".join(letter for letter in line if letter not in to_remove)


if __name__ == "__main__":
    while True:
        sentence = input("Enter a sentence (or stop): ").lower()
        if sentence == "stop":
            break

        letters_to_remove = input("Enter letter(s) to remove: ").lower()
        print(remover(sentence, letters_to_remove))
'''
