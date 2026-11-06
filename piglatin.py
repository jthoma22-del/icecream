

def pig_latin(sentence):
    mysent = sentence.lower().split()

    for word in mysent:
        print(word)

    word_list = []
    for word in mysent:
        update = word[1:]
        new_word = update+word[0]+'ay'
        word_list.append(new_word)

    return " ".join(word_list)


sentence = input()


print(pig_latin(sentence))
