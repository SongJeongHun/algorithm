import numpy as np
a = ([1,2],[2,3])
b = ([1,0],[0,3])

arrA = np.array(list(a))
arrB = np.array(list(b))

print(arrA.dot(arrB))
