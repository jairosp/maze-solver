# Maze solver!
In order to solve a maze, fill the script file with the maze data as follows:
- Fill the maze tuple with all the wall coordinates.
- Set the maze dimension in the variable dimension.
- Optional: Set the start and ending coordinate of your maze, by default it starts in (0,0) and ends in (m-1,n-1) for mxn dimensional maze.
```python
start = (4,4) # Note that Python coordinates start in (0,0) so for a mxn dimensional maze the (m,n) wont be valid
ending = (0,0)
wall = ((0,1), (0,3), (0,4), (1,1), (2,1), (1,3), (3,3), (4,0), (4,1), (4,2), (4,3))
dimension = (5,5)
```
Then execute the file script.py and it will show you the solution. 