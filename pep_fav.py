people_dict = {}

def add_person(name, number):
    if number in people_dict.values():
        print("That number has already been used")
    else:
        people_dict[name] = number
        print(f"{number} is set as {name}'s favorite")

if __name__ == "__main__":
    pep = input("What do you want to do (add favorite number), print favorite numbers for <person>, or quit?\n")
    while pep != "quit":
        if pep.startswith("print favorite number for "):
            name = pep.split()[-1]
            if name in people_dict:
                print(people_dict[name])
            else:
                print("That person has not been added")
        else:
            name, number =pep.split()
            number = int(number)
            add_person(name, number)

        pep = input("What do you want to do (add favorite number), or quit? ")

