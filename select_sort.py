arbitrary_list = [1, 5, 12, 7, 34, 8, 0, 82, 8]


def select_sort(data):
    for i in range(len(data) - 1):
        min_value = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_value]:
                min_value = j
        if min_value != i:
            data[min_value], data[i] = data[i], data[min_value]
    return data


print select_sort(arbitrary_list)
