def maxBlock(word):
    m= 0
    ma = 0
    for i in word:
        m = word.count(i)
        if m>ma:
            ma = m
    return ma
