import graph

def bfs(start, goal, expand, draw=False):
    edges = []
    node_ctr = 0
    frontier = [(start, 0, 0)]
    explored = []
    path = []
    count = 0
    while True:
        if len(frontier) == 0:
            break
        leaf = frontier.pop(len(frontier) - 1)
        if(len(path) <= leaf[1]):
            path.append(leaf[0])
        else:
            path[leaf[1]] = leaf[0]
        if leaf[0] == goal:
            if draw:
                graph.drawTree(range(node_ctr+1), edges)
            path.reverse()
            return (count, path)
        explored.append(leaf[0])
        count += 1
        nextNodes = expand(leaf[0])
        for node in nextNodes:
            if not node in explored and not node in map(lambda a : a[0], frontier):
                frontier.insert(0, (node, leaf[1] + 1, node_ctr + 1))
                edges.append((leaf[2], node_ctr + 1))
                node_ctr += 1
    return None

def dfs(start, goal, expand, draw=False):
    edges = []
    node_ctr = 0
    frontier = [(start, 0, 0)]
    explored = []
    path = []
    count = 0
    while True:
        if len(frontier) == 0:
            break
        leaf = frontier.pop(len(frontier) - 1)
        if(len(path) <= leaf[1]):
            path.append(leaf[0])
        else:
            path[leaf[1]] = leaf[0]
        if leaf[0] == goal:
            if draw:
                graph.drawTree(range(node_ctr+1), edges)
            path.reverse()
            return (count, path)
        explored.append(leaf[0])
        count += 1
        nextNodes = expand(leaf[0])
        for node in nextNodes:
            if not node in explored and not node in map(lambda a : a[0], frontier):
                frontier.append((node, leaf[1] + 1, node_ctr + 1))
                edges.append((leaf[2], node_ctr + 1))
                node_ctr += 1
    return None

def aStar(start, goal, expand, h, draw=False):
    edges = []
    node_ctr = 0
    frontier = [(start, 0, 0, 0)]
    explored = []
    path = []
    count = 0
    while True:
        if len(frontier) == 0:
            break
        leaf = frontier.pop(len(frontier) - 1)
        if(len(path) <= leaf[1]):
            path.append(leaf[0])
        else:
            path[leaf[1]] = leaf[0]
        if leaf[0] == goal:
            if draw:
                graph.drawTree(range(node_ctr+1), edges)
            path.reverse()
            return (count, path)
        explored.append(leaf[0])
        count += 1
        nextNodes = expand(leaf[0])
        for node in nextNodes:
            if not node in explored and not node in map(lambda a : a[0], frontier):
                frontier.append((node, leaf[1] + 1, leaf[1] + 1 + h(leaf[0]), node_ctr + 1))
                frontier.sort(key = lambda a : a[2])
                edges.append((leaf[3], node_ctr + 1))
                node_ctr += 1
    return None