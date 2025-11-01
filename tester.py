import algorithms
import time

def multi_naive(text, pattern): # Method runs naive search with multiple patterns
    start_time = time.time()
    time.perf_counter()
    for i in range(len(pattern)):
        if algorithms.naive(text, pattern[i]):
            print(f"'{pattern[i]}' found in text")
        else:
            print(f"'{pattern[i]}' not found in text")
    total_time = time.time() - start_time
    print(f"Run time of algorithm: {total_time:.6f} seconds")

def multi_kmp(text, pattern): # Method runs KMP search with multiple patterns
    start_time = time.time()
    time.perf_counter()
    for i in range(len(pattern)):
        if algorithms.kmp(text, pattern[i]):
            print(f"'{pattern[i]}' found in text")
        else:
            print(f"'{pattern[i]}' not found in text")
    total_time = time.time() - start_time
    print(f"Run time of algorithm: {total_time:.6f} seconds")

patterns = ["hi", "hello", "Hello", "how are you", "Tell me", "Muse", "was now gone", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbba"]
with open("odyssey.txt", "r") as file:
    test_string = file.read()
multi_naive(test_string, patterns)
multi_kmp(test_string, patterns)
