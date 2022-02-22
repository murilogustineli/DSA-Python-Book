"""
R-1.4
"""


def sumSquares(n):
    if n < 0 or not isinstance(n, int):
        return "n is not a positive integer"

    else:
        total = 0
        for i in range(1, n):
            total += i**2
        return total


# One line of code
def sumSquaresSimple(k):
    return sum(x*x for x in range(1, k))


if __name__ == '__main__':
    nums = [0, 2, 10, -5]
    for n in nums:
        print(sumSquares(n))
