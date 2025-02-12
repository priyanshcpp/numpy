# Slicing Array - Slicing in python means taking elements from one given index to another given index.

import numpy as np
kohli = np.array([1,2,3,4,5,6,7,8,9])
print(kohli[1:5])
# The result includes the start index, but excludes the end index.

print(kohli[4:7])


print(kohli[5:])

# By leaving out the start index, the slice will start at the first item.
print(kohli[:4])

import numpy as np
print(kohli[1:])

# Negative Slicing 
import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9])
print(x[-7:-1])

import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9])
print(x[1:5:2])

# now return every other element in the entire array
import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9])
print(x[::2])

# Slicing 2-D Arrays
import numpy as np
x = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(x[1,1:5])
print(x[0,0:4])

print(x[0,3]) #4
print(x[1,3]) #9

print(x[0:2,2])

print(x[0:2,1:4]) 
