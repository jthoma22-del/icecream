'''''
Joshua Thomas Section 16
The program takes input from the user to build a sandwich in a given order.
'''

stack = input().lower()

if stack != "bottom slice":
    print("You just made a mess!")
else:
    first = ""
    count = 0
    condiments = []

    ingred = input().lower()

    while ingred != "top slice":
        if first == "":
            first = ingred

        if ingred == first:
            count += 1
        elif ingred not in condiments:
            condiments.append(ingred)

        ingred = input().lower()

    if condiments:
        condiment_text = ", ".join(condiments)
    else:
        condiment_text = "No condiments"

    print(
        f"You have created a {count}-{first} sandwich with the condiments: {condiment_text}")
