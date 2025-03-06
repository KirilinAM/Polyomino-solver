import numpy as np
from polyominator import polyomino

area = np.ones((5,8))

figures = [
    np.array([
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
        [1,1,1]
        ,[1,0,0]
    ])
    ,np.array([
        [1,0,0]
        ,[1,1,1]
    ])
    ,np.array([
        [0,1,1]
        ,[1,1,0]
    ])
    ,np.array([
        [0,1,1]
        ,[1,1,0]
    ])
    ,np.array([
        [1,1,0]
        ,[0,1,1]
    ])
    ,np.array([
        [1,1,0]
        ,[0,1,1]
    ])
]


pm = polyomino(figures,area)
solutions = pm.solve()
print(solutions[0])