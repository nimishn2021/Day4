# Write a function that takes **kwargs as an input and finds out the final values. 
#   - Use decorators to execute the code (Optional)
#   - Handle all Exceptions

# Function to find the maximum of a list
def find_max(arr):
    maxi = arr[0]
    for item in arr:
        if item > maxi:
            maxi = item
    return maxi


# Function to find the minimum of a list
def find_min(arr):
    mini = arr[0]
    for item in arr:
        if item < mini:
            mini = item
    return mini


# function for calculating sum
def find_sum(arr):
    total = 0
    for item in arr:
        total += item
    return total


# function to find the length of the list
def find_len(arr):
    length = 0
    for _ in arr:
        length += 1
    return length


# function to calculate average of the numbers in the list
def find_avg(arr):
    total = find_sum(arr)
    count = find_len(arr)
    return total / count


def ex19(**kwargs):
    inp_val = [value for key, value in kwargs.items()]
    action = inp_val.pop()
    if action == 'sum':
        return find_sum(inp_val)
    elif action == 'avg':
        return find_avg(inp_val)
    elif action == 'max':
        return find_max(inp_val)
    elif action == 'min':
        return find_min(inp_val)


print(ex19(x=100, y=200, z=150, a=300, b=180, e=90, f=25, g=80, h=120, action="avg"))

print(ex19(x=100, y=200, z=150, a=300, b=180, e=90, f=25, g=80, h=120, action="sum"))

print(ex19(x=100, y=200, z=150, a=300, b=180, e=90, f=25, g=80, h=120, action="max"))

print(ex19(x=100, y=200, z=150, a=300, b=180, e=90, f=25, g=80, h=120, action="min"))
