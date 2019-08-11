def permu(st1, st2):
    if sorted(st1) == sorted(st2):
        return True
    else:
        return False

s1 = 'Hello World'
s2 = 'World Hello'
print(permu(s1,s2))
