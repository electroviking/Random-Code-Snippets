arbitrary_list = [12, 1, 4, 16, 8, 3, 4]


def merger(l, r):
    c = []
    while len(l) != 0 and len(r) != 0:
        if l[0] < r[0]:
            c.append(l[0])
            l.remove(l[0])
        else:
            c.append(r[0])
            r.remove(r[0])

    if len(l) == 0:
        c += r
    else:
        c += l

    return c


def merge_sort(data):
    if len(data) in [1, 0]:
        return data
    else:
        mid = len(data) / 2
        return merger(merge_sort(data[:mid]), merge_sort(data[mid:]))


print merge_sort(arbitrary_list)

