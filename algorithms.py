

# This file contains all of the string-search algorithms 
# and the helper algorithms needed.


def naive(text, pattern): # naive search algorithm
    t = list(text) # convert string to a list of characters
    p = list(pattern) # convert pattern to a list of characters
    is_matching = False
    result = []
    for i in range(len(t) - len(p)):
        for j in range(len(p)):
            if t[i+j] != p[j]: # check if pattern matches current index of string
                is_matching = False
                break
            else:
                is_matching = True
        if is_matching:
            result.append(i)
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
    return result 

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
    matches = []
    i = m-1
    while i < n:
        j = m-1
        while j>= 0 and p[j] == t[i]:
            i = i-1
            j = j-1
        if j == -1:
            matches.append(i) # Match found
        i = i + max(bc_table.get(t[i]), m-j)
    return matches

class Node:
    def __init__(self):
        self.child = {}
        self.fail = None
        self.output = []

def build_trie(patterns):
    root = Node()

    for pattern in patterns:
        curr = root
        for i in pattern:
            if i in curr.child:
                curr = curr.child[i]
            else:
                new_node = Node()
                curr.child[i] = new_node
                curr = new_node
        curr.output.append(pattern)

    return root

def build_failure_links(root):
    queue = []

    root.fail = root
    
    for i, node in root.child.items():
        node.fail = root
        queue.append(node)
    
    head = 0
    while head < len(queue):
        curr = queue[head]
        head += 1
    
        for i, next_node in curr.child.items():
            queue.append(next_node)

            f = curr.fail
            while f is not root and i not in f.child:
                f = f.fail
            
            if i in f.child:
                next_node.fail = f.child[i]
            else:
                next_node.fail = root
            next_node.output += next_node.fail.output

def search(text, root):
    curr = root
    matches = []

    for i, c in enumerate(text):

        while curr is not root and c not in curr.child:
            curr = curr.fail


        if c in curr.child:
            curr = curr.child[c]
        else:
            curr = root

        for pattern in curr.output:
            matches.append((pattern, i))

    return matches

