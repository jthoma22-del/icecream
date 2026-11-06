"""
Joshua Thomas
Section 16
The program takes a list of integers from the user and returns a new list
that contains a string of symbols used to generate a visual representation.
Each symbol has a numeric value associated with it. 
"""


def art_generator(values):
    dictionary = {"smallest": ".", 1: ".", 2: ",", 3: ":", 4: ";",
                  5: "=", 6: "*", 7: "#", 8: "%", 9: "@", 10: "$", "largest": "$"}
    # smallest = min(values)
    # largest = max(values)

    smallest = values[0]
    largest = values[0]

    for value in values:
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value

    # Create a new list to hold the generated art
    art = []

    for value in values:
        if smallest == largest:
            # If all values are the same, use the middle symbol
            art_line = dictionary.get(6, "*")
        elif value == smallest:
            art_line = dictionary.get("smallest", ".")
        elif value == largest:
            art_line = dictionary.get("largest", "$")
        else:
            index = int((value - smallest) * 9 / (largest - smallest))
            art_line = dictionary.get(index + 1, "")

        art.append(art_line)

    return "".join(art)


if __name__ == "__main__":
    line = input()
    while line != "":
        values = []
        for x in line.split():
            values.append(int(x))
        print(art_generator(values))
        line = input()
