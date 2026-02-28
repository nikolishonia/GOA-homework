# 2) 
def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
    return sum

# 3) 
def repeat_str(repeat, string):
    return(string*repeat)

# 4)
def square_sum(numbers):
    sum = 0
    for i in numbers:
        sum += i**2
    return sum

# 5

def string_to_number(s):
    return int(s)
