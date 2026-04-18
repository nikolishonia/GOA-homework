# 1

def spin_words(sentence):
    words = []
    for i in sentence.split():
        if len(i) == 5 or len(i) > 5:
            words.append(i[::-1])
        else:
            words.append(i)
    return " ".join(words)

# 2

def capitalize(s):
    ns1 = ""
    ns2 = ""
    for i in range(len(s)):
        if i % 2 == 0:
            ns1 += s[i].upper()
            ns2 += s[i]
        elif i % 2 == 1:
            ns1 += s[i]
            ns2 += s[i].upper()
    return [ns1, ns2]

# 3

def reverse_words(text):
    rvrsed = []
    for i in text.split(" "):
        rvrsed.append(i[::-1])
    return " ".join(rvrsed)

# 4

def vowel_indices(word):
    vc = []
    vowels = "aeiyouAEIYOU"
    for i in range(len(word)):
        if word[i] in vowels:
            vc.append(i + 1)
    return vc

# 5

def show_sequence(n):
    nums = []
    if n > 0:
        for i in range(n + 1):
            nums.append(str(i))
            
        return("+".join(nums) + " = " + str(sum(range(n + 1))))
    elif n < 0:
        return(str(n) + "<0")
    elif n == 0:
        return(str(n) + "=0")
