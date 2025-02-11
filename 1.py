# we will create a numpy ndarray object

import numpy as np
x  = np.array([1,2,3,4,5])
print(x)

print(type(x))

# we can also pass a list, tuple or any array like object to the array. and it will be converted to ndarray

import numpy as np
y = np.array((2,3,4,5,6))
print(y)

print(type(y))

# Dimesions in Array - A dimeension in arrays is one level of array depth (nested arrays). nested arrays are arrays that have arrays as their elements.
# 0-D Arrays - 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
# 1-D Arrays - An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

# we will create a 0-D array with value 57
import numpy as np
x = np.array(57)
print(x)

#1-D array- an array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
import numpy as np
priyanshu = np.array([1,2,3,4,5])
print(priyanshu)

# 2-D Arrays

import numpy as np
x = np.array([[1,2,3],[4,5,6]])
print(x)

# 3-D Arrays

import numpy as np
y = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(y)

#check the number of dimensions of an array using ndim attribute

import numpy as np
a = np.array(57)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
print(a.ndim)
print(b.ndim)
print(c.ndim)

# create an array with 5 dimensions and verify the number of dimensions

import numpy as np
priyanshu = np.array([1,2,3,4,5], ndmin=7)
print(priyanshu)
print('number of dimesions:', priyanshu.ndim)