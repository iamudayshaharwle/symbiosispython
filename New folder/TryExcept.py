
try:
    
    num =int(input())
    print(num)

except TypeError as e:
    print(f'invalid input:{e}')

finally:
    print("always")