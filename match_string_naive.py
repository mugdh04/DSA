import time

def naive(text, pattern):
    n = len(text)
    m = len(pattern)

    start = time.time()
    
    for i in range(n):
        for j in range(m):
            if text[i + j] != pattern[j]:
                break
        else:
            print(f"Pattern found at index {i}")

    end = time.time()
    time_taken = end - start
    return time_taken

text = "The quick brown fox jumps over the lazy dog."
pattern = "b dog"

tt = naive(text, pattern)

print(f"Time taken = {tt}")