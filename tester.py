import algorithms
import time
import matplotlib.pyplot as plt

# This file is used to run and test the different algorithms.
# It runs all of the algorithms with multiple patterns, and with one pattern.
# At the end of the testing, this program creates and shows a plot of the results.


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
patterns = ["hi", "hello", "Hello", "how are you", "Tell me", "Muse", "was now gone"]
# Single pattern
single_pattern = ["Then Jove's daughter Minerva came up to them, having assumed the form and voice of Mentor."]

# Plot values
x = ["Naive", "KMP", "Boyer-Moore"]
y = []
z = []


with open("odyssey.txt", "r") as file:
    test_string = file.read().replace('\n', ' ') # Reads file and replaces new lines with a space character
    file.close()

print("\n\nMulti pattern testing:\n\n")
y.append(multi_naive(test_string, patterns))
y.append(multi_kmp(test_string, patterns))
y.append(multi_boyer_moore(test_string, patterns))

print("\n\nSingle pattern testing:\n\n")
z.append(multi_naive(test_string, single_pattern))
z.append(multi_kmp(test_string, single_pattern))
z.append(multi_boyer_moore(test_string, single_pattern))

# Plot the runtimes of the algorithms when using multiple patterns
plt.bar(x, y)
plt.xlabel("Algorithm")
plt.ylabel("Run time (sec)")
plt.title("Multi-Pattern Run Times")
plt.show()

# Plot the runtimes of the algorithms when using one pattern
plt.bar(x, z)
plt.xlabel("Algorithm")
plt.ylabel("Run time (sec)")
plt.title("Single-Pattern Run Times")
plt.show()