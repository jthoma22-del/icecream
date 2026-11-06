def add_person(people_dict, name, number):
    if number in people_dict.values():
        print("That number has already been used")
    else:
        people_dict[name] = number
        print(f"{number} is set as {name}'s favorite")


if __name__ == "__main__":
    people_dict = {}

    pep = input("Enter name and number, print favorite number for <person>, or quit:\n")

    while pep != "quit":
        if pep.startswith("print favorite number for "):
            name = pep.split()[-1]

            if name in people_dict:
                print(people_dict[name])
            else:
                print("That person has not been added")
        else:
            parts = pep.split()
        
            if len(parts) == 2:
                name, number = parts
                number = int(number)
                add_person(name, number)
             
            '''name, number = pep.split()
            number = int(number)
            add_person(people_dict, name, number)
            '''

        pep = input("Enter name and number, print favorite number for <person>, or quit: ")