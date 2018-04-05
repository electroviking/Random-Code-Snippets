arbitrary_list = [1, 5, 1, 7, 34, 8, 3, 82, 8]


def bubble_sort(data):
    for i in range(len(data) - 1):
        for j in range(i, len(data)):
            if data[j] < data[i]:
                data[i], data[j] = data[j], data[i]
    return data


print bubble_sort(arbitrary_list)
