def my_dupes(word):
    repeats=[]
    for dupes in word:
        if dupes in repeats:
            return ("dupes")
        repeats.append(dupes)
    else:
        return("no dupes")
  
  

if __name__ == "__main__":
    results = []
    word = input()
    while word != "done":
        results.append(my_dupes(word))   # save the answer, don't print yet
        word = input()

    for result in results:               # print everything after "done"
        print(result)
 

