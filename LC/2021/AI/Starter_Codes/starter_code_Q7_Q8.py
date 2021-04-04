# Function to implement for problem 7
def problem7(game_node):
    def minimax(state):
        player, curr_node = state
        if type(curr_node) != list:
            return curr_node, None
        choices = [(minimax(nextState)[0], i) for i, nextState in enumerate(nextStates7(state))]
        if player == 1:
            return max(choices)
        elif player == -1:
            return min(choices)

    expected_profit, choice = minimax((1, game_node))
    return choice, expected_profit


# Function to implement for problem 8
def problem8(game_node):
    def expectimax(state):
        player, curr_node = state
        if type(curr_node) != list:
            return curr_node, None
        choices = [(expectimax(nextState)[0], i) for i, nextState in enumerate(nextStates8(state))]
        if player == 1:
            return max(choices)
        elif player == 0:
            probabilities = [p for p, _ in curr_node]
            return sum(p * c[0] for p, c in zip(probabilities, choices)), None
        elif player == -1:
            return min(choices)

    expected_profit, choice = expectimax((1, game_node))
    return choice, expected_profit


# You can define more helper functions here. Feel free to modify anything.
def isEnd(state):
    _, currNode = state
    return type(currNode) != list


def nextStates8(state):
    if isEnd(state):
        raise ValueError("You have reached the end")
    player, curr_node = state
    if player == 1:
        next_player = 0
        return [(next_player, node) for node in curr_node]
    elif player == 0:
        next_player = -1
        return [(next_player, node) for prob, node in curr_node]
    elif player == -1:
        next_player = 1
        return [(next_player, node) for node in curr_node]


def nextStates7(state):
    if isEnd(state):
        raise ValueError("You have reached the end")
    player, currNode = state
    nextPlayer = -1 * player
    return [(nextPlayer, node) for node in currNode]


if __name__ == '__main__':
    test_case_1 = [[[1], [3, -2, -5]], [[99], [2, -99]], [4]]
    test_case_1_result = problem7(test_case_1)
    print("problem 7 result: " + str(test_case_1_result))
    print("problem 7 correctness: " + str(test_case_1_result == (2, 4)))

    test_case_2 = [[(0.5, [2, 4]), (0.5, [7, 4])], [(0.5, [6, 0]), (0.5, [5, -2])]]
    test_case_2_result = problem8(test_case_2)
    print("problem 7 result: " + str(test_case_2_result))
    print("problem 7 correctness: " + str(test_case_2_result == (0, 3)))
