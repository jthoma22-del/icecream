

'''def favorite(people, name, number):
    if number in people.values():
        print("That number has already been used")
    else:
        people[name] = number
        print(f"{number} is set as {name}'s favorite")


def print_favorite(people, name):
    if name in people:
        print(people[name])
    else:
        print(f"{name} does not have a favorite number")

if __name__ == "__main__":
    people = {}
    command = input("What do you want to do (add favorite number), print favorite numbers for <person>, or quit? ")

    while command != "quit":
        words = command.split()
        number =int(number)
        (name, number)
                

        command = input("What do you want to do (add favorite number), or quit? ")


if __name__ == "__main__":
    pep=name, number=input().split()
    number =int(number)

    while pep!="quit":
        pep=name, number=input().split()
        number =int(number)
        dict(name, number)
 '''       
def add_favorite(people, name, number):
    if number in people.values():
        print("That number has already been used")
    else:
        people[name] = number
        print(f"{number} is set as {name}'s favorite")


def print_favorite(people, name):
    if name in people:
        print(people[name])
    else:
        print(f"{name} does not have a favorite number")


if __name__ == "__main__":
    people = {}
    command = input("What do you want to do (add favorite number), print favorite numbers for <person>, or quit? ")

    while command != "quit":
        words = command.split()

        if len(words) == 2:
            add_favorite(people, words[0], int(words[1]))
        elif len(words) == 5 and words[0] == "print":
            print_favorite(people, words[4])

        command = input("What do you want to do (add favorite number), or quit? ")   



    