import algorithms
import time

def multi_naive(text, pattern):
    start_time = time.time()
    time.perf_counter()
    for i in range(len(pattern)):
        if algorithms.naive(text, pattern[i]):
            print(f"'{pattern[i]}' found in text")
        else:
            print(f"'{pattern[i]}' not found in text")
    total_time = time.time() - start_time
    print(f"Run time of algorithm: {total_time:.6f} seconds")

patterns = ["hi", "hello", "Hello", "how are you", "Tell me", "Muse", "was now gone"]
with open("large.txt", "r") as file:
    test_string = file.read()
multi_naive(test_string, patterns)