from itertools import permutations


def get_all_anagrams(data, n):
    perm = {"".join(i): "".join(i) for i in permutations(n)}
    res = []

    for i in range(len(data) - len(n) + 1):
        if perm.get(data[i:i + len(n)]):
            res.append(i)
    return res


print get_all_anagrams("cbaebabacd", "abc")
