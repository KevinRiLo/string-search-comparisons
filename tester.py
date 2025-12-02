import algorithms
import time
import matplotlib.pyplot as plt

# This file is used to run and test the different algorithms.
# It runs all of the algorithms with multiple patterns, and with one pattern.
# At the end of the testing, this program creates and shows a plot of the results.


# TODO: Edit each algorithm to return the runtime after everysingle pattern so the 
# plot will be more accurate.



def multi_naive(text, pattern): # Method runs naive search with multiple patterns
    start_time = time.time()
    time.perf_counter()
    for i in range(len(pattern)):
        if algorithms.naive(text, pattern[i]):
            print(f"'{pattern[i]}' found in text")
        else:
            print(f"'{pattern[i]}' not found in text")
    total_time = time.time() - start_time
    print(f"Run time of naive algorithm: {total_time:.6f} seconds")
    return total_time

def multi_kmp(text, pattern): # Method runs KMP search with multiple patterns
    start_time = time.time()
    time.perf_counter()
    for i in range(len(pattern)):
        if algorithms.kmp(text, pattern[i]):
            print(f"'{pattern[i]}' found in text")
        else:
            print(f"'{pattern[i]}' not found in text")
    total_time = time.time() - start_time
    print(f"Run time of KMP algorithm: {total_time:.6f} seconds")
    return total_time

def multi_boyer_moore(text, pattern): # Method runs Boyer-Moore search with multiple patterns
    start_time = time.time()
    time.perf_counter()
    for i in range(len(pattern)):
        if algorithms.boyer_moore(text, pattern[i]):
            print(f"'{pattern[i]}' found in text")
        else:
            print(f"'{pattern[i]}' not found in text")
    total_time = time.time() - start_time
    print(f"Run time of Boyer-Moore algorithm: {total_time:.6f} seconds")
    return total_time

# Multiple patterns
patterns = []
# Single pattern
single_pattern = ["Then Jove's daughter Minerva came up to them, having assumed the form and voice of Mentor."]
# single_pattern = ["Hello"]
# Plot values
x = [1, 10, 100, 300, 600, 1000]
y1 = []
y2 = []
y3 = []

with open("odyssey.txt", "r") as file:
    test_string = file.read().replace('\n', ' ') # Reads file and replaces new lines with a space character
    file.close()

with open("words.txt", "r") as file:
    content = file.read().replace('\n', ' ')
    patterns = content.split()
    file.close()

print("\n\nNaive algorithm testing:\n\n")
y1.append(multi_naive(test_string, single_pattern))
y1.append(multi_naive(test_string, patterns[:10]))
y1.append(multi_naive(test_string, patterns[:100]))
y1.append(multi_naive(test_string, patterns[:300]))
y1.append(multi_naive(test_string, patterns[:600]))
y1.append(multi_naive(test_string, patterns))


print("\n\nKMP algorithm testing:\n\n")
y2.append(multi_kmp(test_string, single_pattern))
y2.append(multi_kmp(test_string, patterns[:10]))
y2.append(multi_kmp(test_string, patterns[:100]))
y2.append(multi_kmp(test_string, patterns[:300]))
y2.append(multi_kmp(test_string, patterns[:600]))
y2.append(multi_kmp(test_string, patterns))


print("\n\nBoyer-Moore algorithm testing:\n\n")
y3.append(multi_boyer_moore(test_string, single_pattern))
y3.append(multi_boyer_moore(test_string, patterns[:10]))
y3.append(multi_boyer_moore(test_string, patterns[:100]))
y3.append(multi_boyer_moore(test_string, patterns[:300]))
y3.append(multi_boyer_moore(test_string, patterns[:600]))
y3.append(multi_boyer_moore(test_string, patterns))

plt.plot(x,y1, label="Naive", marker='o')
plt.plot(x,y2, label="KMP", marker='o')
plt.plot(x,y3, label="Boyer-Moore", marker='o')
plt.xlabel("Number of Patterns")
plt.ylabel("Runtime (sec)")
plt.title("Algorithm Runtimes Over Different Numbers of Patterns")
plt.show()


