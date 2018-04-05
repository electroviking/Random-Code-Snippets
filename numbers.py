from itertools import permutations

OPERATORS = ["+", "-", "*", "/"]


def get_all_permutations(data):
    # number of operands needed to find all permutations
    __num_operands__ = len(list(data)) - 1
    return [perm for perm in set(permutations(OPERATORS * __num_operands__, __num_operands__))]


def rpn(data, target=30):
    __results = []
    __infix_string = []
    for permutation in get_all_permutations(data):
        for ch in range(len(data)):
            if ch < len(permutation):
                __infix_string.append(data[ch])
                __infix_string.append(permutation[ch])
            else:
                __infix_string.append(data[ch])

        __possible_target = "".join(__infix_string)
        if eval(__possible_target) == target:
            __results.append(__possible_target)
        __infix_string = []
    return __results


print rpn("1239")
