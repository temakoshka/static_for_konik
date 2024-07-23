def scramble(s1, s2):
    for i in s2:
        if s2.count(i) == s1.count(i):
            continue
        else:
            return False
    return True

print(scramble('ykubd', 'vsasinvy'))