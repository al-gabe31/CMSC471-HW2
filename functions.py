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
    
    @staticmethod
    def get_heuristic(otherState):
        return abs(otherState.x - 1) + abs(otherState.y - 1)
    
    # The following 4 methods returns the resulting state based on a given action
    # Pours out the 3 gallon jug to the floor (emptying it)
    @staticmethod
    def pour_out_x(otherState):
        return waterState(0, otherState.y, otherState)
    
    # Pours out the 1 gallon jug to the floor (emptying it)
    @staticmethod
    def pour_out_y(otherState):
        return waterState(otherState.x, 0, otherState)
    
    # Pours the 3 gallon jug to the 1 gallon jug
    @staticmethod
    def pour_x_to_y(otherState):
        return waterState(0, min(Y_CAPACITY, otherState.x + otherState.y), otherState)
    
    # Pours the 1 gallon jug to the 3 gallon jug
    @staticmethod
    def pour_y_to_x(otherState):
        return waterState(min(X_CAPACITY, otherState.x + otherState.y), 0, otherState)
    
    # Performs all 4 possible actions
    # Returns a tuple
    @staticmethod
    def perform_all(otherState):
        return (waterState.pour_out_x(otherState), waterState.pour_out_y(otherState), waterState.pour_x_to_y(otherState), waterState.pour_y_to_x(otherState))
    
    # Returns True if the current state matches the goal state
    @staticmethod
    def is_goal_state(otherState):
        return otherState.x == 1 and otherState.y == 1
    
    # To string method
    def __str__(self):
        return f"X = {self.x} & Y = {self.y}"
    
    # Makes waterState objects comparable to each other using the getHeuristic method
    def __lt__(self, otherState):
        return waterState.get_heuristic(self) < waterState.get_heuristic(otherState)
    
    def __eq__(self, otherState):
        return waterState.get_heuristic(self) == waterState.get_heuristic(otherState)

class WaterPouringSolution:
    @staticmethod
    def greeting():
        print("Hi there!")