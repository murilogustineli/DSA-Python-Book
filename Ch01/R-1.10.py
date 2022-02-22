"""
R-1.10
"""


def parameters():
    nums = []
    for i in range(8, -10, -2):
        nums.append(i)
    return nums


if __name__ == '__main__':
    print(*parameters())
    