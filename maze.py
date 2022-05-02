class Maze():
    def __init__(self, dimension, wall, start=(0,0), ending=None):
        self.dimension = dimension
        self.wall = wall
        self.start = start
        self.ending = ending
        self.array = self.array()

    def array(self):
        maze = list() # We create the maze as a list of lists, making a 2-Dimensional array

        for i in range(self.dimension[0]):
            row = list()
            
            for j in range(self.dimension[1]):

                verification = 0 # Verifies whether (i,j) coordinate is a wall
                for element in self.wall:
                        
                        if (i,j) == element:
                            verification += 1
                        


                if verification == 1:
                    
                    row.append('X')

                else:
                    row.append(' ')
                
            maze.append(row)

        
        return maze

    def show(self):
        print(40*"=")
        print("\n\tMaze's Map\n")
        for row in self.array:
            print("\t",row)
        print("\n",40*"=", 2*"\n")
        
    def solve(self):
        current_coordinate = self.start
        if self.ending:
            goal_coordinate = (self.ending)
        else:
            goal_coordinate = (self.dimension[0] - 1, self.dimension[1] - 1) # The goal coordinate will be lower right corner as default

        if current_coordinate == goal_coordinate:
            raise NameError("Starting point cannot be the same as the ending!")

        way_traveled = [current_coordinate] # Already traveled squares' array

        instructions = []
        checkpoints = [] # This array stores the checkpoints (points where we might return later)

        def give_instructions(first_square, second_square):
            if first_square[0] == second_square[0]:
                if first_square[1] + 1 == second_square[1]:
                    return "Right"
                if first_square[1] - 1 == second_square[1]:
                    return "Left"
            elif first_square[1] == first_square[1]:
                if first_square[0] + 1 == second_square[0]:
                    return "Down"
                if first_square[0] - 1 == second_square[0]:
                    return "Up"
            else:
                raise NameError("Movement error, squares are not adjoining")


        while current_coordinate != goal_coordinate:
            # We check what are the squares around
            around = []
            

            for i in (current_coordinate[0] - 1, current_coordinate[0], current_coordinate[0] + 1):
                for j in (current_coordinate[1] - 1, current_coordinate[1], current_coordinate[1] + 1):

                    inside_the_maze = i>=0 and j>= 0 and i<self.dimension[0] and j<self.dimension[1]
                    not_in_diagonal = (current_coordinate[0] + current_coordinate[1]) % 2 != (i+j)%2 # When the coordinate sum parity is different between two coordinates, we claim they are not in diagonal
                    not_the_same_square = (i,j) != (current_coordinate[0],current_coordinate[1])

                    if inside_the_maze and not_the_same_square and not_in_diagonal:
                        around.append((i,j))

            # Count possible squares around

            free_squares = []
            for casilla in around:

                casilla_libre = self.array[casilla[0]][casilla[1]] != 'X'

                if (casilla not in way_traveled) and casilla_libre:
                    free_squares.append(casilla)

            # Depending on the number of avaible squares, we act in a different way

            # In case there's only one, we simply advance
            if len(free_squares) == 1:
                instructions.append(give_instructions(current_coordinate,free_squares[0]))
                current_coordinate = free_squares[0]
                way_traveled.append(current_coordinate)

            # In case there are several options, we choose any and save the checkpoint in case we need to return later
            elif len(free_squares) > 1:

                checkpoints.append((current_coordinate, len(instructions)))
                instructions.append(give_instructions(current_coordinate,free_squares[0]))

                current_coordinate = free_squares[0]
                way_traveled.append(current_coordinate)

            # In case there's no option we return to the latter checkpoint (when possible)
            elif len(free_squares) == 0:
                try:
    
                    last_checkpoint_data = checkpoints.pop()
                    current_coordinate = last_checkpoint_data[0] # Returns to the latter checkpoint
                    last_checkpoint_list_len = last_checkpoint_data[1]
                    while len(instructions) > last_checkpoint_list_len:
                        instructions.pop()

                except:
                    raise Exception("No exit maze")

        print("Maze solved succesfully!")
        print(instructions)