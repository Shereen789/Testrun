def maxBlock(word):
    m= 1
    ma = 0
    for i in range(0,len(word)-1):
        if word[i] == word[i+1]:
        m+=1
        if m>ma:
            ma = m
        else:
        m = 1
    return ma
