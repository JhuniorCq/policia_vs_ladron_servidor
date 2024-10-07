import random
from utils.constants import UP, DOWN, LEFT, RIGHT

def non_deterministic(): 
    movimiento = random.choice([UP, DOWN, LEFT, RIGHT])
    return movimiento