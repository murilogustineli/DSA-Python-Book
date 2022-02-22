"""
R-1.7
"""


def sum_squares_odd(n):
    return sum([i ** 2 for i in range(1, n) if i % 2 != 0])


if __name__ == '__main__':
    nums = [2, 4, 0, 10, 5, -6, -72]
    for n in nums:
        print(sum_squares_odd(n))
        