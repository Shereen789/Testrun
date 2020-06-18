def maxBlock(word):
    count= 0
    ma = 0
    for i in word:
        count = word.count(i)
        if count>ma:
            ma = count
    return ma
