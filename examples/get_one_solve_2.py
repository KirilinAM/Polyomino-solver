import numpy as np
from polyominator import polyomino

area = np.ones((10,4))

figures = [
    np.array([
         [0,1,1]
        ,[1,1,0]
    ])
    ,np.array([
         [1,1,1]
        ,[0,1,0]
    ])
    ,np.array([
         [1,1,1]
        ,[0,1,0]
    ])
    ,np.array([
         [1,1,1]
        ,[0,1,0]
    ])
    ,np.array([
         [1,1,1]
        ,[0,1,0]
    ])
    ,np.array([
        [1,1]
        ,[1,1]
    ])
    ,np.array([
        [1,1]
        ,[1,1]
    ])
    ,np.array([
        [1,1,1,1]
    ])
    ,np.array([
        [1,1,1]
        ,[1,0,0]
    ])
    ,np.array([
        [1,1,1]
        ,[1,0,0]
    ])
]


pm = polyomino(figures,area)
solutions = pm.solve()
print(solutions)