

'''
Joshua Thomas
Section 16

This programs takes a binary string input(1s or 0s) from the user, then converts it to base 10, a decimal number.
'''

binary_string = input()

power = len(binary_string)-1
count = 0

for bit in binary_string:
    count += int(bit)*2**power
    power -= 1

print(count)
