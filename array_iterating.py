
# Iterating Array - means going through elements one by one

# iterate the elements of 1-D
import numpy as np
x = np.array([1,2,3,4,5])
for i in x:
    print(i)
 
# iterate the elements of 2-D

import numpy as np
x = np.array([[1,2,3],[4,5,6]])
for i in x:
    print(i)

# iterate on each scalar element of the 2-D array
import numpy as np
x = np.array([[1,2,3],[4,5,6]])
for i in x:
    for j in i:
        print(j)

# iterate the elements of 3-D array
import numpy as np
sharad = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for i in sharad:
    for a in i:
        for b in a:
            print(b)


# Iterating array using nditer()

import numpy as np
x = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for i in np.nditer(x):
    print(i)

import numpy as np
y = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for i in np.nditer(x[:, ::2]):
    print(i)    
 

import numpy as np
z = np.array([[1,2,3,4],[5,6,7,8]])
for i in np.nditer(z[:, ::2]):
    print(i)

    