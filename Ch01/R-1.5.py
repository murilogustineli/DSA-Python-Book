"""
R-1.5
"""


def sumSquares(k):
    return sum(x*x for x in range(1, k))


if __name__ == '__main__':
    nums = [0, 2, 10, -5]
    for n in nums:
        print(sumSquares(n))
        