# Write python code to jumble 2 strings without using any built-ins.
# Take chars from alternate indexes and shift.
# Before running you must ensure both strings are of same length.
# Handle exceptions.

# Function to find the minimum of two numbers
def find_min(m, n):
    if m < n:
        return m
    return n


# Function to find the length of the list
def find_length(string):
    length = 0
    for item in string:
        length += 1
    return length


# Function to combine two different string into one in alternate forms
def func(str1, str2):
    m = find_length(str1)
    n = find_length(str2)
    res = ""
    min_len = find_min(m, n)
    i = 0
    while i < min_len:
        res += str1[i] + str2[i]
        i += 1

    while i < m:
        res += str1[i:]
        i += 1

    while i < n:
        res += str2[i:]
        i += 1

    return res


print(func("hello", "worlds"))
print(func("Python", "JavaCP"))
