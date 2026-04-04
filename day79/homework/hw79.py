# 1)
def multi_table(number):
    multtable = []
    for i in range(1,11):
        multtable.append(str(i) + " * " + str(number) + " = " + str(i*number))
    return "\n".join(multtable)


# 3)
def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i -1] != 1:
            return(arr[i])
    return None


