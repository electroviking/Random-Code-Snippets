def is_palidrome(data):
    if len(data) == 1:
        return True
    else:

        if data[0] != data[-1]:
            return False
        else:
            return is_palidrome(data[1:-1])


print is_palidrome("abcba")


def first_method(data):
    return data[::-1] == data


def second_method(data):
    count = len(data) - 1
    for i in range(len(data) / 2):
        if data[i] != data[count]:
            return False
        count -= 1
    return True


# print second_method("abba")

def longest_palidrome(s):
    from collections import Counter
    return min(sum(i for i in Counter(s).values()) + 1, len(s))

# print longest_palidrome("abcvbc")
