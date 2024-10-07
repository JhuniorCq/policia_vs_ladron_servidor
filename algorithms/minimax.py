from utils.constants import UP, DOWN, LEFT, RIGHT, ROLES
from utils.manhattan_distance import manhattan_distance
from utils.move_player import move_player

def evaluation_function(pos_maquina, pos_objetivo):
    if pos_maquina == pos_objetivo:
        return -1000
    
    distancia = manhattan_distance(pos_maquina, pos_objetivo)

    return distancia

def minimax(profundidad, rol, pos_maquina, pos_objetivo):
    # Caso base: Llegamos a la profundidad 0 o la Máquina alcanzó su Objetivo
    if profundidad == 0 or pos_maquina == pos_objetivo:
        return evaluation_function(pos_maquina, pos_objetivo)
    
    if rol == ROLES["POLICE"]: # Rol "Policía"
        mejor_evaluacion = float("inf") # El Policía quiere minimizar
        
        for direccion in [UP, DOWN, LEFT, RIGHT]:
            pos_maquina_temp = pos_maquina.copy() # Copia temporal del policía
            move_player(pos_maquina_temp, direccion) # Simulamos el movimiento
            evaluacion = minimax(profundidad - 1, ROLES["THIEF"], pos_maquina_temp, pos_objetivo)
            mejor_evaluacion = min(mejor_evaluacion, evaluacion) # Tomamos la mejor evaluación
        return mejor_evaluacion
    else: # Rol "Ladrón"
        mejor_evaluacion = float("-inf") # El Ladrón quiere maximizar
        
        for direccion in [UP, DOWN, LEFT, RIGHT]:
            pos_objetivo_temp = pos_objetivo.copy() # Copia temporal del ladrón
            move_player(pos_objetivo_temp, direccion) # Simulamos el movimiento
            evaluacion = minimax(profundidad - 1, ROLES["POLICE"], pos_maquina, pos_objetivo_temp)
            mejor_evaluacion = max(mejor_evaluacion, evaluacion) # Tomamos la mejor evaluación
        return mejor_evaluacion