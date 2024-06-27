li = [ 'sachin',123,13.3,'opp']
listr =[]
liint =[]
lifoalt = []
print(li)
for i in li:
    if isinstance(i,str):
        listr.append(i)
    elif isinstance(i,int):
        liint.append(i)
    else:
        lifoalt.append(i)

print(listr)        
print(liint)
print(lifoalt)

