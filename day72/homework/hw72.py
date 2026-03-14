# 2)

def get_sum(a,b):
    sum = 0
    if a < b:
        for i in range(a, b + 1):
            sum += i
    else:
        for i in range(b, a + 1):
            sum += i
    return sum


# 3)

def is_isogram(string):
    string = string.lower()
    for i in string:
            if string.count(i) > 1:
                return False
    return True


# 4)

def well(x):
    bad = 0
    good = 0
    for i in x:
        if i == "bad":
            bad += 1
        elif i == "good":
            good += 1
    if good > 2:
        return("I smell a series!")
    elif good > 0:
        return("Publish!")
    elif good == 0:
        return("Fail!")
    
    
    # 5)
    
    def warn_the_sheep(queue):
        wolf_index = queue.index("wolf")
        
        if queue[-1] == "wolf":
            return("Pls go away and stop eating my sheep")
        else:
            return("Oi! Sheep number " + str(len(queue) - (wolf_index+1)) + "! You are about to be eaten by a wolf!")
        
    
def sum_digits(number):
    sum = 0
    for i in str(number):
        sum += int(i)
    return sum