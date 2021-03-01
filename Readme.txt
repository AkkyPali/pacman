Name: Akanksha Paliwal
SFSU ID: 921427283




Q1. Finding a Fixed Food Dot using Depth First Search


Implemented DFS using stack from util. Used “(coord, path_to_coord)” tuple as the node placed in the stack in the DFS. “path_to_node” is used to return the path once it has reached the goal. 




Q2. BFS


Implemented BFS using queue from util by using “(coord, path_to_coord)” tuple as the node placed in the queue similar to DFS.


Q3. UCS


Implemented UCS using priority queue from util in a similar way to BFS. Here in addition to “(coord, path_to_coord)”, also added “cost_to_coord” to the node placed in the queue. “cost_to_coord” of used as the priority for the node in the queue. “cost_to_coord” of successors is computed using “cost_to_coord” + cost of action from parent coord to successor.


Q4. A*


Implemented A* using priority queue from util in a similar way to BFS and UCS. The node used in PriorityQueue is still “(coord, path_to_coord, cost_to_coord)” which is the same as UCS. The only change from UCS is to used “cost_to_coord + heuristic(coord)“ as the priority in the priority_queue.


Q5. Finding Corners - Problem


Designed the successor state in CornersProblem to contain “(coord, list_of_visited_corners)”. The “list_of_visited_corners” is initialized to “[]”. During expansion, if a successor is a corner (not part of already visited), it is added to the “visited_corners_list” for that particular successor. “isGoalState” returns true “visited_corners_list” of the state contains all 4 corners.


Q6. Finding Corners - Heuristics


Tried multiple heuristics -
* Tried the sum of manhattan distance of all unvisited corners from the current coord as the heuristic. This was inadmissible, probably because it was not bound by the actual lowest distance of the path.
* Used the distance of the furthest manhattan distance as the heuristic, as this was certain to be bound to be lesser than the shortest path. This gave a score of ⅔ as this expanded 1357 nodes.
* Defined the heuristic as manhattan distance to visit all nodes, starting from the nearest corner first, and then visiting the closest corner from that corner and so on. This gave a score 3/3 as it explored only 901 nodes.


Q7. Eating All The Dots - Heuristics


Tried multiple heuristics -
* Tried the distance of nearest food as the heuristic. This gave the score of 2/4 as it expanded 12372 nodes. Here, BFS is used to compute the distance data b/w point and various food items. Also, “problem.heuristicInfo” was used to cache distance data (keyed by (from, to) coordinate tuple), since a lot of distances need to be computed multiple times.
* Could not improve on this heuristic for a while. Searched online for ideas to improve this heuristic. Found a useful suggestion from here - https://rshcaroline.github.io/research/resources/pacman-report.pdf. This improved heuristic by adding maximum distance among all the remaining food items. This improved heuristic brought down the expanded node count to 719. The idea for the improved heuristic was taken from the mentioned link, the code was implemented independently.


Q8. Suboptimal Search


For finding the closest food dot, we just need to do a BFS, and stop once we have reached a food item. For this, we simply call a BFS (implemented in Q2) and apply it to AnyFoodSearchProblem. AnyFoodSearchProblem is implemented to return true on isGoalState as soon as the current state has reached any of the foodItem.




Time taken Spent about a total of 15 hours in two weeks. 
Stated with reading up about the algorithm, pseudo-codes, and suggested text readings. Started with translating from pseudo-codes for the first 4 questions which took about 4-5 hours. It took about 2 hours on Implementing Corner Search Problem (Q5) and trying out simple heuristics for Corner Search Problem (Q6). Coming up with the optimum heuristic for the Corner Search Problem (Q6) took about an hour and additional 4 hours in trying multiple heuristic for Eating All Dots. Searching online and trying that heuristic which gave an optimal solution. And lastly about 1/2 hour on Suboptimal Search.