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
    biggest_int = 0
    for i in range(n,0,-1):
        sum_of_digits = sum(int(digit) for digit in str(i))
        if sum_of_digits > biggest_so_far:
            biggest_so_far = sum_of_digits
            biggest_int = i
    return biggest_int

