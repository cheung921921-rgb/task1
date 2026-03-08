import math
import numpy as np

# 3x+y+4z=23  
# 4x+3y+z=27
# x+8y+6z=40

A = np.array([[3, 1, 4],
              [4, 3, 1],
              [1, 8, 6]])
#Matrix

B = np.array([23, 27, 40])
# constant vector

X = np.linalg.solve(A, B)

print("Solution (x, y, z):", X)
