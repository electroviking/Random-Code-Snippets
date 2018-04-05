def reverse_an_array(data):
    end = len(data) - 1
    for start in range(len(data) / 2):
        data[start], data[end] = data[end], data[start]
        end -= 1
    return data


print reverse_an_array([5, 2, 1, 6, 3, 7])
