from .constants import WHITE, BLACK, ROWS, COLS
from .heuristics import game_over, evaluate


def minimax(board, depth, alpha, beta, maximizing_player):
    print(f"Entering minimax: depth={depth}, maximizing={maximizing_player}")
    if depth == 0 or game_over(board):
        eval_score = evaluate(board)
        print(f"Game Over or Depth 0: {eval_score}")
        return eval_score, None

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(board, BLACK):
            piece, new_row, new_col= move
            original_row, original_col = piece.row, piece.col
            board.make_move(move)
            evaluation = minimax(board, depth - 1, alpha, beta, False)[0]
            board.undo_move(move, original_row, original_col)
            print(f"Move Evaluated: {evaluation} vs Max Eval: {max_eval}")
            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move
                print('do i have best move')
            alpha = max(alpha, evaluation)
            print(f"Alpha updated: {alpha}")
            if beta <= alpha:
                print(f"Pruning at alpha: {alpha}, beta: {beta}")
                break

        for wall in get_all_wall_placements(board, BLACK):
            move = ('place_wall', wall[0], wall[1], wall[2])
            if board.valid_wall_placement(wall[0], wall[1], wall[2]):
                board.make_move(move)
                evaluation = minimax(board, depth - 1, alpha, beta, False)[0]
                board.undo_move(move)
                print(f"Wall Placement Evaluated: {evaluation} vs Max Eval: {max_eval}")
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = move
                alpha = max(alpha, evaluation)
                print(f"Alpha updated: {alpha}")
                if beta <= alpha:
                    print(f"Pruning at alpha: {alpha}, beta: {beta}")
                    break

        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(board, WHITE):
            piece, new_row, new_col = move
            original_row, original_col = piece.row, piece.col
            board.make_move(move)
            evaluation = minimax(board, depth - 1, alpha, beta, True)[0]
            board.undo_move(move, original_row, original_col)
            print(f"Move Evaluated: {evaluation} vs Min Eval: {min_eval}")
            if evaluation < min_eval:
                min_eval = evaluation
                best_move = move
            beta = min(beta, evaluation)
            print(f"Beta updated: {beta}")
            if beta <= alpha:
                print(f"Pruning at alpha: {alpha}, beta: {beta}")
                break

        for wall in get_all_wall_placements(board, WHITE):
            move = ('place_wall', wall[0], wall[1], wall[2])
            if board.valid_wall_placement(wall[0], wall[1], wall[2]):
                board.make_move(move)
                evaluation = minimax(board, depth - 1, alpha, beta, True)[0]
                board.undo_move(move)
                print(f"Wall Placement Evaluated: {evaluation} vs Min Eval: {min_eval}")
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move
                beta = min(beta, evaluation)
                print(f"Beta updated: {beta}")
                if beta <= alpha:
                    print(f"Pruning at alpha: {alpha}, beta: {beta}")
                    break

        return min_eval, best_move




def get_all_moves(board, color):
    moves = []
    for row in board.board:
        for piece in row:
            if piece != 0 and piece.color == color:
                moves.extend(get_valid_moves(board, piece))
    return moves 

def get_all_wall_placements(board, color):
    wall_placements = []
    for row in range(ROWS):
        for col in range(COLS):
            if board.valid_wall_placement(row, col, 'horizontal'):
                wall_placements.append((row, col, 'horizontal'))
            if board.valid_wall_placement(row, col, 'vertical'):
                wall_placements.append((row, col, 'vertical'))
    return wall_placements


def get_valid_moves(board, piece):
    valid_moves = []
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]  # Standard moves in Quoridor are two steps in any direction

    for direction in directions:
        new_row = piece.row + direction[0]
        new_col = piece.col + direction[1]
        if board.valid_move(piece, new_row, new_col) and not board.is_wall(piece, new_row, new_col):
            valid_moves.append((piece, new_row, new_col))

    return valid_moves


def ai_move(board):
    depth = 1  # Depth of the search for the minimax algorithm
    _, best_move = minimax(board, depth, float('-inf'), float('inf'), True)
    print("best move", best_move)
    if best_move:
        print(f"AI Move: {best_move}")
        if best_move[0] == 'place_wall':
            if board.player2_wall >= 0:
                print("player2_wall", board.player2_wall)
                print("AI adding_wall")
                board.player2_wall -=1
                board.add_wall(best_move[1], best_move[2], best_move[3])
            else: 
                ai_move(board)
        else:
            board.move_piece(best_move[0], best_move[1], best_move[2])