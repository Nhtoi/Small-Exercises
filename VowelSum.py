def vowelSum(sentece):
    vowels = "a,e,i,o,u"
    utf = []
    dictionary = {}
    for words in sentece:
        for c in words:
            if c in vowels:
                dictionary[c] = dictionary.get(c, 0) + 1
                c.lower()
                utf.append(ord(c) - ord("a"))
    return len(utf), sum(utf), dictionary
print(vowelSum("mfs are actually wilding and they bouncing on it"))