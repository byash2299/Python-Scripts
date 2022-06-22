# Generator Function
def fib(num):
    a,b = 0,1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b

# Using List
def fib2(num):
    a,b = 0,1
    result = []
    for i in range(num):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

# for x in fib(20):  
#     print(x)

print(fib2(21))