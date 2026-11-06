
'''
Joshua Thomas
Section 16

This program takes input from the user to determine how many numbers (1 + 2 + 3 + ...) 
must be added together before the Gauss sum reaches or exceeds the number the user enters.
'''
N = int(input())  # target input from user
iterations = 0  # a count of the added numbers
total_value = 0  # Gauss' sum

# If N is 0 or negative, the loop never runs, so both values stay 0.
# loop continues while total value is less than inputted number,
# so it stops once the sum reaches or exceeds it
while total_value < N:
    iterations += 1
    total_value += iterations

print(f"After {iterations} iterations, the gauss sum is {total_value} which exceeds (or is equal to) the number {N}")
