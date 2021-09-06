# Sort the array according to the occurrence of numbers

# Function to sort the occurence freq in increasing order
def sorted_freq(freq):
    return sorted(freq.items(), key=lambda kv: (kv[1], kv[0]))


# Function to find the frequency of each number in a list
def find_freq(arr):
    freq = {}
    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    res = sorted_freq(freq)
    print([item[0] for item in res][::-1])


array = [
    1, 1, 1, 2, 3, 4, 9, 0, 2, 2, 3, 4, 3, 2, 1, 5, 5, 9, 0, 0, 1, 1, 1, 1, 2,
    5, 6, 7, 7, 8, 9, 0, 0, 4, 4, 4, 6, 6, 6, 6, 6, 7, 7, 7
]
find_freq(array)
