"""
What we're trying to solve: https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding
the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""

# Our main variable used to iterate the fibonacci sequence.
fib_list = [0, 1]

# The total sum of all even fibonacci numbers added together.
sum_even_fib = 0

# The total of the first and second fibonacci number passed to
# it added together.
total = 0

while total < 4000000:

    # 'x' will always be equal to the first number presented in
    # the list whereas 'y' will always equal the second number.
    x = fib_list[0]
    y = fib_list[1]
    total = x + y

    # If the calculated total is divisible by 2, we add it to
    # the total value of even fibonacci numbers.
    if total % 2 == 0:
        sum_even_fib += total
    # Deletes the first number from the list and then appends
    # the previous total of those two numbers to the list.
    del fib_list[0]
    fib_list.append(total)

print("The sum of all even fibonacci numbers is:", sum_even_fib)
