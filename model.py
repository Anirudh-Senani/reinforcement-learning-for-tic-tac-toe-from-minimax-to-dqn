"""
Reinforcement Learning for Tic-Tac-Toe: From Minimax to DQN

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - create_empty_board
import numpy as np

def create_empty_board():
    """Return an empty 3x3 Tic-Tac-Toe board as an int numpy array of zeros."""
    # TODO: return a (3, 3) integer numpy array filled with zeros
    return np.zeros((3,3), dtype=np.int32)

# Step 2 - encode_player
def encode_player(player):
    """Return the integer encoding for 'X', 'O', or 'empty'."""
    # TODO: map 'X' to 1, 'O' to -1, 'empty' to 0
    encoding = {'X':1, 'O':-1, 'empty':0}
    return encoding[player]

# Step 3 - print_board
import numpy as np

def print_board(board):
    """Print the 3x3 board using X, O, and . characters."""
    # TODO: render each cell as 'X' (1), 'O' (-1), or '.' (0) in a 3x3 grid
    board = board.tolist()
    encoding = {1:'X',-1:'O',0:'.'}
    for row in board:
        print(*[encoding[col] for col in row], sep=" ")

# Step 4 - is_cell_empty
import numpy as np

def is_cell_empty(board, row, col):
    """Return True if board[row, col] is empty (0), else False."""
    # TODO: check whether the cell at (row, col) is empty
    return board[row, col] == 0

# Step 5 - place_move
import numpy as np

def place_move(board, row, col, player):
    """Place player's mark at (row, col) and return the new board."""
    # TODO: verify the cell is empty, then return a new board with the mark placed.
    new_board = board.copy()
    if new_board[row, col] != 0:
        raise ValueError
    new_board[row, col] = player
    return new_board

# Step 6 - get_legal_moves
import numpy as np

def get_legal_moves(board):
    """Return a list of (row, col) tuples for all empty cells on the board."""
    # TODO: scan the 3x3 board in row-major order and collect coords of empties
    return [tuple(coord) for coord in np.argwhere(board==0).tolist()]

# Step 7 - check_row_win
import numpy as np

def check_row_win(board, player):
    """Return True if `player` has three-in-a-row across any row of `board`."""
    # TODO: detect whether the given player has three identical marks across any row
    row_len = board.shape[1]
    return np.any((board == player).sum(axis=-1)==row_len)

# Step 8 - check_column_win
import numpy as np

def check_column_win(board, player):
    """Return True if `player` has three-in-a-row in any column of `board`."""
    # TODO: detect whether the given player has three-in-a-row across any column
    col_len = board.shape[0]
    return np.any((board == player).sum(axis=0)==col_len)

# Step 9 - check_main_diagonal_win
import numpy as np

def check_main_diagonal_win(board, player):
    """Return True if `player` occupies all three main-diagonal cells."""
    # TODO: check whether the main diagonal of `board` is fully occupied by `player`...
    return np.all(board.diagonal() == player)

# Step 10 - check_anti_diagonal_win
import numpy as np

def check_anti_diagonal_win(board, player):
    # TODO: return True if `player` occupies all three anti-diagonal cells of the 3x3 board.
    return np.all(np.fliplr(board).diagonal() == player)

# Step 11 - is_winner
import numpy as np

def is_winner(board, player):
    """Return True if `player` has three-in-a-row on `board`."""
    # TODO: combine row, column, and diagonal win checks into a single boolean
    return check_row_win(board, player) or check_column_win(board, player) or check_main_diagonal_win(board, player) or check_anti_diagonal_win(board, player)

# Step 12 - is_draw
import numpy as np

def is_draw(board):
    """Return True iff the board is full and neither player has won."""
    # TODO: combine a full-board check with a no-winner check
    if np.all(board!=0):
        if not (is_winner(board, 1) or is_winner(board, -1)):
            return True
    return False

# Step 13 - get_game_status
import numpy as np

def get_game_status(board):
    """Return 'X_win', 'O_win', 'draw', or 'ongoing' for the given 3x3 board."""
    # TODO: classify the board into one of the four status strings
    status = "ongoing"
    if is_winner(board, 1):
        status = "X_win"
    elif is_winner(board, -1):
        status = "O_win"
    elif is_draw(board):
        status = "draw"
    return status

# Step 14 - get_current_player
import numpy as np

def get_current_player(board):
    """Return 1 if X is to move, -1 if O is to move."""
    # TODO: infer whose turn it is from the counts of X and O marks on the board
    r, c = board.shape
    x_count = (board==1).sum()
    empty_count = (board==0).sum()
    o_count = (r*c) - (x_count + empty_count)
    if (x_count < (r*c)//2 + 1) and x_count > o_count:
        move = -1
    else:
        move = 1
    return move

# Step 15 - switch_player
def switch_player(player):
    """Return the opponent of `player` (1 <-> -1)."""
    # TODO: return the opposite player given 1 for X and -1 for O.
    if player == 1:
        return -1
    return 1

# Step 16 - play_hardcoded_game
import numpy as np

def play_hardcoded_game(moves):
    """Replay a fixed sequence of (row, col) moves and return (final_board, status)."""
    # TODO: start from an empty board with X to move, apply moves until terminal
    player = 1
    board = create_empty_board()
    status = 'ongoing'
    for move in moves:
        board = place_move(board, move[0], move[1], player)
        player = switch_player(player)
        status = get_game_status(board)
        if status in ('X_win', 'O_win', 'draw'):
            break

    return board, status

# Step 17 - play_interactive_game
def play_interactive_game():
    """Play a full game with two humans entering moves via stdin and return the final status."""
    # TODO: loop printing the board, reading 'row col' from stdin, applying moves until terminal
    player = 1
    board = create_empty_board()
    status = 'ongoing'
    while True:
        try:
            row, col = map(int, input().split())
        except EOFError:
            break

        try:
            print_board(board)
            board = place_move(board, row, col, player)
        except ValueError:
            # print("illegal move, try again")
            continue
        player = switch_player(player)
        status = get_game_status(board)

        if status in ('X_win', 'O_win', 'draw'):
            break
    print_board(board)
    return status

# Step 18 - TicTacToeGame
class TicTacToeGame:
    """Stateful Tic-Tac-Toe environment wrapping the Part 1 engine."""

    def __init__(self):
        # TODO: initialize board, current_player, and status fields.
        self.board = create_empty_board()
        self.current_player = 1
        self.status = 'ongoing'

    def reset(self):
        # TODO: return board to empty starting state.
        self.board = create_empty_board()
        self.current_player = 1
        self.status = 'ongoing'
        return self.board

    def legal_moves(self):
        # TODO: list of (row, col) tuples still playable.
        return get_legal_moves(self.board)

    def is_terminal(self):
        # TODO: True once status is no longer 'ongoing'.
        if self.status in ('X_win', 'O_win', 'draw'):
            return True
        return False

    def step(self, row, col):
        # TODO: play current player's move, refresh status, switch player if still ongoing.
        if not self.is_terminal():
            self.board = place_move(self.board, row, col, self.current_player)
            self.status = get_game_status(self.board)
            if not self.is_terminal():
                self.current_player = switch_player(self.current_player)
        else:
            raise ValueError

# Step 19 - random_move_agent
import numpy as np

def random_move_agent(board, player, rng):
    """Return a uniformly random legal (row, col) move for `player`."""
    # TODO: sample a uniformly random legal move using rng and return it as (row, col)
    return tuple(rng.choice(get_legal_moves(board)).tolist())

# Step 20 - play_random_vs_random_game
def play_random_vs_random_game(rng):
    """Simulate one full random-vs-random game and return the final status."""
    # TODO: loop until terminal, alternating random moves between X and O
    player = 1
    board = create_empty_board()
    status = 'ongoing'
    while True:
        try:
            row, col = random_move_agent(board, player, rng)
        except ValueError:
            status = get_game_status(board)
            break

        board = place_move(board, row, col, player)
        player = switch_player(player)
        status = get_game_status(board)

        if status in ('X_win', 'O_win', 'draw'):
            break

    return status

# Step 21 - play_random_vs_random_matches
def play_random_vs_random_matches(n_games, rng):
    """Run n_games random-vs-random games and return the list of outcome strings."""
    # TODO: run n_games independent random-vs-random games and collect outcomes.
    return [play_random_vs_random_game(rng) for _ in range(n_games)]

# Step 22 - compute_outcome_rates
def compute_outcome_rates(outcomes):
    """Return {'x_win_rate','o_win_rate','draw_rate'} from a list of outcome labels."""
    # TODO: count occurrences of each outcome and divide by total games
    x_win_rate = 0
    o_win_rate = 0
    draw_rate = 0
    total = 0
    for out in outcomes:
        if out == 'X_win':
            x_win_rate += 1
        elif out == 'O_win':
            o_win_rate += 1
        else:
            draw_rate += 1
        total += 1

    if total == 0:
        total += 1

    return dict(
        x_win_rate=x_win_rate/total,
        o_win_rate=o_win_rate/total,
        draw_rate=draw_rate/total
    )

# Step 23 - minimax_terminal_score
def minimax_terminal_score(status):
    """Return +1 for 'X_win', -1 for 'O_win', 0 for 'draw'."""
    # TODO: map a terminal status string to its minimax leaf value.
    if status == 'X_win':
        return 1
    elif status == 'O_win':
        return -1
    else:
        return 0

# Step 24 - minimax_value
def minimax_value(board, player):
    """Return the minimax value of `board` with `player` to move."""
    # TODO: terminal -> minimax_terminal_score; else max (X) / min (O) over recursive child values

    status = get_game_status(board)
    if status in {'X_win', 'O_win', 'draw'}:
        return minimax_terminal_score(status)

    child_values = [minimax_value(
                place_move(board, row, col, player),
                switch_player(player),
            )
        for row, col in get_legal_moves(board)]

    value = max(child_values) if player==1 else min(child_values)

    return value

# Step 25 - minimax_recursive
def minimax_recursive(board, player):
    """Return the minimax value of `board` with `player` to move."""
    # TODO: recurse over legal moves, max for X (+1), min for O (-1), terminal via minimax_terminal_score
    def minimax(board, player, memo=None):
        if memo is None:
            memo = {}

        key = (board.tobytes(), player)
        if key in memo:
            return memo[key]

        status = get_game_status(board)
        if status in {'X_win', 'O_win', 'draw'}:
            return minimax_terminal_score(status)

        child_values = [minimax(
                    place_move(board, row, col, player),
                    switch_player(player),
                    memo
                )
            for row, col in get_legal_moves(board)]

        value = max(child_values) if player==1 else min(child_values)
        memo[key] = value

        return value
    return minimax(board, player)

# Step 26 - minimax_max_min_step
def minimax_max_min_step(board, player):
    """Return (best_score, best_move) after expanding one minimax level."""
    # TODO: iterate legal moves, recurse, pick max if player == 1 else min...
    def minimax(board, player, memo=None, coord=None):
        if memo is None:
            memo = {}

        # print(memo)
        key = (board.tobytes(), player)
        if key in memo:
            return memo[key]

        status = get_game_status(board)
        if status in {'X_win', 'O_win', 'draw'}:
            value = (minimax_terminal_score(status), coord)
            return value

        child_values = [((minimax(
                    place_move(board, row, col, player),
                    switch_player(player),
                    memo,
                    (row, col)
                )[0], (row, col)))
            for row, col in get_legal_moves(board)]

        key_fn = lambda x: x[0]
        value = max(child_values, key=key_fn) if player==1 else min(child_values, key=key_fn)
        memo[key] = value

        return value
    return minimax(board, player)

# Step 27 - minimax_best_move
def minimax_best_move(board, player):
    """Return the optimal (row, col) move for `player` via minimax."""
    # TODO: use the minimax max/min step to pick the best legal move for player
    best_score, best_move = minimax_max_min_step(board, player)
    return best_move

# Step 28 - minimax_alpha_beta
import numpy as np

def minimax_alpha_beta(board, player, alpha, beta):
    """Return (best_score, best_move) for `player` using alpha-beta pruning."""
    # TODO: search the game tree with alpha-beta pruning and return (score, move)
    def minimax(board, player, alpha, beta, memo=None, coord=None):
        if memo is None:
            memo = {}

        # print(memo)
        key = (board.tobytes(), player)
        if key in memo:
            return memo[key]

        status = get_game_status(board)
        if status in {'X_win', 'O_win', 'draw'}:
            value = (minimax_terminal_score(status), coord)
            return value

        if player == 1:
            value = (-float('inf'), (None,None))
            for row, col in get_legal_moves(board):
                value = max(value, (minimax(
                            place_move(board, row, col, player),
                            switch_player(player),
                            alpha,
                            beta,
                            memo,
                            (row, col)
                        )[0], (row, col)), key=lambda x: x[0])

                alpha = max(alpha, value[0])
                if alpha >= beta:
                    break

            memo[key] = value
            return value

        value = (float('inf'), (None,None))
        for row, col in get_legal_moves(board):
            value = min(value, (minimax(
                        place_move(board, row, col, player),
                        switch_player(player),
                        alpha,
                        beta,
                        memo,
                        (row, col)
                    )[0], (row, col)), key=lambda x: x[0])

            beta = min(beta, value[0])
            if alpha >= beta:
                break

        memo[key] = value
        return value

    return minimax(board, player, alpha, beta)

# Step 29 - play_minimax_vs_random_matches (not yet solved)
# TODO: implement

# Step 30 - play_minimax_vs_minimax_matches (not yet solved)
# TODO: implement

# Step 31 - encode_board_state_key (not yet solved)
# TODO: implement

# Step 32 - canonical_board_key (not yet solved)
# TODO: implement

# Step 33 - initialize_q_table (not yet solved)
# TODO: implement

# Step 34 - get_q_value (not yet solved)
# TODO: implement

# Step 35 - set_q_value (not yet solved)
# TODO: implement

# Step 36 - choose_learning_rate_alpha (not yet solved)
# TODO: implement

# Step 37 - choose_discount_factor_gamma (not yet solved)
# TODO: implement

# Step 38 - choose_initial_epsilon (not yet solved)
# TODO: implement

# Step 39 - epsilon_decay_schedule (not yet solved)
# TODO: implement

# Step 40 - epsilon_greedy_explore_move (not yet solved)
# TODO: implement

# Step 41 - epsilon_greedy_select_action (not yet solved)
# TODO: implement

# Step 42 - greedy_argmax_over_legal_actions (not yet solved)
# TODO: implement

# Step 43 - random_tie_break_argmax (not yet solved)
# TODO: implement

# Step 44 - tic_tac_toe_reward (not yet solved)
# TODO: implement

# Step 45 - q_learning_nonterminal_target (not yet solved)
# TODO: implement

# Step 46 - q_learning_terminal_target (not yet solved)
# TODO: implement

# Step 47 - q_learning_update (not yet solved)
# TODO: implement

# Step 48 - episode_reset_game (not yet solved)
# TODO: implement

# Step 49 - episode_agent_pick_action (not yet solved)
# TODO: implement

# Step 50 - episode_apply_action (not yet solved)
# TODO: implement

# Step 51 - episode_apply_q_update (not yet solved)
# TODO: implement

# Step 52 - episode_check_terminate (not yet solved)
# TODO: implement

# Step 53 - train_q_learning_agent (not yet solved)
# TODO: implement

# Step 54 - compute_batched_outcome_stats (not yet solved)
# TODO: implement

# Step 55 - self_play_episode (not yet solved)
# TODO: implement

# Step 56 - flip_board_perspective (not yet solved)
# TODO: implement

# Step 57 - perspective_reward_sign (not yet solved)
# TODO: implement

# Step 58 - train_q_agent_self_play (not yet solved)
# TODO: implement

# Step 59 - evaluate_q_agent_vs_random (not yet solved)
# TODO: implement

# Step 60 - evaluate_q_agent_vs_minimax (not yet solved)
# TODO: implement

# Step 61 - inspect_q_values_for_state (not yet solved)
# TODO: implement

# Step 62 - serialize_q_table_to_dict (not yet solved)
# TODO: implement

# Step 63 - deserialize_q_table_from_dict (not yet solved)
# TODO: implement

# Step 64 - encode_board_flat_length_nine (not yet solved)
# TODO: implement

# Step 65 - encode_board_one_hot_length_eighteen (not yet solved)
# TODO: implement

# Step 66 - build_mlp_architecture (not yet solved)
# TODO: implement

# Step 67 - initialize_mlp_parameters (not yet solved)
# TODO: implement

# Step 68 - mlp_forward_pass (not yet solved)
# TODO: implement

# Step 69 - mask_illegal_actions_neg_inf (not yet solved)
# TODO: implement

# Step 70 - argmax_action_from_q_values (not yet solved)
# TODO: implement

# Step 71 - mse_loss_on_chosen_action (not yet solved)
# TODO: implement

# Step 72 - mlp_backward_pass (not yet solved)
# TODO: implement

# Step 73 - adam_update_step (not yet solved)
# TODO: implement

# Step 74 - create_replay_buffer (not yet solved)
# TODO: implement

# Step 75 - append_transition_to_buffer (not yet solved)
# TODO: implement

# Step 76 - cap_buffer_size_drop_oldest (not yet solved)
# TODO: implement

# Step 77 - sample_minibatch_from_buffer (not yet solved)
# TODO: implement

# Step 78 - build_target_network_copy (not yet solved)
# TODO: implement

# Step 79 - compute_target_q_with_target_network (not yet solved)
# TODO: implement

# Step 80 - sync_target_network_periodically (not yet solved)
# TODO: implement

# Step 81 - dqn_select_action (not yet solved)
# TODO: implement

# Step 82 - dqn_train_step (not yet solved)
# TODO: implement

# Step 83 - train_dqn_agent (not yet solved)
# TODO: implement

# Step 84 - compare_dqn_tabular_random_minimax (not yet solved)
# TODO: implement

# Step 85 - sarsa_on_policy_update (not yet solved)
# TODO: implement

# Step 86 - train_sarsa_agent (not yet solved)
# TODO: implement

# Step 87 - reinforce_log_prob_of_action (not yet solved)
# TODO: implement

# Step 88 - reinforce_collect_episode_returns (not yet solved)
# TODO: implement

# Step 89 - reinforce_policy_gradient_update (not yet solved)
# TODO: implement

# Step 90 - train_reinforce_agent (not yet solved)
# TODO: implement

# Step 91 - compare_value_vs_policy_learners (not yet solved)
# TODO: implement

# Step 92 - symmetry_augmented_training (not yet solved)
# TODO: implement

