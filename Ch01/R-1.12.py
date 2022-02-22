"""
R-1.12
Use randrange function to implement your version of the choice function
"""

# Import randrange
from random import randrange


def random(array):
    choice = randrange(0, len(array))
    return array[choice]


def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for _ in range(50):
        print(random(array), end=' ')


if __name__ == '__main__':
    main()
