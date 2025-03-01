"""
Tic Tac Toe Player
"""
print("Le fichier tictactoe.py s'est bien exécuté !")
import math
import copy

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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action")

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # Check rows and columns
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_value = -math.inf
        best_move = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action
        return best_move

    else:  # current_player == O
        best_value = math.inf
        best_move = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action
        return best_move

def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
# fonction pou tester le role de qui
X = 'X'
O = 'O'

# Exemple de plateau avec un certain nombre de X et O
board = [
    [X, EMPTY, X],
    [O, X, O],
    [O, X, EMPTY]
]

# Appeler la fonction player pour déterminer le prochain joueur
next_player = player(board)

# Afficher le joueur qui doit jouer
print(next_player)

# fonction pou teste les actions possibles
EMPTY = None  # Définir ce que représente une case vide

# Exemple de plateau de jeu (tic-tac-toe)
board = [
    [EMPTY, 'X', 'O'],
    ['X', EMPTY, 'O'],
    ['O', 'X', EMPTY]
]

# Appeler la fonction actions avec ce board
available_actions = actions(board)

# Afficher les actions disponibles
print(available_actions)

# fonction pour tester result
X = 'X'
O = 'O'

def actions(board):
    """Retourne l'ensemble de toutes les actions possibles sur le plateau"""
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def player(board):
    """Retourne le joueur qui doit jouer"""
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O

EMPTY = None

# Exemple de plateau de jeu
board = [
    [EMPTY, 'X', 'O'],
    ['X', EMPTY, 'O'],
    ['O', 'X', EMPTY]
]

# Exemple d'action
action = (0, 0)  # Le joueur va jouer en (0, 0)

# Appeler la fonction result pour obtenir le nouveau plateau
new_board = result(board, action)

# Afficher le nouveau plateau
for row in new_board:
    print(row)
print("Le fichier tictactoe.py s'est bien exécuté !")
