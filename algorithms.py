def naive(text, pattern): # naive search algorithm
    t = list(text) # convert string to a list of characters
    p = list(pattern) # convert pattern to a list of characters
    result = False
    for i in range(len(t) - len(p)):
        for j in range(len(p)):
            if t[i+j] != p[j]: # check is pattern matches current index of string
                result = False
                break
            else:
                result = True
        if result:
            return result
    return result


def lps_array(pattern): # Algorithm for getting the LPS array used in KMP
    m = len(pattern)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length +=1
            lps[i] = length
            i+=1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i+=1
    return lps



def kmp(text, pattern): # KMP search algorithm
    lps = lps_array(pattern)

    i = 0  
    j = 0  
    result = []

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == len(pattern):
                result.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return result
    
