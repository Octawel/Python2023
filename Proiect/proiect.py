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