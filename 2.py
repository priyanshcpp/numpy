import numpy as np
x = np.array([1,2,3,4,5])
print(x[1])

#Array indexing is the same as accessing an array element.

# we can get the third and fourth elements from adding them

import numpy as np
x = np.array([1,2,3,4,5])
print(x[2]+x[3])


# 2-D Arrays- In a 2-D array, the first dimension is rows and the second dimension is columns.
import numpy as np
x = np.array([[1,2,3,4,5],[6,7,8,9,10]]) 
#print('2nd elements in 1st row:', x[0,1])

print('5th element in the 2nd row:', x[1,4])

# accessing 3-D arrays

import numpy as np
x = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(x[0,1,2])