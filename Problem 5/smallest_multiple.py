"""
What we're trying to solve: https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

calculating = True
num = 20
while calculating:
    if all(num % i == 0 for i in range(1, 21)):
        print("The smallest multiple is: ", num)
        calculating = False
    else:
        print(num)
        num += 20
