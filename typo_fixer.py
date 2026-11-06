'''
Joshua Thomas Section 16
The program takes input from the user and replaces each word with the first 
word in word_list that begins with the same letter. Words without 
a match remain unchanged. It prints the updated sentence and repeats 
until the user enters "done".
'''
sentence = input()
updated_sentence = []
word_list = ["algorithm", "we", "compile", "dog", "ethernet",
             "fetch", "grit", "have", "internet", "kernel", "build"]

while sentence != "done":
    # Split the sentence into a list of words.
    sentence_words = sentence.split()

    # Visit each word's index in the sentence.
    for i in range(len(sentence_words)):
        for word in word_list:   # Check each word in word_list
            # Compare the first letters of the two words.
            if sentence_words[i][0] == word[0]:
                # Replace the sentence word with the matching list word.
                sentence_words[i] = word
                break   # Stop searching
    # add sentence word to list
    updated_sentence.append(" ".join(sentence_words))
    sentence = input()   # Read the next sentence.
for update in updated_sentence:
    print(update)
