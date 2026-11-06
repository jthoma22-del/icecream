'''
Joshua Thomas
Section 16
The program takes a list of integers from the user and returns a new list
that contains Pascal's triangle row based on the original list. 
The first and last elements of the new list are always the same
as the first and last elements of the input list.
'''


def next_level(level):
    new_sums = [level[0]]

    for i in range(len(level) - 1):
        new_sums.append(level[i] + level[i + 1])

    new_sums.append(level[0])
    return new_sums


if __name__ == "__main__":
    in_string = input()

    while in_string != "":
        values = []
        for x in in_string.split():
            values.append(int(x))

        print(next_level(values))
        in_string = input()
