def is_armstrong_number(data):
    print str(sum([int(data[i]) ** int(len(list(data))) for i in range(len(list(data)))])) == data

    result = []
    new_list = list(data)
    whole_len = len(new_list)
    for i in range(whole_len):
        result.append(int(data[i]) ** whole_len)
    return sum(result)


print is_armstrong_number("153")

# 1*1*1 + 3*3*3 + 5*5*5
