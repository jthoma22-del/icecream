"""
Joshua Thomas (Section 16)
JupiterFizzBuzz
This program users an integer from the user and determines whether one number is divisible bycertain numbers
using these conditions:
1. If the number is divisible by 6, the program prints "Fizz".
2. If the number is divisible by 10, the program prints "Buzz".
3. If the number is divisible by both 6 and 10, the program prints
"JupiterFizzBuzz".
4. Otherwise, the program prints the number itself.
"""

num=int(input())

if num%6==0 and num%10==0:
    print("JupiterFizzBuzz")
elif num%6==0:
    print("Fizz")
elif num%10==0:
    print("Buzz")
else:
    print(num)


