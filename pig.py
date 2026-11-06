def pig_latin(sentence):
    mySent = sentence.lower().split()

    for word in mySent:
        print(word)

    word_list = []

    for word in mySent:
        new_word = word[1:]+word[0]+'ay'
        #print(new_word)

        word_list.append(new_word)

    return " ".join(word_list)


sentence = input()
print(pig_latin(sentence))
