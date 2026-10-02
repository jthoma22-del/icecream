'''
Joshua Thomas
Section 16
The program takes row and colunm unput from user the creates a box of asterisks that border the box only.
'''

r = int(input())
c = int(input())

for i in range(1, r+1):
    for j in range(1, c+1):
        if i == 1 or i == r or j == 1 or j == c:
            print("*", end='')
        else:
            print(" ", end='')
    print()
