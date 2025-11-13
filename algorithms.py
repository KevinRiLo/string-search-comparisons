def naive(text, pattern): # naive search algorithm
    t = list(text) # convert string to a list of characters
    p = list(pattern) # convert pattern to a list of characters
    result = False
    for i in range(len(t) - len(p)):
        for j in range(len(p)):
            if t[i+j] != p[j]: # check if pattern matches current index of string
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
    text = list(text) # Convert text to character list
    pattern = list(pattern) # Convert pattern to character list
    lps = lps_array(pattern) # Fill out LPS array 

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
    
    return result #This returns all indexes of matches

def bad_character_heuristic(pattern): # Algorithm fills out bad character table for use in Boyer_Moore algorithm
    m = len(pattern) # m = length of pattern
    bc_table = {}
    for i in range(127): # Loop through all ascii values
        bc_table.update({chr(i): m}) # Fill out all values with m
    for i in range(m):
        bc_table.update({pattern[i]: (m - i - 1)}) # Update values of the characters in the pattern with their rightmost index
    
    return bc_table

def boyer_moore(text, pattern): # Boyer-Moore search algorithm
    t = list(text)  # Convert text to char list
    p = list(pattern)   # Convert pattern to char list
    n = len(t) # n = length of t
    m = len(p) # m = length of p
    bc_table = bad_character_heuristic(p) # Initialize B-C table

    i = m-1
    while i < n:
        j = m-1
        while j>= 0 and p[j] == t[i]:
            i = i-1
            j = j-1
        if j == -1:
            return True # Match found
        i = i + max(bc_table.get(t[i]), m-j)
    return False    # No match found in entire text

