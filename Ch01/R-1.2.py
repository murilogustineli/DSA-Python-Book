"""
R-1.2
"""


def is_even(k:int):
    assert type(k) == int, 'Your input must be an int'
    return k & 1 == 0


if __name__ == '__main__':
    print(is_even(2))
    print(is_even(1))
    print(is_even(0))
    print(is_even(100002343))
