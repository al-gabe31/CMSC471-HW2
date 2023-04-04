from collections import deque # Needed for Stacks and Queues
from queue import PriorityQueue # Needed for Priority Queue

X_CAPACITY = 3 # Capacity of the first water jug
Y_CAPACITY = 1 # Capacity of the second water jug

class waterState:
    def __init__(self, x = X_CAPACITY, y = Y_CAPACITY, prevState = None):
        # Validates constructor inputs
        # x in [0, 3] and y in [0, 1]
        if x in range(0, X_CAPACITY + 1) and y in range(0, Y_CAPACITY + 1):
            self.x = x
            self.y = y
        # Otherwise, set x to 3 and y to 1
        else:
            self.x = X_CAPACITY
            self.y = Y_CAPACITY
        
        self.prevState = prevState
    
    def get_heuristic(otherState):
        return abs(otherState.x - 1) + abs(otherState.y - 1)
    
    # The following 4 methods returns the resulting state based on a given action
    # Pours out the 3 gallon jug to the floor (emptying it)
    def pour_out_x(self):
        return waterState(0, self.y, self)
    
    # Pours out the 1 gallon jug to the floor (emptying it)
    def pour_out_y(self):
        return waterState(self.x, 0, self)
    
    # Pours the 3 gallon jug to the 1 gallon jug
    def pour_x_to_y(self):
        num_poured = min(self.x, Y_CAPACITY - self.y)
        return waterState(self.x - num_poured, min(Y_CAPACITY, self.x + self.y), self)
    
    # Pours the 1 gallon jug to the 3 gallon jug
    def pour_y_to_x(self):
        num_poured = min(X_CAPACITY - self.x, self.y)
        return waterState(min(X_CAPACITY, self.x + self.y), self.y - num_poured, self)
    
    # Performs all 4 possible actions
    # Returns a tuple
    def perform_all(self):
        return (self.pour_out_x(), self.pour_out_y(), self.pour_x_to_y(), self.pour_y_to_x())
    
    # Returns True if the current state matches the goal state
    def is_goal_state(self):
        return self.x == 1 and self.y == 1
    
    # To string method
    def __str__(self):
        return f"[{self.x}, {self.y}]"
    
    # String representation of the state
    def string_repr(self):
        return f"{self.x}:{self.y}"
    
    # Makes waterState objects comparable to each other using the getHeuristic method
    def __lt__(self, otherState):
        return waterState.get_heuristic(self) < waterState.get_heuristic(otherState)
    
    def __eq__(self, otherState):
        return waterState.get_heuristic(self) == waterState.get_heuristic(otherState)

class WaterPouringSolution:
    # Performs a breadth-first solution on the problem
    # Returns a tuple where index:
    #   - 0: End state
    #   - 1: Cost of solution
    @staticmethod
    def breadth_first():
        visited_string = []
        visited = []
        frontier = deque() # Will be a Queue data structure

        frontier.append(waterState(3, 1))
        curr_state = frontier[0]

        iters = 0 # Will also act as the cost
        max_iters = 1000

        # Keeps finding a solution until:
        #   - Frontier is empty (solution isn't possible)
        #   - Goal state found (heuristic value = 0)
        while len(frontier) > 0 and curr_state.get_heuristic() != 0 and iters < max_iters:
            # Adds current state to the visited list (if it hasn't been visited yet)
            if curr_state.string_repr() not in visited_string:
                visited_string.append(curr_state.string_repr())
                visited.append(curr_state)
            
            # Adds new states to the frontier based on all possible actions
            for state in curr_state.perform_all():
                if state.string_repr() not in visited_string:
                    frontier.append(state)
                
                # frontier.append(state)
            
            # Gets state from the left of the Queue
            curr_state = frontier.popleft()

            iters += 1

        # Obtain the solution path
        solution_path = [curr_state]
        while(solution_path[-1].prevState):
            solution_path.append(solution_path[-1].prevState)
        solution_path.reverse()
        
        return (solution_path, iters)