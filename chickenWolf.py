#checks wether a given state is valid or not
def isValidState(state) -> bool:
    #check for a state
    if state == None:
        return False
    #seperate left and right sides
    left = state[0]
    right = state[1]
    #check for negative values
    if left[0] < 0 or left[1] < 0 or right[0] < 0 or right[1] < 0:
        return False
    #check if boat value is valid
    elif left[2] < 0 or left[2] > 1 or right[2] < 0 or right[2] > 1:
        return False
    #check number of chickens an wolves
    else:
        return (left[0] > 0 or left[0] >= left[1]) and (right[0] > 0 or right[0] >= right[1])

#alter current state based on a given action
#actions:
#   0 = move 1 chicken across
#   1 = move 2 chickens across
#   2 = move 1 wolf across
#   3 = move 2 wolves across
#   4 = move 1 chicken and 1 wolf across
def alterState(state, action):
    #chekc what side the boat is on and save this as a multiplier for each side
    left = [state[0][0], state[0][1], -1 if state[0][2] == 1 else 1]
    right = [state[1][0], state[1][1], -1 if state[1][2] == 1 else 1]
    #perform action
    if action == 0:
        left[0] += 1 * left[2]
        right[0] += 1 * right[2]
    elif action == 1:
        left[0] += 2 * left[2]
        right[0] += 2 * right[2]
    elif action == 2:
        left[1] += 1 * left[2]
        right[1] += 1 * right[2]
    elif action == 3:
        left[1] += 2 * left[2]
        right[1] += 2 * right[2]
    elif action == 4:
        left[0] += 1 * left[2]
        right[0] += 1 * right[2]
        left[1] += 1 * left[2]
        right[1] += 1 * right[2]
    #build new state
    newState = [[left[0], left[1], 1 if left[2] == 1 else 0], [right[0], right[1], 1 if right[2] == 1 else 0]]
    return newState

#build a list of next possible states based on a current given state
def expand(state):
    nextNodes = []
    for i in range(0, 5):
        newState = alterState(state, i)
        if isValidState(newState):
            nextNodes.append(newState)
    return nextNodes

#evaluate how close a current state is to the goal
def h(state, goal):
    return (abs(state[0][0] - state[1][0]) + abs(state[0][1] - state[1][1])) / 2