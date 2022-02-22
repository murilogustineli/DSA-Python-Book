"""
R-1.6
"""


def sum_squares_odd(n):
    total = 0
    for i in range(1, n):
        if i % 2 != 0:
            total += i**2
    return total


if __name__ == '__main__':
    nums = [2, 4, 0, 10, 5, -6, -72]
    for n in nums:
        print(sum_squares_odd(n))
