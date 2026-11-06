def checkerboard(size, symbol_1, symbol_2):
    for row in range(size):
        for col in range(size):
            if row % 2 == 0:
                print(symbol_1, end="")
            else:
                print(symbol_2, end="")
        else:
            if col % 2 == 0:
                print(symbol_2, end="")
            else:
                print(symbol_1, end="")
        print()


# implement this function
if __name__ == "__main__":
    size = int(input())
    symbols = input().split()
    checkerboard(size, symbols[0], symbols[1])


"""def checkerboard(size, symbol_1, symbol_2):
    for row in range(size):
        for column in range(size):
            if (row + column) % 2 == 0:
                print(symbol_1, end=" ")
            else:
                print(symbol_2, end=" ")
        print()  # Start a new line after each row


if __name__ == "__main__":
    size = int(input())
    symbols = input().split()
    checkerboard(size, symbols[0], symbols[1])
"""
