
def name(n):
    '''hi'''
    print(f'my name is {n}')

print(name.__doc__)
name('uday')    

# func with arguement

def sum(a,b):
   
    return print(f'sum = {a+b}')

def main():
    a = int(input('enter: '))
    b =int(input('enter: '))
    return sum(a,b)
    
    
if __name__ =='__main__':
    main()



