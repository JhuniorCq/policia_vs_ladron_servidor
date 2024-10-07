import heapq
from utils.constants import ROWS, COLUMNS, ROLES
from utils.manhattan_distance import manhattan_distance

def best_first(posicion_jugador, posicion_objetivo, rol, pos_policia, pos_ladron):
    # Posibles direcciones de movimiento
    direcciones = {
        'w': (-1, 0),
        's': (1, 0),
        'a': (0, -1),
        'd': (0, 1)
    }
    
    # Lista de prioridad con heapq
    movimientos = []
    movimientos_secundarios = []
    
    # Evaluamos cada movimiento posible
    for direccion, (dx, dy) in direcciones.items():
        nueva_posicion = [posicion_jugador[0] + dx, posicion_jugador[1] + dy]
        
        # Aseguramos que la nueva posición esté dentro de los límites del tablero
        if 0 <= nueva_posicion[0] < ROWS and 0 <= nueva_posicion[1] < COLUMNS:
            if rol == ROLES["THIEF"]: # Ladrón
                distancia_actual_policia = manhattan_distance(pos_ladron, pos_policia)
                # Si la distancia de separación con el policía es de 4 casilleros
                if distancia_actual_policia <= 5:
                    distancia_nueva_policia = manhattan_distance(nueva_posicion, pos_policia)

                    if distancia_nueva_policia <= distancia_actual_policia:
                        distancia = manhattan_distance(nueva_posicion, posicion_objetivo)
                        heapq.heappush(movimientos_secundarios, (distancia, nueva_posicion, direccion))
                        continue
            
            # Calculamos la heurística (distancia al ladrón / casa más cercana)
            distancia = manhattan_distance(nueva_posicion, posicion_objetivo)
            
            # Añadimos la nueva posición a la lista de prioridades
            heapq.heappush(movimientos, (distancia, nueva_posicion, direccion))
    
    if len(movimientos) != 0:
        # Retornamos el mejor movimiento (el de menor distancia) -> mejor_movimiento es una TUPLA
        mejor_movimiento = heapq.heappop(movimientos)
        return mejor_movimiento[2] # Nueva posición y Dirección
    else:
        mejor_movimiento = heapq.heappop(movimientos_secundarios)
        return mejor_movimiento[2] # Nueva posición y Dirección