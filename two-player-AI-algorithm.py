def minimax(state, depth, is_maximizing):
    if game_over(state):
        return evaluate(state)  # Return the utility of the state
    
    if is_maximizing:
        max_eval = float('-inf')
        for move in get_possible_moves(state):
            eval = minimax(make_move(state, move), depth + 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_possible_moves(state):
            eval = minimax(make_move(state, move), depth + 1, True)
            min_eval = min(min_eval, eval)
        return min_eval
# Optimize with Alpha-Beta Pruning

def minimax_alpha_beta(state, depth, alpha, beta, is_maximizing):
    if game_over(state):
        return evaluate(state)

    if is_maximizing:
        max_eval = float('-inf')
        for move in get_possible_moves(state):
            eval = minimax_alpha_beta(make_move(state, move), depth + 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_possible_moves(state):
            eval = minimax_alpha_beta(make_move(state, move), depth + 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
/*..

f

 */ 
