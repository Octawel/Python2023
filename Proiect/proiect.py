import copy
import random

def get_init_state():
    return {'available': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'player': [], 'bot': []}

def is_final_state(state):
    player, bot = state['player'], state['bot']
    if len(player) < 3 and len(bot) < 3:
        return False

    if len(player) >= 3:
        for i in range(0, len(player)):
            for j in range(i + 1, len(player)):
                for k in range(j + 1, len(player)):
                    if player[i] + player[j] + player[k] == 15:
                        return 'player'

    if len(bot) >= 3:
        for i in range(0, len(bot)):
            for j in range(i + 1, len(bot)):
                for k in range(j + 1, len(bot)):
                    if bot[i] + bot[j] + bot[k] == 15:
                        return 'bot'

    return False

def is_valid_transition(state, value):
    return value in state['available']

def transition(state, value, turn):
    new_state = copy.deepcopy(state)
    if not is_valid_transition(new_state, value):
        return False

    if turn in ['player', 'bot']:
        new_state[turn].append(value)
        new_state['available'].remove(value)

    return new_state

def score_heuristic(state):
    final_state = is_final_state(state)
    if final_state == 'player':
        return -1000
    elif final_state == 'bot':
        return 1000
    else:
        return len(state['available'])

def minmax(state, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or is_final_state(state):
        return score_heuristic(state), None

    if maximizingPlayer:
        maxEval = float("-inf")
        best_move = None
        for move in state['available']:
            evaluation, _ = minmax(transition(state, move, 'bot'), depth - 1, alpha, beta, False)
            if evaluation > maxEval:
                maxEval = evaluation
                best_move = move
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return maxEval, best_move
    else:
        minEval = float("inf")
        best_move = None
        for move in state['available']:
            evaluation, _ = minmax(transition(state, move, 'player'), depth - 1, alpha, beta, True)
            if evaluation < minEval:
                minEval = evaluation
                best_move = move
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return minEval, best_move

def bot_move(state):
    _, move = minmax(state, 2, float("-inf"), float("inf"), True)
    return move

def print_board(state):
    for i in range(1, 10):
        if i in state['player']:
            print('X', end=' ')
        elif i in state['bot']:
            print('O', end=' ')
        else:
            print('_', end=' ')

        if i % 3 == 0:
            print()

def get_difficulty():
    while True:
        try:
            difficulty = int(input("Selectează dificultatea (1-Ușor, 2-Mediu, 3-Greu): "))
            if 1 <= difficulty <= 3:
                return difficulty
            else:
                print("Input invalid. Te rog introdu un număr între 1 și 3.")
        except ValueError:
            print("Input invalid. Te rog introdu un număr între 1 și 3.")

def player_move(state):
    try:
        choice = int(input("Jucătorule, alege o poziție (1-9): "))
        while not is_valid_transition(state, choice):
            print("Mutare invalidă. Te rog alege o poziție disponibilă.")
            choice = int(input("Jucătorule, alege o poziție (1-9): "))
        return choice
    except ValueError:
        print("Input invalid. Te rog introdu un număr între 1 și 9.")
        return player_move(state)

def play_game():
    total_score = {'player': 0, 'bot': 0, 'egal': 0}

    while True:
        state = get_init_state()
        turn = 'player'
        difficulty = get_difficulty()

        print("Hai să jucăm X și 0!")
        print_board(state)

        while not is_final_state(state) and state['available']:
            if turn == 'player':
                choice = player_move(state)
                state = transition(state, choice, turn)
                turn = 'bot'
            elif turn == 'bot':
                if difficulty == 1:
                    choice = random.choice(state['available'])
                elif difficulty == 2:
                    if random.randint(1, 2) == 1:
                        choice = random.choice(state['available'])
                    else:
                        choice = bot_move(state)
                elif difficulty == 3:
                    choice = bot_move(state)
                
                print(f"Bot alege: {choice}")
                state = transition(state, choice, turn)
                turn = 'player'

            print_board(state)

        winner = is_final_state(state)
        if winner == 'player':
            print("Jucătorul câștigă!")
            total_score['player'] += 1
        elif winner == 'bot':
            print("Botul câștigă!")
            total_score['bot'] += 1
        else:
            print("Egal!")
            total_score['egal'] += 1

        print(f"Scor total - Jucător: {total_score['player']}, Bot: {total_score['bot']}, Egal: {total_score['egal']}")

        play_again = input("Vrei să joci din nou? (da/nu): ").lower()
        if play_again != 'da':
            print("Mulțumim pentru joc!")
            break

# Începe jocul
play_game()

