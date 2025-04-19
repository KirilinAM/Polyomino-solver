import numpy as np
from polyominator import polyomino

area = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
])

corner = np.array([
    [1,1],
    [1,0],
])
stick = np.array([
    [1,1]
])
ceil = np.array([
    [1]
])

figures = [corner,corner,stick,ceil]
pm = polyomino(figures=figures,area=area)

solution = pm.solve()

print(solution)