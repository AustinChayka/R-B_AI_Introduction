import search
import chickenWolf
import sys
import studentFuntions

expand = chickenWolf.expand #studentFunctions.expand
h = chickenWolf.h #studentFunctions.h

def main(args):

    global expand
    global h

    if len(args) < 1:
        print("ERROR: not enough arguments.")
        return

    start = [[3, 3, 1], [0, 0, 0]]
    goal = [[0, 0, 0], [3, 3, 1]]

    path = []
    if args[0] == "bfs":
        path = search.bfs(start, goal, expand, draw=True)
    elif args[0] == "dfs" :
        path = search.dfs(start, goal, expand, draw=True)
    elif args[0] == "astar":
        path = search.aStar(start, goal, expand, h, draw=True)

    if path == None:
        print("ERROR: no solution found.")
        return
    
    total_steps = len(path[1]) - 1
    print(str(total_steps) + " steps to goal.")
    print(str(path[0]) + " nodes explored.")
    for line in path[1][::-1]:
        print(line)


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)