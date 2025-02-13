
#joining the numpy arrays - we will pass concatenate()

import numpy as np
x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.concatenate((x,y))
print(z)


#joining the 2-D arrays along with rows(axis =1)
import numpy as np
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
z = np.concatenate((x,y), axis =1)
print(z)

#joining arrray using stack() function
import numpy as np
x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.stack((x,y), axis =1)
print(z)

# stacking along with rows: hstack()
import numpy as np
x = np.array([1,2,3])
y = np.array([4,5,6])   
z = np.hstack((x,y))
print(z)    


