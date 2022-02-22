"""
R-1.1
Write a short function is_multiple(n, m), that takes two integer values and returns True if n is a multiple of m
that is, n = mi for some integer i, and False otherwise
"""


def is_multiple(n, m):
    if n % m == 0:
        return True
    return False


if __name__ == '__main__':
    n = 6
    m = 3
    print(is_multiple(n, m))