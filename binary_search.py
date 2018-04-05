container = [2, 4, 6, 9, 12, 15]


def binary_Search(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) / 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid + 1
    return -1

print binary_Search(container, 15)
