'''

You will be given an integer n and your task will be to return the
largest integer that is <= n and has the highest digit sum.
In the input:
n - integer, n > 0
At the output: number
78 -->  78

'''


def max_digit_sum(n):
    biggest_so_far = 0
    sum = 0
    for digit in str(n):
        sum += int(digit)
        n = n-1
    return biggest_so_far
max_digit_sum(54)