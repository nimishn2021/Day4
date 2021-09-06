# Write python code to find the count of occurrence of vowels.

# Global variable to store the vowels as list
vowels = ['a', 'e', 'i', 'o', 'u']


# Function to find the frequency of vowels in the string
def func(string):
    freq = {}
    for char in string:
        if char in vowels:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq


print(func("hello world"))
