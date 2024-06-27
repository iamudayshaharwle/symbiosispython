 
def sum(fx,value1,value2):
    return 2 + fx(value1,value2)#function in fuunction



square = lambda x: x*x
cube = lambda x: x*x*x

print(square(8))
print(cube(5))
print(sum(lambda x,y: x*y,8,7))