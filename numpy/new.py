import numpy as np
# creating one dimensional array

a = np.array([1,2,3,4])
print(type(a))
print(a)
print(a.shape)
# two dimensional array

b = np.array([[1,2,3],[4,5,6]])
print(type(b))
print(b)
print(b.shape)
d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(d.shape)
# 3rd dimensional array

c = np.array([[[1,7],[7,4]],[[7,8],[6,9]],[[5,7],[7,4]]])
print(type(c))
print(c)
print(c.shape)
#cheak dimension 

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#len()
print(len(a))
print(len(b))
print(len(c))


#size: return the total number of elements inside the array

print(a.size)

#itemsize: return the lenght of each element of each element of element of array in bytes

print(a.itemsize)