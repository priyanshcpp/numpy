# data types in numpy

#int
#bool
#unsigned int
#float
#complex float - c 
#timedelta - m
#datetime - M
#object
#string - S
#unicode string - U
#v - memory

#checking the data type of numpy array

import numpy as np
x = np.array([1,2,3,4])
print(x.dtype)

# checking the data type of numpy array - string

import numpy as np
x = np.array(['apple','banana','cherry'])
print(x.dtype)

# creating array with a defined data type: 

import numpy as np
x = np.array([1,2,3,4],dtype='S')
print(x)
print(x.dtype)

# now we will create an array with data type 4 bytes integer

import numpy as np
x = np.array([1,2,3,4], dtype = 'i4')
print(x)
print(x.dtype)

# if a type is given  in which the elements cannot be casted then numpy will raise a ValueError. what if a value cannot be converted?
# Let's see an example:

 #import numpy as np
 #x = np.array(['a','2','3'],dtype='i')
 #print(x)

# The above code will raise an error because 'a' cannot be converted to integer.

# Converting Data Type on Existing Arrays
# The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
# The astype() function creates a copy of the array, and allows we to specify the data type as a parameter.
# The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or we can use the data type directly like float for float and int for integer.


import numpy as np
x = np.array([1.1,2.1,3.1])
x1 = x.astype('i')
print(x1)
print(x1.dtype)

# Change data type from float to integer by using 'i' as parameter value:

# converting from int to bool

import numpy as np
x = np.array([1,0,3])
x1= x.astype(bool)
print(x1)
print(x1.dtype)


# how to push this file on github
# git init
# git add datatypes.py
# git commit -m "first commit"
# git remote add origin
# git push -u origin master
# git push origin master
