import numpy as np

a = np.mgrid[1:8:1, 2:5:0.5, 2:12]
print(a)
print(dir(a))
# print(help(np.mgrid))