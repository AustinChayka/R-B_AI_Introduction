import graph

#bredth-first search
def bfs(start, goal, expand, draw=False):
    #setup variables
    #edge and node_ctr are used only for graphing
    edges = []
    node_ctr = 0
    #frontier = list of next states to look at
    frontier = [(start, 0, 0)]
    #explored = list of visited states
    explored = []
    #path = path taken to goal
    path = []
    #count = number of nodes visited
    count = 0
    while True:
        #check if there are more nodes to look at
        if len(frontier) == 0:
            break
        #take the next node from the frontier
        #for bfs this is done in fist-in-first-out order
        #leaf = [state, depth, node count]
        leaf = frontier.pop(len(frontier) - 1)
        #if the current node is further along, append the state, otherwise set respective path position ot the state
        if(len(path) <= leaf[1]):
            path.append(leaf[0])
        else:
            path[leaf[1]] = leaf[0]
        #check if we reached the goal, if so return
        if leaf[0] == goal:
            if draw:
                graph.drawTree(range(node_ctr+1), edges)
            path.reverse()
            return (count, path)
        #add current state to the explored list
        explored.append(leaf[0])
        #increment visited nodes counter
        count += 1
        #get the next possible states
        nextNodes = expand(leaf[0])
        #look at next states, add ones that haven't been seen before to the front of the frontier list
        for node in nextNodes:
            if not node in explored and not node in map(lambda a : a[0], frontier):
                frontier.insert(0, (node, leaf[1] + 1, node_ctr + 1))
                edges.append((leaf[2], node_ctr + 1))
                node_ctr += 1
    return None

#depth-first search
def dfs(start, goal, expand, draw=False):
    #setup variables
    #edge and node_ctr are used only for graphing
    edges = []
    node_ctr = 0
    #frontier = list of next states to look at
    frontier = [(start, 0, 0)]
    #explored = list of visited states
    explored = []
    #path = path taken to goal
    path = []
    #count = number of nodes visited
    count = 0
    while True:
        #check if there are more nodes to look at
        if len(frontier) == 0:
            break
        #take the next node from the frontier
        #for dfs this is done in fist-in-last-out order
        #leaf = [state, depth, node count]
        leaf = frontier.pop(len(frontier) - 1)
        #if the current node is further along, append the state, otherwise set respective path position ot the state
        if(len(path) <= leaf[1]):
            path.append(leaf[0])
        else:
            path[leaf[1]] = leaf[0]
        #check if we reached the goal, if so return
        if leaf[0] == goal:
            if draw:
                graph.drawTree(range(node_ctr+1), edges)
            path.reverse()
            return (count, path)
        #add current state to the explored list
        explored.append(leaf[0])
        #increment visited nodes counter
        count += 1
        #get the next possible states
        nextNodes = expand(leaf[0])
        #look at next states, add ones that haven't been seen before to the back of the frontier list
        for node in nextNodes:
            if not node in explored and not node in map(lambda a : a[0], frontier):
                frontier.append((node, leaf[1] + 1, node_ctr + 1))
                edges.append((leaf[2], node_ctr + 1))
                node_ctr += 1
    return None

#a-star search, based on the h() evaluation function
def aStar(start, goal, expand, h, draw=False):
   #setup variables
    #edge and node_ctr are used only for graphing
    edges = []
    node_ctr = 0
    #frontier = list of next states to look at
    frontier = [(start, 0, 0, 0)]
    #explored = list of visited states
    explored = []
    #path = path taken to goal
    path = []
    #count = number of nodes visited
    count = 0
    while True:
        #check if there are more nodes to look at
        if len(frontier) == 0:
            break
        #take the next node from the frontier
        #for a-star this is done in order of priority based on the evaluation function
        #leaf = [state, depth, node count]
        leaf = frontier.pop(len(frontier) - 1)
        #if the current node is further along, append the state, otherwise set respective path position ot the state
        if(len(path) <= leaf[1]):
            path.append(leaf[0])
        else:
            path[leaf[1]] = leaf[0]
        #check if we reached the goal, if so return
        if leaf[0] == goal:
            if draw:
                graph.drawTree(range(node_ctr+1), edges)
            path.reverse()
            return (count, path)
        #add current state to the explored list
        explored.append(leaf[0])
        #increment visited nodes counter
        count += 1
        #get the next possible states
        nextNodes = expand(leaf[0])
        #look at next states, add ones that haven't been seen before to the frontier list
        for node in nextNodes:
            if not node in explored and not node in map(lambda a : a[0], frontier):
                frontier.append((node, leaf[1] + 1, leaf[1] + 1 + h(leaf[0], goal), node_ctr + 1))
                #sort frontier based on evaluation score
                frontier.sort(key = lambda a : a[2])
                edges.append((leaf[3], node_ctr + 1))
                node_ctr += 1
    return None