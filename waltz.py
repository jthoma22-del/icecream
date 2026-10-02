

'''''
Joshua Thomas
Section 16

The program takes the user input for the number of steps in a waltz, then produces 
a string version of the steps.
'''

steps = int(input())

result = ""
for step in range(steps):
    result += str(step % 6 + 1)

print(result)
