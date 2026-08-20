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
def minimax_alpha_beta(board, player, alpha, beta):
    """Return (best_score, best_move) for `player` using alpha-beta pruning."""
    # TODO: search the game tree with alpha-beta pruning and return (score, move)
    def minimax(board, player, alpha, beta, memo=None):
        if memo is None:
            memo = {}

        # print(memo)
        key = (board.tobytes(), player)
        if key in memo:
            return memo[key]

        status = get_game_status(board)
        if status in {'X_win', 'O_win', 'draw'}:
            return minimax_terminal_score(status), None

        if player == 1:
            fully_searched = True
            value = (-float('inf'), (None,None))
            for row, col in get_legal_moves(board):
                child_value, _ = minimax(
                            place_move(board, row, col, player),
                            switch_player(player),
                            alpha,
                            beta,
                            memo
                        )

                if child_value > value[0]:
                    value = (child_value, (row, col))

                alpha = max(alpha, value[0])
                if alpha >= beta:
                    fully_searched = False
                    break

            if fully_searched:
                memo[key] = value
            return value

        value = (float('inf'), (None,None))
        fully_searched = True
        for row, col in get_legal_moves(board):
            child_value, _ = minimax(
                        place_move(board, row, col, player),
                        switch_player(player),
                        alpha,
                        beta,
                        memo
                    )
            
            if child_value < value[0]:
                value = (child_value, (row, col))

            beta = min(beta, value[0])
            if alpha >= beta:
                fully_searched = False
                break

        if fully_searched:
            memo[key] = value
        return value

    return minimax(board, player, alpha, beta)

# Step 29 - play_minimax_vs_random_matches
def play_minimax_vs_random_matches(n_games, minimax_plays_x, rng):
    # TODO: run n_games of minimax vs random and return aggregated outcome rates.
    outcomes = []
    for _ in range(n_games):
        board = create_empty_board()
        player = 1
        status = 'ongoing'
        while status not in ('X_win', 'O_win', 'draw'):
            if minimax_plays_x and player==1:
                # score, move = minimax_alpha_beta(board, player, -10, 10)
                move = minimax_best_move(board, player)
            elif (not minimax_plays_x) and player==-1:
                # score, move = minimax_alpha_beta(board, player, -10, 10)
                move = minimax_best_move(board, player)
            elif (not minimax_plays_x) and player==1:
                move = random_move_agent(board, player, rng)
            elif minimax_plays_x and player==-1:
                move = random_move_agent(board, player, rng)
            board = place_move(board, move[0], move[1], player)
            status = get_game_status(board)
            player = switch_player(player)
        outcomes.append(status)

    return compute_outcome_rates(outcomes)

# Step 30 - play_minimax_vs_minimax_matches
def play_minimax_vs_minimax_matches(n_games):
    """Play n_games minimax-vs-minimax games and report outcome rates plus an all_draws flag."""
    # TODO: simulate n_games minimax-vs-minimax games and aggregate outcome rates.
    outcomes = []
    for _ in range(n_games):
        board = create_empty_board()
        player = 1
        status = 'ongoing'
        while status not in {'X_win', 'O_win', 'draw'}:
            row, col = minimax_best_move(board, player)
            board = place_move(board, row, col, player)
            status = get_game_status(board)
            player = switch_player(player)
        outcomes.append(status)

    result = compute_outcome_rates(outcomes)
    result['all_draws'] = result['draw_rate'] == 1.0 if len(outcomes)>0 else True

    return result

# Step 31 - encode_board_state_key
import numpy as np

def encode_board_state_key(board):
    """Encode a 3x3 board as a length-9 string over {'0','1','2'} in row-major order."""
    # TODO: map each cell (0, 1, -1) to a single character and join row-major.
    board = board.flatten()
    board = np.where(board==-1, 2, board)
    return "".join(map(str, board.tolist()))

# Step 32 - canonical_board_key
def canonical_board_key(board):
    # TODO: return the lex-smallest encoded key over all 8 symmetries of the board.
    keys = []
    keys.append(encode_board_state_key(board))
    keys.append(encode_board_state_key(board.T))
    keys.append(encode_board_state_key(np.rot90(board, 1)))
    keys.append(encode_board_state_key(np.rot90(board, 2)))
    keys.append(encode_board_state_key(np.rot90(board, 1)))
    keys.append(encode_board_state_key(np.fliplr(board)))
    keys.append(encode_board_state_key(np.flipud(board)))
    keys.append(encode_board_state_key(np.fliplr(np.flipud(board)).T))

    return min(keys)

# Step 33 - initialize_q_table
from collections import defaultdict

def initialize_q_table():
    """Create an empty Q-table that returns 0.0 for unseen (state, action) keys."""
    # TODO: return a mapping where missing (state_key, action) lookups yield 0.0
    return defaultdict(float)

# Step 34 - get_q_value
def get_q_value(q_table, state_key, action):
    # TODO: return Q(state_key, action), or 0.0 if the pair is not in the table
    return q_table.get((state_key, action), 0.0)

# Step 35 - set_q_value
def set_q_value(q_table, state_key, action, value):
    """Write a new Q-value for a (state, action) pair into the Q-table."""
    # TODO: store value under the (state_key, action) key in q_table.
    q_table[(state_key, action)] = value

# Step 36 - choose_learning_rate_alpha
def choose_learning_rate_alpha():
    """Return the learning rate alpha (float in (0, 1]) for tabular Q-learning."""
    # TODO: return a float in (0, 1] to use as the Q-learning step size.
    return 0.1

# Step 37 - choose_discount_factor_gamma
def choose_discount_factor_gamma():
    """Return the discount factor gamma in [0, 1] for Q-learning."""
    # TODO: return a float discount factor in [0, 1] for tabular Q-learning.
    return 0.9

# Step 38 - choose_initial_epsilon
def choose_initial_epsilon():
    """Return the starting exploration rate epsilon for epsilon-greedy."""
    # TODO: return the starting exploration rate in [0, 1] favoring exploration
    return 1.0

# Step 39 - epsilon_decay_schedule
import numpy as np

def epsilon_decay_schedule(initial_epsilon, episode_index, min_epsilon, decay_rate):
    """Return the decayed epsilon for the given episode, clipped to min_epsilon."""
    # TODO: compute exponential decay of initial_epsilon over episode_index, clipped to a floor.
    return max(min_epsilon, initial_epsilon*np.exp(-episode_index*decay_rate))

# Step 40 - epsilon_greedy_explore_move
def epsilon_greedy_explore_move(legal_actions, rng):
    """Sample a uniformly random legal action from legal_actions using rng."""
    # TODO: pick one action uniformly at random from legal_actions using rng
    if isinstance(legal_actions[0], (list, tuple)):
        return tuple(rng.choice(legal_actions).tolist())
    else:
        return int(rng.choice(legal_actions))

# Step 41 - epsilon_greedy_select_action
def epsilon_greedy_select_action(q_table, state_key, legal_actions, epsilon, rng):
    """Choose an action via epsilon-greedy over the legal actions."""
    # TODO: with probability epsilon explore, else pick the greedy legal action.
    if rng.random() <= epsilon:
        move = epsilon_greedy_explore_move(legal_actions, rng)
    else:
        move = greedy_argmax_over_legal_actions(q_table, state_key, legal_actions, rng)

    return move

# Step 42 - greedy_argmax_over_legal_actions
def greedy_argmax_over_legal_actions(q_table, state_key, legal_actions, rng):
    """Return the legal action with the highest Q-value (random tie-break)."""
    # TODO: return the legal action with the highest Q(state_key, action)...
    q_values = [get_q_value(q_table, state_key, action) for action in legal_actions]
    max_q_val = max(q_values)
    ind = rng.choice([i for i in range(len(q_values)) if q_values[i]==max_q_val])
    return legal_actions[ind]

# Step 43 - random_tie_break_argmax
def random_tie_break_argmax(values, candidates, rng):
    """Return one candidate whose value equals max(values), tie-broken uniformly at random."""
    # TODO: pick a candidate whose value equals the maximum, breaking ties uniformly with rng.
    max_val = max(values)
    ind = rng.choice([i for i in range(len(values)) if values[i]==max_val])
    return candidates[ind]

# Step 44 - tic_tac_toe_reward
def tic_tac_toe_reward(game_status, agent_player):
    """Return scalar reward from the agent's perspective.

    game_status: one of 'X_win', 'O_win', 'draw', 'ongoing'.
    agent_player: +1 for X, -1 for O.
    """
    # TODO: map terminal status to +/-1 from the agent's perspective, 0 otherwise
    if game_status == 'X_win' and agent_player==1:
        reward = 1.0
    elif game_status == 'X_win' and agent_player==-1:
        reward = -1.0
    elif game_status == 'O_win' and agent_player==-1:
        reward = 1.0
    elif game_status == 'O_win' and agent_player==1:
        reward = -1.0
    else:
        reward = 0.0
    return reward

# Step 45 - q_learning_nonterminal_target
def q_learning_nonterminal_target(reward, gamma, q_table, next_state_key, next_legal_actions):
    """Return the TD target r + gamma * max_a' Q(s', a') over legal next actions."""
    # TODO: compute the bootstrapped Q-learning target for a non-terminal transition
    rng = np.random.default_rng()
    if len(next_legal_actions)>0:
        next_action = greedy_argmax_over_legal_actions(q_table, next_state_key, next_legal_actions, rng)
        td = reward + gamma*(get_q_value(q_table, next_state_key, next_action))
    else:
        td = reward
    return td

# Step 46 - q_learning_terminal_target
def q_learning_terminal_target(reward):
    """Return the TD target for a terminal transition."""
    # TODO: return the terminal TD target given the observed reward.
    return reward

# Step 47 - q_learning_update
def q_learning_update(q_table, state_key, action, target, alpha):
    """Apply Q(s,a) <- Q(s,a) + alpha * (target - Q(s,a)) and return the new value."""
    # TODO: read current Q via get_q_value, move toward target by alpha, write back with set_q_value
    q_val = get_q_value(q_table, state_key, action)
    q_val += alpha*(target - q_val)
    set_q_value(q_table, state_key, action, q_val)
    return q_val

# Step 48 - episode_reset_game
import numpy as np

def episode_reset_game():
    """Return a fresh empty board and the starting player (+1 for X)."""
    # TODO: build a new empty board and return it alongside the starting player
    return create_empty_board(), 1

# Step 49 - episode_agent_pick_action
def episode_agent_pick_action(q_table, board, current_player, epsilon, rng):
    # TODO: return (canonical_state_key, action_index_0_to_8) using epsilon-greedy over legal moves.
    state_key = canonical_board_key(board)
    legal_actions = [row*3+col for row,col in get_legal_moves(board)]
    action = epsilon_greedy_select_action(q_table, state_key, legal_actions, epsilon, rng)

    return state_key, action

# Step 50 - episode_apply_action
def episode_apply_action(board, action, current_player, agent_player):
    """Apply one move, return next_board/next_player/status/reward/done."""
    # TODO: convert action to (row, col), place the move, then evaluate status and reward.
    row = action//3
    col = action%3

    next_board = place_move(board, row, col, current_player)
    next_player = switch_player(current_player)
    status = get_game_status(next_board)
    reward = tic_tac_toe_reward(status, agent_player)
    done = status in {'X_win', 'O_win', 'draw'}

    return dict(
        next_board=next_board,
        next_player=next_player,
        status=status,
        reward=reward,
        done=done
    )

# Step 51 - episode_apply_q_update
def episode_apply_q_update(q_table, state_key, action, reward, next_board, done, alpha, gamma):
    """Compute the TD target (terminal or nonterminal) and apply the Q-learning update."""
    # TODO: branch on done, build the appropriate target, then call the update helper.
    if done:
        td = q_learning_terminal_target(reward)
    else:
        next_state_key = canonical_board_key(next_board)
        # next_legal_actions = [row*3+col for row,col in get_legal_moves(next_board)]
        next_legal_actions = get_legal_moves(next_board)
        td = q_learning_nonterminal_target(reward, gamma, q_table, next_state_key, next_legal_actions)

    q_val = q_learning_update(q_table, state_key, action, td, alpha)
    return q_val

# Step 52 - episode_check_terminate
def episode_check_terminate(status):
    """Return True if status is terminal (win or draw), else False."""
    # TODO: return True when status indicates the episode should end
    return status in {'X_win', 'O_win', 'draw'}

# Step 53 - train_q_learning_agent
def train_q_learning_agent(num_episodes, alpha, gamma, initial_epsilon, min_epsilon, decay_rate, opponent_policy, rng):
    # TODO: run N Q-learning episodes vs opponent_policy, decay epsilon, return q_table and outcomes
    q_table = initialize_q_table()
    episode_outcomes = []
    for ep in range(num_episodes):
        epsilon = epsilon_decay_schedule(initial_epsilon, ep, min_epsilon, decay_rate)
        board, player = episode_reset_game()
        agent_player = 1
        status = 'ongoing'
        while True:
            state_key, action = episode_agent_pick_action(q_table, board, player, epsilon, rng)
            cur_state = episode_apply_action(board, action, player, agent_player)
            next_board = cur_state['next_board']
            status = cur_state['status']
            reward = cur_state['reward']
            player = cur_state['next_player']
            done = cur_state['done']

            if not done:
                move = opponent_policy(next_board, player, rng)
                cur_state = episode_apply_action(next_board, move, player, agent_player)
                next_board = cur_state['next_board']
                status = cur_state['status']
                # reward = cur_state['reward']
                player = cur_state['next_player']
                done = cur_state['done']
                # if done:
                #     break

            episode_apply_q_update(q_table, state_key, action, reward, next_board, done, alpha, gamma)
            board = next_board
            if done:
                break
        episode_outcomes.append(status)

    return dict(
        q_table=q_table,
        episode_outcomes=episode_outcomes
    )

# Step 54 - compute_batched_outcome_stats
import numpy as np

def compute_batched_outcome_stats(episode_outcomes, batch_size):
    """Aggregate outcomes into per-batch win/loss/draw rates."""
    # TODO: group outcomes into chunks of batch_size and compute rates per chunk
    num_batches = len(episode_outcomes)//batch_size
    win_rates = []
    loss_rates = []
    draw_rates = []
    for i in range(num_batches):
        rates = compute_rates(episode_outcomes[i*batch_size:(i+1)*batch_size])
        win_rates.append(rates[0])
        loss_rates.append(rates[1])
        draw_rates.append(rates[2])

    return dict(
        batch_index = np.arange(num_batches),
        win_rate=np.asarray(win_rates),
        loss_rate=np.asarray(loss_rates),
        draw_rate=np.asarray(draw_rates)
    )


def compute_rates(outcomes):
    """Return {'x_win_rate','o_win_rate','draw_rate'} from a list of outcome labels."""
    # TODO: count occurrences of each outcome and divide by total games
    win_rate = 0
    loss_rate = 0
    draw_rate = 0
    total = 0
    for out in outcomes:
        if out == 'win':
            win_rate += 1
        elif out == 'loss':
            loss_rate += 1
        else:
            draw_rate += 1
        total += 1

    if total == 0:
        total += 1

    return win_rate/total, loss_rate/total, draw_rate/total

# Step 55 - self_play_episode
def self_play_episode(q_table, alpha, gamma, epsilon, rng):
    """Run one self-play episode and return final_status and a list of transitions."""
    # TODO: loop until terminal, picking actions with episode_agent_pick_action and applying them
    board, player = episode_reset_game()
    transitions = []
    while True:
        state_key, action = episode_agent_pick_action(q_table, board, player, epsilon, rng)
        cur_state = episode_apply_action(board, action, player, player)
        transitions.append(dict(
            state_key=state_key,
            action=action,
            reward=cur_state['reward'],
            next_board=cur_state['next_board'],
            done=cur_state['done'],
            player=player
        ))

        player = cur_state['next_player']
        board = cur_state['next_board']
        if cur_state['done']:
            break

    return dict(
        final_status=cur_state['status'],
        transitions=transitions
    )

# Step 56 - flip_board_perspective
import numpy as np

def flip_board_perspective(board, current_player):
    """Return a board view where current_player's marks are +1."""
    # TODO: return a new (3,3) int array expressed from current_player's perspective
    return np.where(board!=0, board//current_player, 0)

# Step 57 - perspective_reward_sign
def perspective_reward_sign(reward, acting_player, scoring_player):
    """Return reward expressed from acting_player's perspective."""
    # TODO: flip the sign of reward when acting_player and scoring_player differ
    if acting_player != scoring_player:
        reward /= -1
    return reward

# Step 58 - train_q_agent_self_play
def train_q_agent_self_play(num_episodes, alpha, gamma, initial_epsilon, min_epsilon, decay_rate, rng):
    # TODO: run num_episodes of self-play, applying Q-learning updates with perspective flipping.
    q_table = initialize_q_table()
    episode_outcomes = []
    for ep in range(num_episodes):
        epsilon = epsilon_decay_schedule(initial_epsilon, ep, min_epsilon, decay_rate)
        self_play_ep = self_play_episode(q_table, alpha, gamma, epsilon, rng)
        episode_outcomes.append(self_play_ep['final_status'])
        for transit in self_play_ep['transitions']:
            player = transit['player']
            reward = perspective_reward_sign(transit['reward'], player, 1)
            next_board = flip_board_perspective(transit['next_board'], player)
            episode_apply_q_update(q_table, transit['state_key'], transit['action'], reward, next_board, transit['done'], alpha, gamma)

    return dict(
        q_table=q_table,
        episode_outcomes=episode_outcomes
    )

# Step 59 - evaluate_q_agent_vs_random
def evaluate_q_agent_vs_random(q_table, num_games, rng):
    """Play num_games between the greedy Q-agent and a random opponent.

    Returns a dict with keys 'wins', 'losses', 'draws' (ints) and
    'win_rate', 'loss_rate', 'draw_rate' (floats), all from the agent's
    perspective. The agent alternates between playing X and O across games.
    """
    # TODO: simulate num_games and tally outcomes from the agent's perspective
    wins = 0
    losses = 0
    draws = 0

    agent = 1
    for _ in range(num_games):
        board, _ = episode_reset_game()
        player = agent
        status = 'ongoing'
        while True:
            state_key = canonical_board_key(flip_board_perspective(board, player))
            legal_actions = get_legal_moves(board)
            row, col = greedy_argmax_over_legal_actions(q_table, state_key, legal_actions, rng)
            board = place_move(board, row, col, player)
            status = get_game_status(board)
            done = episode_check_terminate(status)
            player = switch_player(player)

            if not done:
                legal_actions = get_legal_moves(board)
                row, col = rng.choice(legal_actions)
                board = place_move(board, row, col, player)
                status = get_game_status(board)
                done = episode_check_terminate(status)
                player = switch_player(player)
            
            if done:
                break
        
        reward = tic_tac_toe_reward(status, agent)
        if reward == 1.0:
            wins += 1
        elif reward == -1.0:
            losses += 1
        else:
            draws += 1
        
        agent = switch_player(agent)
    
    if num_games == 0:
        num_games += 1
    
    return dict(
        wins=wins,
        losses=losses,
        draws=draws,
        win_rate=wins/num_games,
        loss_rate=losses/num_games,
        draw_rate=draws/num_games
    )

# Step 60 - evaluate_q_agent_vs_minimax
def evaluate_q_agent_vs_minimax(q_table, num_games, rng):
    # TODO: play num_games matches alternating X/O between Q-agent and minimax, return agent-perspective rates.
    def pick_action(board, player, agent):
        if player == agent:
            state_key = canonical_board_key(flip_board_perspective(board, player))
            legal_actions = get_legal_moves(board)
            move = greedy_argmax_over_legal_actions(q_table, state_key, legal_actions, rng)
        else:
            legal_actions = get_legal_moves(board)
            move = minimax_best_move(board, player)
        return move


    wins = 0
    losses = 0
    draws = 0
    agent = 1
    for _ in range(num_games):
        board, player = episode_reset_game()
        status = 'ongoing'
        while True:
            row, col = pick_action(board, player, agent)
            board = place_move(board, row, col, player)
            status = get_game_status(board)
            done = episode_check_terminate(status)
            player = switch_player(player)

            if not done:
                row, col = pick_action(board, player, agent)
                board = place_move(board, row, col, player)
                status = get_game_status(board)
                done = episode_check_terminate(status)
                player = switch_player(player)

            if done:
                break

        reward = tic_tac_toe_reward(status, agent)
        if reward == 1.0:
            wins += 1
        elif reward == -1.0:
            losses += 1
        else:
            draws += 1

        agent = switch_player(agent)

    if num_games == 0:
        num_games += 1

    return dict(
        x_win_rate=wins/num_games,
        o_win_rate=losses/num_games,
        draw_rate=draws/num_games
    )

# Step 61 - inspect_q_values_for_state
import numpy as np

def inspect_q_values_for_state(q_table, board, current_player):
    """Print the board and Q-values for all 9 cells; return a length-9 array."""
    # TODO: look up Q-values for every cell of the board and pretty-print them.
    state_key = canonical_board_key(board)
    q_vals = []
    print_board(board)
    for i in range(3):
        row_str = ""
        for j in range(3):
            val = get_q_value(q_table, state_key, (i,j))
            row_str += f" {val:+.2f}"
            q_vals.append(val)
        print(row_str.strip())
    return np.asarray(q_vals)

# Step 62 - serialize_q_table_to_dict
def serialize_q_table_to_dict(q_table):
    """Convert a Q-table (str -> np.ndarray shape (9,)) into a plain dict (str -> list of floats)."""
    # TODO: convert each numpy array value into a plain Python list of floats
    return {key: val.astype(float).tolist() for key, val in q_table.items()}

# Step 63 - deserialize_q_table_from_dict
import numpy as np

def deserialize_q_table_from_dict(serialized):
    """Rebuild a Q-table (state_key -> np.ndarray shape (9,)) from a plain dict."""
    # TODO: convert each list value back into a numpy float array of shape (9,)
    return {key: np.asarray(val, dtype=np.float64) for key, val in serialized.items()}

# Step 64 - encode_board_flat_length_nine
import numpy as np

def encode_board_flat_length_nine(board, current_player):
    """Encode a 3x3 board as a length-9 float32 vector from current_player's view."""
    # TODO: relabel pieces so own=+1, opponent=-1, empty=0, then flatten to (9,) float32
    return flip_board_perspective(board, current_player).flatten().astype(np.float32)

# Step 65 - encode_board_one_hot_length_eighteen
import numpy as np

def encode_board_one_hot_length_eighteen(board, current_player):
    """Encode a 3x3 board as a length-18 two-channel one-hot vector."""
    # TODO: build own-piece and opponent-piece masks, flatten and concatenate
    opponent_player = switch_player(current_player)
    current_pieces = np.where(board==current_player, 1.0, 0.0).flatten()
    opponent_pieces = np.where(board==opponent_player, 1.0, 0.0).flatten()

    return np.concatenate([current_pieces, opponent_pieces]).astype(np.float32)

# Step 66 - build_mlp_architecture
def build_mlp_architecture(input_dim, hidden_dim, output_dim=9):
    # TODO: return a dict describing input_dim -> hidden_dim -> output_dim layer sizes.
    return dict(
        input_dim=input_dim,
        hidden_dim=hidden_dim,
        output_dim=output_dim
    )

# Step 67 - initialize_mlp_parameters
def initialize_mlp_parameters(architecture, seed=0):
    """Initialize MLP weights with He init and zero biases.

    architecture: dict from build_mlp_architecture with input_dim, hidden_dim, output_dim.
    seed: int seed for numpy RNG.
    Returns dict with keys 'W1', 'b1', 'W2', 'b2'.
    """
    # TODO: sample weights with He init and zero the biases
    # rng = np.random.default_rng(seed)
    np.random.seed(seed)
    d_in = architecture['input_dim']
    d_h = architecture['hidden_dim']
    d_out = architecture['output_dim']

    # W1 = rng.normal(loc=0.0, scale=(2/d_in)**0.5, size=(d_in, d_h))
    W1 = np.random.normal(loc=0.0, scale=(2/d_in)**0.5, size=(d_in, d_h))
    b1 = np.zeros(d_h)
    # W2 = rng.normal(loc=0.0, scale=(2/d_h)**0.5, size=(d_h, d_out))
    W2 = np.random.normal(loc=0.0, scale=(2/d_h)**0.5, size=(d_h, d_out))
    b2 = np.zeros(d_out)

    return dict(
        W1=W1,
        b1=b1,
        W2=W2,
        b2=b2
    )

# Step 68 - mlp_forward_pass
def mlp_forward_pass(params, x):
    """Forward pass through a two-layer MLP with ReLU hidden activation.

    Args:
        params: dict with keys 'W1', 'b1', 'W2', 'b2'.
        x: np.ndarray of shape (batch, input_dim).

    Returns:
        (q_values, cache) where q_values has shape (batch, output_dim) and
        cache is a dict with keys {'x', 'z1', 'h1', 'q'}.
    """
    # TODO: compute z1 = x W1 + b1, h1 = ReLU(z1), q = h1 W2 + b2, cache intermediates.
    z1 = x @ params['W1'] + params['b1']
    h1 = np.maximum(z1, 0.0)
    q = h1 @ params['W2'] + params['b2']

    return q,dict(x=x, z1=z1, h1=h1, q=q)

# Step 69 - mask_illegal_actions_neg_inf
import numpy as np

def mask_illegal_actions_neg_inf(q_values, legal_action_mask):
    """Return a copy of q_values with illegal entries set to -inf."""
    # TODO: replace q-values at positions where the mask is False with -inf
    return np.where(legal_action_mask, q_values, -np.inf)

# Step 70 - argmax_action_from_q_values
import numpy as np

def argmax_action_from_q_values(masked_q_values):
    """Return the index of the largest entry in masked_q_values as an int."""
    # TODO: pick the action index with the highest (masked) Q-value
    return int(np.argmax(masked_q_values))

# Step 71 - mse_loss_on_chosen_action
import numpy as np

def mse_loss_on_chosen_action(predicted_q, action_indices, target_q):
    """MSE between Q(s, a_taken) and the bootstrapped target Q."""
    # TODO: gather one Q-value per row using action_indices, then mean squared error vs target_q.
    return float(np.mean((predicted_q[np.arange(predicted_q.shape[0]),action_indices] - target_q)**2))

# Step 72 - mlp_backward_pass
def mlp_backward_pass(params, cache, action_indices, target_q):
    """Backprop MSE-on-chosen-action loss through the MLP and return param gradients."""
    # TODO: compute gradients dW1, db1, dW2, db2 for the MSE-on-chosen-action loss
    batch_size = action_indices.shape[0]
    dres = 2 * (cache['q'][np.arange(batch_size), action_indices] - target_q)/batch_size
    dq = np.zeros_like(cache['q'])
    dq[np.arange(batch_size), action_indices] = 1.0
    dq *= dres[:,None]
    dW2 = cache['h1'].T @ dq
    db2 = dq.sum(axis=0)
    dh1 = dq @ params['W2'].T
    dz1 = np.where(cache['z1']>0.0, dh1, 0.0)
    dW1 = cache['x'].T @ dz1
    db1 = dz1.sum(axis=0)

    return dict(
        W1=dW1,
        b1=db1,
        W2=dW2,
        b2=db2
    )

# Step 73 - adam_update_step
import numpy as np

def adam_update_step(params, grads, adam_state, learning_rate=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    # TODO: perform one Adam step; update adam_state's moments and step counter, return (new_params, adam_state).
    if not adam_state:
        adam_state['m'] = {}
        adam_state['v'] = {}
        adam_state['t'] = 0
        for key in params:
            adam_state['m'][key] = np.zeros_like(params[key])
            adam_state['v'][key] = np.zeros_like(params[key])

    adam_state['t'] += 1

    for key in params:
        adam_state['m'][key] = adam_state['m'][key] * beta1 + grads[key]*(1-beta1)
        adam_state['v'][key] = adam_state['v'][key] * beta2 + (grads[key]**2)*(1-beta2)

        m_t = adam_state['m'][key]/(1-beta1**adam_state['t'])
        v_t = adam_state['v'][key]/(1-beta2**adam_state['t'])

        params[key] -= learning_rate * m_t/(np.sqrt(v_t)+eps)

    return params, adam_state

# Step 74 - create_replay_buffer
from collections import deque


def create_replay_buffer(capacity):
    """Return an empty replay buffer with a fixed maximum capacity."""
    # TODO: build a dict holding an empty bounded deque and the capacity
    return dict(
        data=deque(maxlen=capacity),
        capacity=capacity
    )

# Step 75 - append_transition_to_buffer
def append_transition_to_buffer(buffer, state, action, reward, next_state, done, next_legal_mask):
    """Append one (s, a, r, s', done, next_legal_mask) transition to the replay buffer."""
    # TODO: store the transition tuple in buffer['data']
    buffer['data'].append((state, action, reward, next_state, done, next_legal_mask))
    return buffer

# Step 76 - cap_buffer_size_drop_oldest
def cap_buffer_size_drop_oldest(buffer):
    """Drop oldest transitions until len(buffer['data']) <= buffer['capacity']."""
    # TODO: pop from the front of buffer['data'] until it fits the capacity.
    if isinstance(buffer['data'], list):
        buffer['data'] = buffer['data'][max(len(buffer['data'])-buffer['capacity'],0):]
    else:
        for _ in range(max(len(buffer['data'])-buffer['capacity'],0)):
            buffer['data'].popleft()

    return buffer

# Step 77 - sample_minibatch_from_buffer
import numpy as np


def sample_minibatch_from_buffer(buffer, batch_size, rng):
    """Draw `batch_size` random transitions from `buffer` and stack fields into arrays."""
    # TODO: draw a uniformly random minibatch of transitions and stack each field.
    batch = {}
    for key in buffer['data'][0]:
        batch[key+'s'] = []

    for transition in rng.choice(buffer['data'], size=batch_size):
        for key in transition:
            batch[key+'s'].append(transition[key])

    for key in batch:
        batch[key] = np.stack(batch[key])

    return batch

# Step 78 - build_target_network_copy
import numpy as np

def build_target_network_copy(online_params):
    """Return a deep copy of the online MLP parameter dict."""
    # TODO: return a new dict whose arrays are independent copies of online_params
    target = {}
    for key in online_params:
        target[key] = online_params[key].copy()
    return target

# Step 79 - compute_target_q_with_target_network
import numpy as np

def compute_target_q_with_target_network(target_params, batch, gamma):
    """Compute DQN bootstrap targets r + gamma * max_a' Q_target(s', a')."""
    # TODO: forward next_states through the target net, mask illegal actions, take max, zero on terminals
    q_target, _ = mlp_forward_pass(target_params, batch['next_states'])
    q_target_masked = mask_illegal_actions_neg_inf(q_target, batch['next_legal_masks'])
    q_target_masked_max = q_target_masked.max(axis=-1)
    q_target_masked_max = np.where(batch['dones'], 0.0, q_target_masked_max)

    return batch['rewards'] + gamma * q_target_masked_max

# Step 80 - sync_target_network_periodically
import numpy as np

def sync_target_network_periodically(online_params, target_params, step_count, sync_every_k):
    """Copy online -> target every sync_every_k steps; otherwise leave target unchanged."""
    # TODO: refresh target_params from online_params when step_count is a positive multiple of sync_every_k
    if step_count%sync_every_k == 0 and step_count != 0:
        target_params = build_target_network_copy(online_params)
    return target_params

# Step 81 - dqn_select_action
def dqn_select_action(online_params, state, legal_mask, epsilon, rng):
    """Epsilon-greedy action index over the legal moves."""
    # TODO: explore with prob epsilon (random legal action) else argmax of masked Q-values
    if rng.random() <= epsilon:
        action = int(rng.choice(np.arange(legal_mask.shape[0])[legal_mask]))
    else:
        q_values, _ = mlp_forward_pass(online_params, state)
        q_values = mask_illegal_actions_neg_inf(q_values, legal_mask)
        action = argmax_action_from_q_values(q_values)

    return action

# Step 82 - dqn_train_step
def dqn_train_step(online_params, target_params, adam_state, buffer, batch_size, gamma, lr, rng):
    """Run one DQN minibatch update. Return (online_params, adam_state, loss)."""
    # TODO: sample -> targets -> forward -> loss -> backward -> adam step
    batch = sample_minibatch_from_buffer(buffer, batch_size, rng)
    targets = compute_target_q_with_target_network(target_params, batch, gamma)
    q_vals, cache = mlp_forward_pass(online_params, batch['states'])

    loss = mse_loss_on_chosen_action(q_vals, batch['actions'], targets)
    grads = mlp_backward_pass(online_params, cache, batch['actions'], targets)
    online_params, adam_state = adam_update_step(online_params, grads, adam_state, lr)

    return online_params, adam_state, loss

# Step 83 - train_dqn_agent
def build_legal_mask(board, input_dim=9):
    legal_moves = [row*3+col for row, col in get_legal_moves(board)]
    legal_mask = np.full(9, False)
    legal_mask[legal_moves] = True
    if input_dim == 18:
        legal_mask = np.asarray(legal_mask.tolist() + legal_mask.tolist())
    return legal_mask


def train_dqn_agent(num_episodes, hidden_dim=64, gamma=0.99, lr=1e-3, batch_size=64, buffer_capacity=10000, sync_every_k=200, epsilon_start=1.0, epsilon_end=0.05, seed=0):
    """Full DQN self-play training loop. Returns dict with online_params,
    target_params, loss_history, reward_history, architecture."""
    # TODO: run num_episodes of self-play, store transitions, train with Adam.
    rng = np.random.default_rng(seed)
    architecture = build_mlp_architecture(9, hidden_dim)
    online_params = initialize_mlp_parameters(architecture, seed)
    target_params = build_target_network_copy(online_params)
    loss_history = []
    reward_history = []
    adam_state = {}

    buffer = create_replay_buffer(buffer_capacity)
    epsilon = np.linspace(epsilon_start, epsilon_end, num_episodes)
    for i in range(num_episodes):
        board, player = episode_reset_game()
        while True:
            # state = encode_board_one_hot_length_eighteen(board, player)
            state = encode_board_flat_length_nine(board, player)
            legal_mask = build_legal_mask(board)
            action = dqn_select_action(online_params, state, legal_mask, epsilon[i], rng)
            cur_state = episode_apply_action(board, action, player, player)
            # next_state = encode_board_one_hot_length_eighteen(cur_state['next_board'], player)
            next_state = encode_board_flat_length_nine(cur_state['next_board'], player)
            next_legal_mask = build_legal_mask(cur_state['next_board'])
            buffer['data'].append(dict(
                state=state,
                action=action,
                reward=cur_state['reward'],
                next_state=next_state,
                done=cur_state['done'],
                next_legal_mask=next_legal_mask
                ))
            buffer = cap_buffer_size_drop_oldest(buffer)

            player = cur_state['next_player']
            board = cur_state['next_board']
            if cur_state['done']:
                break

        reward_history.append(cur_state['reward'])
        online_params, adam_state, loss = dqn_train_step(online_params, target_params, adam_state, buffer, batch_size, gamma, lr, rng)
        target_params = sync_target_network_periodically(online_params, target_params, i, sync_every_k)
        loss_history.append(loss)

    return dict(
        online_params=online_params,
        target_params=target_params,
        loss_history=loss_history,
        reward_history=reward_history,
        architecture=architecture
    )

# Step 84 - compare_dqn_tabular_random_minimax
def compare_dqn_tabular_random_minimax(dqn_artifacts, q_table, num_games=200):
    """Round-robin evaluation among DQN, tabular Q, random, and minimax agents."""
    # TODO: play num_games for each of the six pairings, alternating X, and report rates
    rng = np.random.default_rng()

    def get_action(board, player, agent_type):
        legal_moves = [row*3+col for row,col in get_legal_moves(board)]
        match agent_type:
            case "random":
                return rng.choice(legal_moves)
            case "minimax":
                row, col = minimax_best_move(board, player)
                return row*3 + col
            case "tabular":
                state_key = canonical_board_key(flip_board_perspective(board, player))
                return greedy_argmax_over_legal_actions(q_table, state_key, legal_moves, rng)
            case "dqn":
                if dqn_artifacts['architecture']['input_dim'] == 18:
                    state = encode_board_one_hot_length_eighteen(board, player)
                else:
                    state = encode_board_flat_length_nine(board, player)
                legal_mask = build_legal_mask(board, dqn_artifacts['architecture']['input_dim'])
                return dqn_select_action(dqn_artifacts['online_params'], state, legal_mask, -1.0, rng)

    agents = ['dqn', 'tabular', 'random', 'minimax']

    outcome = {}
    for i in range(4):
        agenti = agents[i]
        for j in range(i+1,4):
            agentj = agents[j]
            result = {'wins':0, 'draws':0, 'losses':0}
            player = 1
            agent_player = player

            for _ in range(num_games):
                board, _ = episode_reset_game()
                status = 'ongoing'
                while True:
                    action = get_action(board, player, agenti)
                    cur_state = episode_apply_action(board, action, player, agent_player)

                    if not cur_state['done']:
                        board = cur_state['next_board']
                        player = cur_state['next_player']
                        action = get_action(board, player, agentj)
                        cur_state = episode_apply_action(board, action, player, agent_player)

                    board = cur_state['next_board']
                    player = cur_state['next_player']
                    if cur_state['done']:
                        break

                if cur_state['reward'] == 1:
                    result['wins']+=1
                elif cur_state['reward'] == -1:
                    result['losses']+=1
                else:
                    result['draws']+=1

                agent_player = switch_player(agent_player)
                player = agent_player

            if num_games > 0:
                result['wins']/=num_games
                result['draws']/=num_games
                result['losses']/=num_games

            outcome[agenti+"_vs_"+agentj] = result

    return outcome

# Step 85 - sarsa_on_policy_update
def sarsa_on_policy_update(q_table, state_key, action, reward, next_state_key, next_action, done, alpha, gamma):
    """Apply one on-policy SARSA update and return the updated q_table."""
    # TODO: compute the SARSA TD target using the next action actually taken, then update Q(s, a).
    q_val = get_q_value(q_table, state_key, action)
    next_q_val = get_q_value(q_table, next_state_key, next_action)
    if done:
        q_val += alpha * reward
    else:
        q_val += alpha * (reward + gamma * next_q_val - q_val)

    set_q_value(q_table, state_key, action, q_val)
    return q_table

# Step 86 - train_sarsa_agent
def train_sarsa_agent(num_episodes, alpha, gamma, initial_epsilon, min_epsilon, decay_rate, opponent_policy, rng):
    # TODO: run num_episodes of on-policy SARSA vs opponent_policy; return q_table and outcomes
    episode_outcomes = []
    q_table = initialize_q_table()
    for ep in range(num_episodes):
        epsilon = epsilon_decay_schedule(initial_epsilon, ep, min_epsilon, decay_rate)
        board, player = episode_reset_game()
        agent_player = 1
        prev_state_key, prev_action = None, None
        prev_reward = 0
        prev_done = False

        while True:
            state_key, action = episode_agent_pick_action(q_table, board, player, epsilon, rng)

            if prev_state_key is not None and prev_action is not None:
                q_table = sarsa_on_policy_update(q_table, prev_state_key, prev_action, cur_state['reward'], state_key, action, cur_state['done'], alpha, gamma)

            cur_state = episode_apply_action(board, action, player, agent_player)
            prev_state_key, prev_action = state_key, action
            prev_reward = cur_state['reward']
            prev_done = cur_state['done']

            if not cur_state['done']:
                board = cur_state['next_board']
                player = cur_state['next_player']
                action = opponent_policy(board, player, rng)
                cur_state = episode_apply_action(board, action, player, agent_player)

            board = cur_state['next_board']
            player = cur_state['next_player']
            if cur_state['done']:
                break

        if prev_state_key is not None and prev_action is not None:
            q_table = sarsa_on_policy_update(q_table, prev_state_key, prev_action, cur_state['reward'], state_key, action, cur_state['done'], alpha, gamma)
        episode_outcomes.append(cur_state['status'])

    return dict(
        q_table=q_table,
        episode_outcomes=episode_outcomes
    )

# Step 87 - reinforce_log_prob_of_action
import numpy as np

def reinforce_log_prob_of_action(logits, legal_action_mask, action):
    """Return (log_prob_of_action, full_prob_vector) under a softmax policy with illegal cells masked out."""
    # TODO: mask illegal logits, take a stable softmax, return log pi(action|s) and the probs.
    logits = mask_illegal_actions_neg_inf(logits, legal_action_mask)
    exp_logits = np.exp(logits - logits.max(axis=-1, keepdims=True))
    probs = exp_logits/exp_logits.sum(axis=-1, keepdims=True)
    return np.log(probs[action]), probs

# Step 88 - reinforce_collect_episode_returns
import numpy as np

def reinforce_collect_episode_returns(rewards, gamma):
    """Return discounted returns G_t for a REINFORCE episode as a numpy array of shape (T,)."""
    # TODO: compute G_t = r_t + gamma * G_{t+1} for each timestep and return as np.ndarray.
    n = len(rewards)
    discounted_rewards = [0.0]*(n+1)
    for i in range(n-1, -1, -1):
        discounted_rewards[i] = rewards[i] + gamma*discounted_rewards[i+1]

    return np.asarray(discounted_rewards[:n])

    # steps = np.arange(n)

    # # 2. Use broadcasting to generate a matrix of step differences (j - i)
    # # np.subtract.outer(steps, steps) yields a matrix where entry (i, j) is j - i
    # distance_matrix = np.subtract.outer(steps, steps)

    # # 3. Create the discount matrix gamma**(j - i)
    # discount_matrix = np.power(gamma, distance_matrix)

    # # 4. Mask the lower triangle to 0 (since future rewards don't affect the past)
    # discount_matrix = np.triu(discount_matrix)

    # # 5. Multiply the matrix by the rewards vector
    # return np.dot(discount_matrix, rewards)

# Step 89 - reinforce_policy_gradient_update (not yet solved)
# TODO: implement

# Step 90 - train_reinforce_agent (not yet solved)
# TODO: implement

# Step 91 - compare_value_vs_policy_learners (not yet solved)
# TODO: implement

# Step 92 - symmetry_augmented_training (not yet solved)
# TODO: implement

