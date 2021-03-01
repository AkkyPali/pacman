# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    #initialisation for DFS
    visited = set()
    stack = util.Stack()
    start_state = problem.getStartState()
    stack.push((start_state, []))

    #running loop on nodes in the stack
    while not stack.isEmpty():
        node, path = stack.pop()
        visited.add(node)
        # print("Popped:", node)
        if problem.isGoalState(node):
            return path
        else:
            successors = problem.getSuccessors(node)
            for successor, action, _ in successors:
                if successor not in visited:
                    # print("Pushing:", successor, "with action:", action)
                    successor_path = path.copy()
                    successor_path.append(action)
                    stack.push((successor, successor_path))
    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    #Initialising for BFS
    visited = set()
    stack = util.Queue()
    start_state = problem.getStartState()
    visited.add(start_state)
    stack.push((start_state, []))

    #running loop on nodes in the stack
    while not stack.isEmpty():
        node, path = stack.pop()
        # print("Popped:", node)
        if problem.isGoalState(node):
            return path
        else:
            successors = problem.getSuccessors(node) 
            for successor, action, _ in successors:
                if successor not in visited:
                    visited.add(successor)
                    # print("Pushing:", successor, "with action:", action)
                    successor_path = path.copy()
                    successor_path.append(action)
                    stack.push((successor, successor_path))
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
   
   #Initialising for UCS
    visited = set()         
    pq = util.PriorityQueue()
    start_state = problem.getStartState()
    pq.push((start_state, [], 0), 0) # ((pushing a tuple with state, path travelled, cost of path), priority)

    #running loop on nodes in the stack
    while not pq.isEmpty():
        node, path, cost = pq.pop()
        # print("Popped:", node)
        if node not in visited:
            visited.add(node)
            if problem.isGoalState(node):
                return path
            else:
                successors = problem.getSuccessors(node)
                for successor, action, successor_cost in successors:
                        # print("Pushing:", successor, "with action:", action)
                        #create a copy of path travelled to update the priority queue
                        successor_path = path.copy()
                        successor_path.append(action)
                        #update the frontier node with successor nodes, path travelled, cost of path 
                        pq.push((successor, successor_path, cost + successor_cost), cost + successor_cost)
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    #Initialising A* search
    visited = set()
    pq = util.PriorityQueue()
    start_state = problem.getStartState()
    pq.push((start_state,[],0),0)

    #running loop on nodes in the stack
    while not pq.isEmpty():
        node, path, cost = pq.pop()
        # print("Popped:", node)
        if node not in visited:
            visited.add(node)
            if problem.isGoalState(node):
                return path
            else:
                successors = problem.getSuccessors(node)
                for successor, action, successor_cost in successors:
                        # print("Pushing:", successor, "with action:", action)
                        #create a copy of path travelled to update the priority queue
                        successor_path = path.copy()
                        successor_path.append(action)
                        #update the frontier node with successor nodes, path travelled, cost of path 
                        pq.push((successor, successor_path, cost + successor_cost), cost + successor_cost + heuristic(successor, problem))
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
