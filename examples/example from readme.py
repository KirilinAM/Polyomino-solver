import numpy as np
from polyominator import polyomino

area = np.ones((6,4))

T_shape = np.array([
    [1,1,1]
    ,[0,1,0]
])
J_shape = np.array([
    [1,0,0]
    ,[1,1,1]
])
L_shape = np.array([
    [1,1,1]
    ,[1,0,0]
])
Z_shape = np.array([
    [1,1,0]
    ,[0,1,1]
])

figures = [T_shape,T_shape,J_shape,J_shape,L_shape,Z_shape]
pm = polyomino(figures=figures,area=area)

solution = pm.solve()

print(solution)
#>>> [[0 0 0 5]
#>>>  [1 0 5 5]
#>>>  [1 1 5 4]
#>>>  [1 4 4 4]
#>>>  [3 2 2 2]
#>>>  [3 3 3 2]]