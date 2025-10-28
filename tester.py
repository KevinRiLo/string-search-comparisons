import algorithms

def multi_naive(text, pattern):
    for i in range(len(pattern)):
        if algorithms.naive(text, pattern[i]):
            print(f"{pattern[i]} found in text")
        else:
            print(f"{pattern[i]} not found in text")

patterns = ["hi", "hello", "Hello", "how are you", "Tell me", "Muse", "was now gone"]
with open("Odyssey_Excerpt.txt", "r") as file:
    test_string = file.read()
multi_naive(test_string, patterns)