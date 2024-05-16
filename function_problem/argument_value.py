# write a function that take variable number of argument and return their sum 


def summation(*args):  # we can use *args for number of variable of sum
    return sum(args)

result = summation(4,5,6)
print(result)