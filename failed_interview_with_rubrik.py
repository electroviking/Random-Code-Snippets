content = [{"age": 60, "fname": "rom", "lname": "lastname"}]
# {"age": 90, "fname": "tim", "lname": "popov"}
filter_items = [{"age": 90, "fname": "tim"}, {"age": 60, "lname": "lastname"}]

data = [['a', 'b', 'c', "d"], ['a', 'b', 'c', "d"], ['a', 'b', 'c', "d"]]
f = [['a', 'c'], ['a', 'c'], ['a', 'c']]


def find_matching_obj(content, filter_obj):
    result = []
    # "age": 90,

    for filter_items in range(len(filter_obj)):
        for fk, fv in filter_obj[filter_items].items():
            for citems in range(len(content)):
                temp = []
                # print  content[citems]
                for ck, cv in content[citems].items():
                    if content[citems].get(ck) == filter_obj[filter_items].get(fk) and content[citems].get(ck) == \
                            filter_obj[filter_items].get(fk):
                        temp.append(content[citems])


                    else:
                        if temp != [] and content[citems].get(ck) == filter_obj[filter_items].get(fk):
                            temp = []

                if temp != []:
                    result += temp
    abs()
    return result


print find_matching_obj(content, filter_items)
