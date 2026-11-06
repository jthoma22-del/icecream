# This program takes a list of numbers, then appends it to a new list after squaring the even numbers
#  while leaving the odd number the same.

num_list = []
n = int(input("Enter a number:  "))
while n != 0:
    if n % 2 == 0:
        num_list.append(n**2)
    else:
        num_list.append(n)
    n = int(input("Enter a number:  "))
print(num_list)

'''''
#This progran takes a list as argument and adds the numbers if they are even

num_list = []
n = int(input("Enter a number: "))
result = 0
while n != 0:
    num_list.append(n)
    if n % 2 == 0:
        result += n
    n = int(input("Enter a number: "))
print(result)


num_list = []
result = 0
while True:
    n = int(input("Enter a number:  "))
    if n == 0:
        break
    num_list.append(n)
    if n % 2 == 0:
        result += n
print(result)
'''
