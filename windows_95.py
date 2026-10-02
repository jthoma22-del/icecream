'''
Joshua Thomas
Section 16
This progam takes input from the user to determine if the created  windows key satisfies two conditions:
The length of the key must be a multiple of 3.
Every third digit (the 3rd, 6th, 9th, ...) must be even.
'''

key = input()
valid = len(key) % 3 == 0


for digit in key[2::3]:
    if int(digit) % 2 != 0:
        valid = False
if valid:
    print("Welcome! Booting the system!")

else:
    print("Invalid key! The authorities have been notified.")
