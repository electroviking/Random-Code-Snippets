def is_anagram():
    word = "nonsense"
    _word = "sensenon"

    def build_hmap(data, hmap):
        for i in range(len(data)):
            hmap[data[i]] = hmap.get(data[i], 0) + 1
        return hmap

    return build_hmap(word, dict()) == build_hmap(_word, dict())


print is_anagram()
