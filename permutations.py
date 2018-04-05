def get_permutations(data):
    res = []
    for i in range(len(data) * 2):
        r = data[i:] + data[:i]
        res.append(r)
        res.append(r[::-1])
    return res


def permute(nums):
    res = []
    dfs(nums, [], res)
    return res


def dfs(nums, path, res):
    print nums
    print path
    print res

    if not nums:
        res.append(path)
        # return # backtracking
    for i in xrange(len(nums)):
        dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


# print permute([1, 2, 3])

def checkInclusion(s1, s2):
    from itertools import permutations
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    all_permutations = permutations(s2)
    print list(all_permutations)
    print s1*2

    return any(["".join(list(i)) in s1 * 2 for i in all_permutations])


print checkInclusion("ooolleoooleh", "hello")




a = "abcabc"
# abc
# bca
# cab