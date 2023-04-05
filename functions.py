from collections import deque # Needed for Stacks and Queues
from queue import PriorityQueue # Needed for Priority Queue

X_CAPACITY = 3  # Capacity of the first water jug
Y_CAPACITY = 1 # Capacity of the second water jug

X_START = 3     # Start value of the first jug
Y_START = 1     # Start value of the second jug

X_GOAL = 1      # End value of the first jug
Y_GOAL = 1      # End value of the second jug

# Code for Question 3
class waterState:
    def __init__(self, x = X_CAPACITY, y = Y_CAPACITY, prev_state = None, path_cost = 0):
        # Validates constructor inputs
        # x in [0, 3] and y in [0, 1]
        if x in range(0, X_CAPACITY + 1) and y in range(0, Y_CAPACITY + 1):
            self.x = x
            self.y = y
        # Otherwise, set x to 3 and y to 1
        else:
            self.x = X_CAPACITY
            self.y = Y_CAPACITY
        
        self.prev_state = prev_state
        self.path_cost = path_cost
    
    def get_heuristic(otherState):
        return abs(otherState.x - X_GOAL) + abs(otherState.y - Y_GOAL)
    
    # The following 4 methods returns the resulting state based on a given action
    # Pours out the 3 gallon jug to the floor (emptying it)
    def pour_out_x(self):
        return waterState(0, self.y, self, self.path_cost + 1)
    
    # Pours out the 1 gallon jug to the floor (emptying it)
    def pour_out_y(self):
        return waterState(self.x, 0, self, self.path_cost + 1)
    
    # Pours the 3 gallon jug to the 1 gallon jug
    def pour_x_to_y(self):
        num_poured = min(self.x, Y_CAPACITY - self.y)
        return waterState(self.x - num_poured, min(Y_CAPACITY, self.x + self.y), self, self.path_cost + 1)
    
    # Pours the 1 gallon jug to the 3 gallon jug
    def pour_y_to_x(self):
        num_poured = min(X_CAPACITY - self.x, self.y)
        return waterState(min(X_CAPACITY, self.x + self.y), self.y - num_poured, self, self.path_cost + 1)
    
    # Performs all 4 possible actions
    # Returns a tuple
    def perform_all(self):
        # The order of which action to perform DOES affect the runtime cost of each algorithm
        # Just pick an order here
        
        # Order 1
        return (self.pour_out_x(), self.pour_out_y(), self.pour_x_to_y(), self.pour_y_to_x())

        # Order 2
        # return (self.pour_x_to_y(), self.pour_out_y(), self.pour_y_to_x(), self.pour_out_x())
    
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

        frontier.append(waterState(X_START, Y_START))
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

        # Case 1: Solution Found
        if curr_state.get_heuristic() == 0:
            # Obtain the solution path
            solution_path = [curr_state]
            while(solution_path[-1].prev_state):
                solution_path.append(solution_path[-1].prev_state)
            solution_path.reverse()
            
            return (solution_path, iters)
        # Case 2: Solution Not Found
        else:
            print("SOLUTION NOT FOUND")
            return -1 # Return error code
    
    # Performs a depth-first solution on the problem
    # Returns a tuple where index:
    #   - 0: End state
    #   - 1: Cost of solution
    @staticmethod
    def depth_first():
        visited_string = []
        visited = []
        frontier = deque() # Will be a Queue data structure

        frontier.append(waterState(X_START, Y_START))
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
            curr_state = frontier.pop()

            iters += 1

        # Case 1: Solution Found
        if curr_state.get_heuristic() == 0:
            # Obtain the solution path
            solution_path = [curr_state]
            while(solution_path[-1].prev_state):
                solution_path.append(solution_path[-1].prev_state)
            solution_path.reverse()
            
            return (solution_path, iters)
        # Case 2: Solution Not Found
        else:
            print("SOLUTION NOT FOUND")
            return -1 # Return error code
    
    # Performs a greedy best-first search using h
    # Returns a tuple where index:
    #   - 0: End state
    #   - 1: Cost of solution
    @staticmethod
    def best_first():
        visited_string = []
        visited = []
        frontier = PriorityQueue() # Will be a Priority Queue data structure

        curr_state = waterState(X_START, Y_START)
        frontier.put(curr_state)

        iters = 0 # Will also act as the cost
        max_iters = 1000

        # Keeps finding a solution until:
        #   - Frontier is empty (solution isn't possible)
        #   - Goal state found (heuristic value = 0)
        while frontier.qsize() > 0 and curr_state.get_heuristic() != 0 and iters < max_iters:
            # Adds current state to the visited list (if it hasn't been visited yet)
            if curr_state.string_repr() not in visited_string:
                visited_string.append(curr_state.string_repr())
                visited.append(curr_state)
            
            # Adds new states to the frontier based on all possible actions
            for state in curr_state.perform_all():
                if state.string_repr() not in visited_string:
                    frontier.put(state)
                
                # frontier.append(state)
            
            # Gets state from the Priority Queue
            curr_state = frontier.get()

            iters += 1

        # Case 1: Solution Found
        if curr_state.get_heuristic() == 0:
            # Obtain the solution path
            solution_path = [curr_state]
            while(solution_path[-1].prev_state):
                solution_path.append(solution_path[-1].prev_state)
            solution_path.reverse()
            
            return (solution_path, iters)
        # Case 2: Solution Not Found
        else:
            print("SOLUTION NOT FOUND")
            return -1 # Return error code
    
    # Performs a greedy best-first search using h
    # Returns a tuple where index:
    #   - 0: End state
    #   - 1: Cost of solution
    @staticmethod
    def a_search():
        visited_string = []
        visited = []
        frontier = PriorityQueue() # Will be a Priority Queue data structure

        curr_state = waterState(X_START, Y_START)
        frontier.put((curr_state.get_heuristic() + curr_state.path_cost, curr_state))

        iters = 0 # Will also act as the cost
        max_iters = 1000

        # Keeps finding a solution until:
        #   - Frontier is empty (solution isn't possible)
        #   - Goal state found (heuristic value = 0)
        while frontier.qsize() > 0 and curr_state.get_heuristic() != 0 and iters < max_iters:
            # Gets state from the Priority Queue
            curr_state = (frontier.get()[1])
            
            # Adds current state to the visited list (if it hasn't been visited yet)
            if curr_state.string_repr() not in visited_string:
                visited_string.append(curr_state.string_repr())
                visited.append(curr_state)
            
            # Adds new states to the frontier based on all possible actions
            for state in curr_state.perform_all():
                if state.string_repr() not in visited_string:
                    # frontier.put(state)
                    frontier.put((state.get_heuristic() + state.path_cost, state))
                
                # frontier.append(state)
            
            iters += 1

        # Case 1: Solution Found
        if curr_state.get_heuristic() == 0:
            # Obtain the solution path
            solution_path = [curr_state]
            while(solution_path[-1].prev_state):
                solution_path.append(solution_path[-1].prev_state)
            solution_path.reverse()
            
            return (solution_path, iters)
        # Case 2: Solution Not Found
        else:
            print("SOLUTION NOT FOUND")
            return -1 # Return error code

# Code for Question 4
# RESUME
class eightPuzzleState:
    def __init__(self, grid, prev_state = None, path_cost = 0):
        pass