
# shapes of an array - the shape of an array is the number of elements in each dimension.
# now we will try to get the shape of an array

import numpy as np
x = np.array([[1,2,3,4],[5,6,7,8]])
print(x.shape)

# (2,4) - the array the 2 dimensions, each dimension has 4 elements

# we will crete 5D array to understand the shape of an array

import numpy as np
x = np.array([1,2,3,4], ndmin =5)
print(x)
print('shape of the array is', x.shape)


# reshaping an array - we can use reshape method to reshape an array

#reshaping from 1D to 2D array

import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x1 = x.reshape(4,3)
print(x)
print(x1)

# reshaping from 1D to 3D array
import numpy as np
y = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y1 = y.reshape(2,3,2)
print(y1)

import numpy as np
z = np.array([1,2,3,4,5,6,7,8])
z1 = z.reshape(2,2,2)
print(z1)

#retuen copy or view

import numpy as np
x = np.array([1,2,3,4,5,6,7,8])
print(x.reshape(2,4)) # break in 2 indexing and each array has 4 elements
print(x.reshape(2,4).base)

#unknown dimesions - we are only allowed to have one unknown dimension, pass -1 as the value, and numpy will calculate this unknown dimension.
import numpy as np
x = np.array([1,2,3,4,5,6,7,8])
x1 = x.reshape(2,2,-1)
print(x1)

#flattenig the arrays by converting multi-dimensional arrays into 1D arrays
import numpy as np
x = np.array([[1,2,3],[4,5,6]]) 
x1 = x.reshape(-1)
print(x1)

# THere are alot of function for changing the shape of an array, like flat, flatten, ravel and also rearranging the element in an array like flip, rot90, etc.
# these are comes under advanced numpy functions