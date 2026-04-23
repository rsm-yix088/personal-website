# %%
def shortest_word(words):
    word1, word2 = words[0], words[1]
    len1, len2 = len(words[0]), len(words[1])

    if len1 > len2:
        s = len1
    elif len1 < len2:
        s = len2
    else:
        s = len1
    return s  # length of the shortest word


shortest_word(["mouse", "king"])  # should return 4

shortest_word(["tax", "house"])  # should return 3
shortest_word(["purple", "orange"])  # should return 6
