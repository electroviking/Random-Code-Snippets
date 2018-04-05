def subsets(nums):
    def loop(data, n):
        res = []
        for i in data:
            res += [i + [n]]
        return res

    result = [[]]
    for num in nums:
        result += loop(result, num)
    return result


print subsets(["1", "2", "3"])
