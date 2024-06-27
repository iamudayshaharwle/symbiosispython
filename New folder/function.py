# func with variable lenght arguments
def add(farg,*args):
    '''to add given numbs'''
    print('formal argument= ',farg)
    sum = 0
    for i in args:
        sum += i
    print('sum of all numbs',(farg + sum))    
    return

add(1,2,3,4,5,6,7)

#func with keyword based arguments

def display(farg,**kwargs):
    print('formal argument: ',farg)
    for x,y in kwargs.items():
        print('key={}| value={} '.format(x,y))

display(1,rno=10,name='arun',marks=100,grade='first')        

#multiple value returning funcition
def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    return c,d,e,f

p,q,r,s=cal(12,16)
print('add is {}'.format(p))
print('sub is {}'.format(q))
print('multi is {}'.format(r))
print('div is {}'.format(s))

    
