def uniChar(s):
    char_set = [False] * 128
    for i in range(len(s)):
        val = ord(s[i])
        if char_set[val]:
            return False
        else:
            char_set[val] = True
    return True

st = 'quick brownsta'
print(uniChar(st))
