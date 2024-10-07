from utils.constants import UP, DOWN, LEFT, RIGHT, ROWS, COLUMNS

def move_player(jugador, direccion):
    if direccion == UP and jugador[0] > 0:  # UP
        jugador[0] -= 1
        return True
    elif direccion == DOWN and jugador[0] < ROWS - 1:  # DOWN
        jugador[0] += 1
        return True
    elif direccion == LEFT and jugador[1] > 0:  # LEFT
        jugador[1] -= 1
        return True
    elif direccion == RIGHT and jugador[1] < COLUMNS - 1:  # RIGHT
        jugador[1] += 1
        return True
    else:
        return False