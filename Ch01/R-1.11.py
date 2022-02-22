"""
R-1.11
"""


def multiply_naive():
    nums = [1]
    n = 1
    while n < 256:
        n += n
        nums.append(n)
    return nums


def multiply_loop():
    nums = []
    for n in range(9):
        nums.append(2**n)
    return nums


def power():
    return [2**x for x in range(9)]


if __name__ == '__main__':
    print(multiply_naive())
    print(multiply_loop())
    print(power())
