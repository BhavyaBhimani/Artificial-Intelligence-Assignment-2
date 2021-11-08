# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 11:17:26 2021

@author: Bhavya
"""

class State:
    def __init__(self, canLeft, missLeft, boat, canRight, missRight, action):
        self.canLeft = canLeft
        self.missLeft = missLeft
        self.boat = boat
        self.canRight = canRight
        self.missRight = missRight
        self.action = action
        self.parent = None

    def check_goal(self):
        if self.canLeft == 0 and self.missLeft == 0:
            return True
        else:
            return False

    def check_valid(self):
        if self.missLeft >= 0 and self.missRight >= 0 \
                and self.canLeft >= 0 and self.canRight >= 0 \
                and (self.missLeft == 0 or self.missLeft >= self.canLeft) \
                and (self.missRight == 0 or self.missRight >= self.canRight):
            return True
        else:
            return False

    def __eq__(self, other):
        return self.canLeft == other.canLeft and self.missLeft == other.missLeft \
               and self.boat == other.boat and self.canRight == other.canRight \
               and self.missRight == other.missRight

    def __hash__(self):
        return hash((self.canLeft, self.missLeft, self.boat, self.canRight, self.missRight))


def successors(cur_state):
    children = []
    if cur_state.boat == 'left':
        # send two missionaries from left to right
        new_state = State(cur_state.canLeft, cur_state.missLeft - 2, 'right',
                          cur_state.canRight, cur_state.missRight + 2,
                          "send two missionaries from left to right")
        if new_state.check_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # send two cannibals from left to right
        new_state = State(cur_state.canLeft - 2, cur_state.missLeft, 'right',
                          cur_state.canRight + 2, cur_state.missRight,
                          "send two cannibals from left to right")
        if new_state.check_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # send one missionary and one cannibal from left to right
        new_state = State(cur_state.canLeft - 1, cur_state.missLeft - 1, 'right',
                          cur_state.canRight + 1, cur_state.missRight + 1,
                          "send one missionary and one cannibal from left to right")
        if new_state.check_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # send one missionary from left to right
        new_state = State(cur_state.canLeft, cur_state.missLeft - 1, 'right',
                          cur_state.canRight, cur_state.missRight + 1,
                          "send one missionary from left to right")
        if new_state.check_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # send one cannibal from left to right
        new_state = State(cur_state.canLeft - 1, cur_state.missLeft, 'right',
                          cur_state.canRight + 1, cur_state.missRight,
                          "send one cannibal from left to right")
        if new_state.check_valid():
            new_state.parent = cur_state
            children.append(new_state)
    else:
        
        # send two missionaries from right to left
        new_state = State(cur_state.canLeft, cur_state.missLeft + 2, 'left',
                          cur_state.canRight, cur_state.missRight - 2,
                          "send two missionaries from right to left")
        if new_state.check_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # send two cannibals from right to left
        new_state = State(cur_state.canLeft + 2, cur_state.missLeft, 'left',
                          cur_state.canRight - 2, cur_state.missRight,
                          "send two cannibals from right to left")
        if new_state.check_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # send one missionary and one cannibal from right to left
        new_state = State(cur_state.canLeft + 1, cur_state.missLeft + 1, 'left',
                          cur_state.canRight - 1, cur_state.missRight - 1,
                          "send one missionary and one cannibal from right to left")
        if new_state.check_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # send one missionary from right to left
        new_state = State(cur_state.canLeft, cur_state.missLeft + 1, 'left',
                          cur_state.canRight, cur_state.missRight - 1,
                          "send one missionary from right to left")
        if new_state.check_valid():
            new_state.parent = cur_state
            children.append(new_state)

        # send one cannibal from right to left
        new_state = State(cur_state.canLeft + 1, cur_state.missLeft, 'left',
                          cur_state.canRight - 1, cur_state.missRight,
                          "send one cannibal from right to left")
        if new_state.check_valid():
            new_state.parent = cur_state
            children.append(new_state)

    return children

def bfs():
    init_state = State(3,3,'left',0,0,"no action yet")
    if init_state.check_goal():
        return init_state 
    front = list()
    explored =  set()
    front.append(init_state)
    while front:
        state = front.pop(0)
        if state.check_goal():
                return state
        explored.add(state)
        children = successors(state)
        for child in children:
            if(child not in explored) or (child not in front):
                front.append(child)
    return None

def dfs() :
    init_state = State(3,3,'left',0,0,"no action yet")
    if init_state.check_goal():
        return init_state 
    front = list()
    explored = set()
    front.append(init_state)
    while front:
        state = front.pop()
        if state.check_goal():
            return state
        explored.add(state)
        children = successors(state)
        for child in children:
            if(child in front) or (child in explored):
                continue
            else:
                front.append(child)
        
    return None


def print_solution(solution):
    path = list()
    path.append(solution)
    parent = solution.parent

    while parent:
        path.append(parent)
        parent = parent.parent

    print("initial state: <3,3,left,0,0>")
    for i in range(1, len(path)):
        state = path[len(path) - i - 1]
        print ("action" + str(i) + ": " + state.action)
        if i == len(path)-1:
            print ("goal state" + str(i) + ": <" + str(state.canLeft) + "," + str(state.missLeft) \
                  + "," + state.boat + "," + str(state.canRight) + "," + \
                  str(state.missRight) + ">")
        else:
            print ("state" + str(i) + ": <" + str(state.canLeft) + "," + str(state.missLeft) \
              + "," + state.boat + "," + str(state.canRight) + "," + \
              str(state.missRight) + ">")


def main():

    print("\n\n\n")
    print("------------------BFS Algorithm------------------\n\n\n")
    solution = bfs()
    print("Format: <cannibal left,missionary left,boat position,cannibal right,missionary right>")
    print_solution(solution)
    print("\n\n\n")
    
    print("------------------DFS Algorithm------------------\n\n\n")
    solution = dfs()
    print("Format: <cannibal left,missionary left,boat position,cannibal right,missionary right>")
    print_solution(solution)


# if called from the command line, call main()
if __name__ == "__main__":
    main()
