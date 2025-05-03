import math
import numpy as np
from maze_2 import Maze

def manhattan(node):
    # WRITE YOUR CODE HERE
    pass

def euclidean(node):
    # WRITE YOUR CODE HERE
    pass

def aStarSearch(start, goal, m, i, epsilon):
    fringe = []
    fringe.append((start + (m.get_distance(start, i), m.get_distance(start, i))))
    closed_list = []
    parent = {}
    paths_poss = {}
    nodes_expanded = 0
    successor = ()
    
    m.visualize_map()
    while fringe:
        m.update_visualization(fringe, closed_list)
        nodes_expanded += 1
        
        all_f_values = [node[3] for node in fringe]
        min_f = min(all_f_values)
        
        current_node = [node for node in fringe if node[3] == min_f][0]
        print(current_node)
        fringe.remove(current_node)
        closed_list.append(current_node[0])
        
        fringe_coordinates = [node[0] for node in fringe]
        successors = m.get_successors(current_node)
        
        for successor1 in successors:
            if successor1[0] not in closed_list:
                if successor1[0] in fringe_coordinates:
                    new_g = successor1[1]
                    print(successor[1])
                    next_successors = m.get_successors(successor1)
                    old_g = 0
                    for suc in next_successors:
                        if suc[0] in closed_list:
                            prev_successor = m.get_successors(suc)
                            old_g = 1 + suc[1]
                            for i in range(old_g):
                                min_g = new_g
                            if i < min_g:
                                min_g = i
                    	     
                    buff = list(successor1)
                    #print(buff)
                    buff[1] = min_g
                    #print(buff)
                    successor1 = tuple(buff)
                 
                buffer_list = list(successor1)
                buffer_list[1] = current_node[1] + 1
                successor = tuple(buffer_list)
                f_value = m.get_distance(successor, i) + successor[1]
                successor_tuple = successor + (m.get_distance(successor, i), f_value)
                fringe.append(successor_tuple)
                closed_list.append(successor[0])
                paths_poss[successor[0]] = current_node[0]	
               
        if current_node[0] == goal:
            break
    
    cell = goal
    if goal not in paths_poss:
        print("Failure to find a path")
        raise KeyError("Failure")
        
    while (cell[0], cell[1]) != tuple(start[0]):
        if paths_poss[cell] == tuple(start[0]):
            parent[paths_poss[cell]] = cell
            
        if (cell[0], cell[1]) == tuple(start[0]):
            paths_poss[start[0]] = (start[0][0] - 1, start[0][1] - 1)
            parent[paths_poss[start]] = start
            
        parent[paths_poss[cell]] = cell
        cell = paths_poss[cell]
    
    return list(parent.values()), nodes_expanded

if __name__ == "__main__":
    m = Maze(map_num=1)  # TOGGLE BETWEEN 1 AND 2 TO TEST IN BOTH ENVIRONMENTS

    m.load_map()

    i = "e"  # Have a look at get_distance function in maze.py
    path, nodes_expanded = aStarSearch(m.get_start_state(), m.get_goal_state(), m, i, epsilon=1)  # Don't worry about epsilon
    print(f"Number of Steps taken by the Robot: {len(path)}")
    print(f"Number of Nodes Expanded: {nodes_expanded}")
    m.keep_plot_open(path)

