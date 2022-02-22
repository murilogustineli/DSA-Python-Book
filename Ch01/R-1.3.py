"""
R-1.3
"""


def minMax(data):
    min_idx, max_idx = 0, 0

    if len(data):
        for i in range(1, len(data)):
            if data[min_idx] < data[i]:
                min_idx = i
            elif data[max_idx] > data[i]:
                max_idx = i
        return data[min_idx], data[max_idx]
    else:
        return 'The data sequence is empty'


if __name__ == '__main__':
    print(minMax([1, 2, 3, 4, 5, 6]))
    print(minMax([4, 2, 5, 4, 5, 6]))
    print(minMax([]))
    print(minMax([2, 35, 6]))
