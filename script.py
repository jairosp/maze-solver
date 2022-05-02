from maze import Maze

if __name__ == '__main__':
    wall = ((0,1), (0,3), (0,4), (1,1), (2,1), (1,3), (3,3), (4,0), (4,1), (4,2), (4,3)) # Walls coordinates' tuple
    dimension = (5,5) # Rows, columns
    start = (0,0) # Note that Python coordinates start in (0,0) so for a mxn dimensional maze the (m,n) wont be valid
    ending = (4,4)
    my_maze = Maze(dimension, wall, start=start, ending=ending)
    my_maze.show()
    my_maze.solve()
