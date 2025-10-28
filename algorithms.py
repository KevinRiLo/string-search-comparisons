def naive(text, pattern):
    t = list(text)
    p = list(pattern)
    result = False
    for i in range(len(t) - len(p)):
        for j in range(len(p)):
            if t[i+j] != p[j]:
                result = False
                break
            else:
                result = True
        if result:
            return result
    return result