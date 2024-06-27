import random

p = random.randint(2,10)
print(p)

q = random.randrange(2,10)
print(q)

fruits =['mango','apple','orange','banana','coconuts','stawberry']
print(random.choice(fruits))


r = random.random()
print(r)

random.shuffle(fruits)
print(fruits)

s = random.uniform(2,8)
print(s)

