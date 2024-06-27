#recursion
def factorial(n):
    if (n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

list1 = [23,22,15,14,12]
print(list(map(factorial,list1)))