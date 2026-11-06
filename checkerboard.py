''''
Joshua Thomas
Section 16
October 29, 2026
This program takes input from the user and generates a checkerboard pattern
 of a given size using two specified symbols.

'''


def checkerboard(size, symbol_1, symbol_2):
    for row in range(size):
        for column in range(size):
            if (row + column) % 2 == 0:  # check if the sum of row and column indices is even
                print(symbol_1, end="")
            else:
                print(symbol_2, end="")
        print()  # Move to the next line after each row


if __name__ == "__main__":
    size = int(input())
    symbols = input().split()
    checkerboard(size, symbols[0], symbols[1])
