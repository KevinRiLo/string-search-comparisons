def naive(text, pattern):
    t = list(text)
    p = list(pattern)
    result = False
    for i in range(len(t) - len(p)):
        for j in range(len(p)):
            print(f"comparing {t[i+j]} and {p[j]}")
            if t[i+j] != p[j]:
                result = False
                break
            else:
                result = True
        if result:
            return result
    return result

x = "Hello how are you doing today"
y = "how are you"
print(naive(x, y))