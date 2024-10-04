import search
import chickenWolf
import sys
import studentFuntions

#choose wether to use the student-written functions or the included example functions
expand = chickenWolf.expand #studentFunctions.expand
h = chickenWolf.h #studentFunctions.h

def main(args):

    global expand
    global h

    #check arguments 
    if len(args) < 1:
        print("ERROR: not enough arguments.")
        return

    #setup start and goal structures, format: [[chichens right, wolves right, boat right], [chickens left, wolves left, boat left]]
    #chaickens and wolves on left and right can be any positive integer grater than 0, the boat integer must be 0 or 1 and represents a boolean value of present or not
    start = [[3, 3, 1], [0, 0, 0]]
    goal = [[0, 0, 0], [3, 3, 1]]

    #run search based on argument
    path = []
    if args[0] == "bfs":
        path = search.bfs(start, goal, expand, draw=True)
    elif args[0] == "dfs" :
        path = search.dfs(start, goal, expand, draw=True)
    elif args[0] == "astar":
        path = search.aStar(start, goal, expand, h, draw=True)

    #print results
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