
# difference between numpy array copy and view
# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
import numpy as np
x = np.array([1,2,3,4])
x1 = x.copy()
print(x)
print(x1)

# now we will make a view , change original and display both
 # The view method creates a new array object that looks at the same data.
 # Changing the data in the original array changes the data in the view.
 # Any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
 # The copy method makes a complete copy of the array and its data.
 # Any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
 # The copy owns the data and any changes made to the copy will not affect original array.
    # The view does not own the data and any changes made to the view will affect the original array.
    # If we modify the view, the original array will be modified as well.
    # If we modify the copy, the original array is not modified.

import numpy as np 
x = np.array([1,2,3,4])
x1 = x.view()
x[0] = 10
print(x)
print(x1)

