"""
Joshua Thomas (Section 16)
The program takes user input to write a 
calculator that tells if a 2x2 Sudoku is solved or unsolved.
"""

a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a!=b and c!=d and a!=c and b!=d:
    print("solved")
else:
    print("unsolved")