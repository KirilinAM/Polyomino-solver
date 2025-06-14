# Polyomino-solver
Solving the problem of accurately paving polyominoes with a given set of shapes. 
The program translates the polymino problem into the language of the X-algorithm. The `algorithm-x` library is used to solve Algorithm X.

## Training manual
In general, using the package looks like this:
1. Connect the package and numpy
```python
import numpy as np
from polyominator import polyomino
```

2. Set the field as an array, where 1 is a cell for paving, 0 is not for paving (like a Boolean array). For example, a 3x3 square field will look like this:
```python
area = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
])
```

3. Set the shapes as arrays, where 1 is the element of the shape, 0 is the free space (again a Boolean array). For example, here is a 3-segment corner, a 2-segment stick, and a single segment, respectively:
```python
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
```
> Please note that there is no fixed size of the array for the shapes. The main thing is that the shape fits into the array.

4. Pass the field and the list of shapes to the `polyomino' class.
```python
figures = [corner,corner,stick,ceil]
pm = polyomino(figures=figures,area=area)
```

5. Get a single solution (with the argument `get_only_one_solve = True`) or a generator of all solutions (`get_only_one_solve = False`) using the `solve` method. 
> By default, `get_only_one_solve = True`.
```python
solution = pm.solve()
#solutions_generator = pm.solve(False)

>>> [[0 0 2]
>>>  [0 1 2]
>>>  [3 1 1]]
```

### What does the solution look like
The solution that (or which) the program will return to you, they look like an array with the same dimension as the field, and filled with numbers. If it seems to you that these numbers form shapes, it doesn't seem to you. When transferring figures to a class, they are numbered in the order of transfer (from 0). In this case:
- 0: corner,
- 1: corner,
- 2: stick,
- 3: ceil.

And these numbers form the silhouette of the figure in the place of the field in which this figure should be inserted.

## Example
The field and the shapes for paving are given:

![Paving field](https://raw.githubusercontent.com/KirilinAM/Polyomino-solver/main/img/empty_area.png) 

![Paving shapes](https://raw.githubusercontent.com/KirilinAM/Polyomino-solver/main/img/figures_with_num.png)

Then the search for the correct paving is presented in the file `examples\example from readme.py `. The solution looks like this:
```python
>>> [[0 0 0 5]
>>>  [1 0 5 5]
>>>  [1 1 5 4]
>>>  [1 4 4 4]
>>>  [3 2 2 2]
>>>  [3 3 3 2]]
```
That is, the final arrangement of the shapes is:

![Paved field](https://raw.githubusercontent.com/KirilinAM/Polyomino-solver/main/img/figured_area_with_num.png)


## Notes
- Theoretically, holes and protrusions in the fields are allowed, but they have not been tested for operability. For example:
```python
example_area = [
    [1,1,1,0],
    [1,0,1,1],
    [1,1,1,0]
]
```
- There is an 'is_rotate` flag in the class. In theory, it regulates whether the pieces can rotate. By default, rotates are allowed, but I have not tested how the program behaves when it is forbidden.

## Thanks
Thanks to the Talos Principle and its beautiful puzzles, in particular the last yellow one, for inspiring the development. I sent rays of goodness to Elohim and Milton, may they be healthy forever and ever.
