"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None

class InvalidMove(Exception):
    pass


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
    # Count x and y and return the player with the lowest count.
    count_x = 0
    count_o = 0
    for row in board:
        for col in row:
            if col == X:
                count_x += 1
            elif col == O:
                count_o += 1
    if count_o < count_x:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col == EMPTY:
                actions.add((row_index, col_index))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    try:
        if board[action[0]][action[1]] != EMPTY:
            raise InvalidMove("Invalid Move. Cell already occupied")
        else:
            new_board = copy.deepcopy(board)
            new_board[action[0]][action[1]] = player(board)
            return new_board

    except IndexError:
        raise InvalidMove("Invalid Move. Move is out of bounds")
    
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # Checking Horizontally
    for row_index, row in enumerate(board):
        current = board[row_index][0]
        if current == EMPTY:
            continue
        won = True
        for col in row:
            if col != current:
                won = False
                break
        if won: return current
            
    # Checking Vertically:
    for i in range(len(board)):
        current = board[0][i]
        if current == EMPTY:
            continue
        won = True
        for j in range(len(board[i])):
            if board[j][i] != current:
                won = False
                break
        if won: return current

    # Checking the diagonals going from top left
    # to bottom right, then from top right to bottom left.
    for i in [0, len(board)-1]:
        current = board[0][i]
        if current == EMPTY:
            continue
        won = True
        for j in range(len(board)):
            if board[j][abs(j - i)] != current:
                won = False
                break
        if won: return current

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    the_winner = winner(board)
    if the_winner != None:
        return True # Someone has won
    
    else: # No won has won yet
        # Checking whether there is still space to play
        for row in board:
            for col in row:
                if col == EMPTY:
                    return False  # Still space to play

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win_dict = {X: 1, O: -1, 'None': 0}
    the_winner = winner(board)
    return win_dict[str(the_winner)]


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None
    
    current_player = player(board)

    if current_player == X:
        # It's X's turn, maximize the score
        best_score = float('-inf')
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            score = min_value(new_board)
            if score > best_score:
                best_score = score
                best_action = action
        return best_action

    elif current_player == O:
        # It's O's turn, minimize the score
        best_score = float('inf')
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            score = max_value(new_board)
            if score < best_score:
                best_score = score
                best_action = action
        return best_action

def max_value(board):
    if terminal(board):
        return utility(board)

    v = float('-inf')
    for action in actions(board):
        new_board = result(board, action)
        v = max(v, min_value(new_board))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)

    v = float('inf')
    for action in actions(board):
        new_board = result(board, action)
        v = min(v, max_value(new_board))
    return v
