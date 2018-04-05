def get_product_of_3_numbers(data):
    first_max = 0, -1e9
    second_max = 0, -1e9
    third_max = 0, -1e9

    for i in range(len(data)):

        if first_max[1] < data[i]:
            first_max = i, data[i]

    for i in range(len(data)):
        if (i != first_max[0]) and (second_max[1] < data[i]):
            second_max = i, data[i]

    for i in range(len(data)):
        if (first_max[0] != i) and (second_max[0] != i) and (third_max[1] < data[i]):
            third_max = i, data[i]

    print first_max, second_max, third_max
    return first_max[1] * second_max[1] * third_max[1]


print get_product_of_3_numbers([1, 5, 2, 9, 4, 7, 6])
