
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
    while True:
        sentence = input()
        if sentence == "stop":
            break
        letter_to_remove = input()
        print(remover(sentence, letter_to_remove))
