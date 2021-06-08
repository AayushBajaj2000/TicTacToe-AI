"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    turnCount = 0

    # Looping over the board
    for i in range(3):
        for j in range(3):
            # If the value is not empty then add to turnCount
            if board[i][j] != EMPTY:
                turnCount = turnCount + 1

    # If turnCount is divisible by 2 then it is X's turn (takes care of the empty state as well)
    return O if turnCount % 2 else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    # Looping over the board
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions if actions else None


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Check if action can be done
    if (action[0] < 0 or action[0] > 2) or (action[1] < 0 or action[1] > 2):
        raise Exception("Not a valid action")

    # Make a copy of the board
    tempBoard = copy.deepcopy(board)

    if tempBoard[action[0]][action[1]] != EMPTY:
        raise Exception("Not a valid action")

    # Updating the board with the action
    tempBoard[action[0]][action[1]] = player(tempBoard)

    return tempBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check Horizontal and Vertical
    for i in range(3):
        # Check Horizontal
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == board[i][2]:
            return board[i][0]

        # Check Vertical
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] == board[2][i]:
            return board[0][i]

    # Check Diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == board[2][0]:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Check for a winner
    if winner(board):
        return True

    # Check if all the places are filled
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) is True:
        return None

    if player(board) == X:
        score = -float("inf")
        bestMove = None

        for action in actions(board):
            val = minvalue(result(board, action))

            if val > score:
                score = val
                bestMove = action

        return bestMove
    else:
        score = float("inf")
        bestMove = None

        for action in actions(board):
            val = maxvalue(result(board, action))

            if val < score:
                score = val
                bestMove = action

        return bestMove


def maxvalue(board):

    # If this is the last possible state then return the utility
    if terminal(board):
        return utility(board)

    val = float('-inf')

    # If not over then look into all the actions possible
    for action in actions(board):
        val = max(val, minvalue(result(board, action)))

    return val


def minvalue(board):
    # If this is the last possible state then return the utility
    if terminal(board):
        return utility(board)

    val = float('inf')

    # If not over then look into all the actions possible
    for action in actions(board):
        val = min(val, maxvalue(result(board, action)))

    return val

