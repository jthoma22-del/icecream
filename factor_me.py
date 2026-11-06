'''
Joshua Thomas
Section 16
This program finds the prime factors of a number using division and stopping once the divisor
passes the square root of the number.

'''

factor_list = []  # stores the prime factors as we find them
num = int(input())  # user input
divisor = 2  # smallest prime factor, starts the divsion proccess


# Keep going while divisor is <=sqrt(num).
# Factors come in pairs, and at least one factor in every
# pair has to be at or below the square root. No need to check divisors
# larger than the square root.

while divisor*divisor <= num:
    if num % divisor == 0:
        factor_list.append(divisor)
        num = num//divisor
    else:
        divisor += 1

if num > 1:  # Check for the last factor after the loop.
    factor_list.append(num)
print("*".join(str(factor) for factor in factor_list))
