from numpy import *
from numpy.linalg import solve


A = array([ [1, 3, 2], [1, 0, 0], [2, 1, 1]])
B= array([4,5,6])

print solve(A,B)