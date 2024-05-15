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


def depthFirstSearch(problem):
    # 현재 problem 에서 StartState를 찾아서 저장한다.
    startstate = problem.getStartState()
    # Depth First Search 는 Last In First Out(LIFO) 를 사용하기 때문에 Stack을 사용하면 편리하다.
    fringe = util.Stack()
    # Stack 에 시작 state와 빈 리스트[]를 하나의 item으로 하여 넣는다.
    fringe.push((startstate, []))
    # visited 는 어떠한 state에 도달하기 까지 방문한 state들을 전부 저장해 놓는 리스트이다.
    visited = []
    # Stack 이 비어 있을때 까지 반복문을 돌린다.
    while not fringe.isEmpty():
        # Stack 에서 가장 나중에 넣은 item을 꺼내어 정보를 저장한다.
        node, direction = fringe.pop()
        # node를 방문한 노드 리스트에 저장한다.
        visited.append(node)             
        # node 가 미로의 끝인지를 확인한다.
        if problem.isGoalState(node):
            # 만약 node 가 미로의 끝이 맞다면 start state 부터 여기까지 도달하기 위한 움직임을 return 한다.
            return direction
        # getSuccessors 하는 함수는 successor, action, stepcost 를 반환하는 함수이다.
        # successor 는 다음에 이동할 수 있는 state를 의미한다.
        # action 은 현재 state 에서 다음 state 로 이동하려면 어느 방향으로 이동해야 하는지를 의미한다.
        # stepcost는 다음 state 까지 이동하는 데 소요되는 비용을 의미한다.
        for successor, action, stepcost in problem.getSuccessors(node):
            # 다음 state 가 이전에 방문한 적이 있는지를 검사한다.
            if not successor in visited:
                # 다음 state와 그 state까지 도달하기 위한 움직임을 하나의 item 으로 묶어서 Stack에 넣는다.
                fringe.push((successor, direction + [action]))
    # 만약 Stack이 비었는데 return을 하지 않았다면 미로를 끝낼수 있는 방법이 없는 것 이므로 빈 리스트를 return 한다. 
    return []
