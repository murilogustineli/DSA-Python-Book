"""
R-1.9
"""


def parameters():
    nums = []
    for i in range(50, 90, 10):
        nums.append(i)
    return nums


if __name__ == '__main__':
    print(*parameters())
