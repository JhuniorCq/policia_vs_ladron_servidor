from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from algorithms.best_first import best_first
from algorithms.minimax import minimax
from algorithms.non_deterministic import non_deterministic
from utils.move_player import move_player
from utils.constants import UP, DOWN, LEFT, RIGHT, ROLES
from typing import List

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class BestFirstData(BaseModel):
    posicion_jugador: List[int]
    posicion_objetivo: List[int]
    rol: str
    pos_policia: List[int]
    pos_ladron: List[int]
    
    
class MinimaxData(BaseModel):
    posicion_jugador: List[int] # Policía
    posicion_objetivo:List[int] # Ladrón
    profundidad: int

@app.post("/best-first")
async def get_best_first(data: BestFirstData):
    return {
        "direction": best_first(data.posicion_jugador, data.posicion_objetivo, data.rol, data.pos_policia, data.pos_ladron)
    }

@app.post("/minimax")
async def get_minimax(data: MinimaxData):
    
    mejor_evaluacion = float("inf")
    mejor_movimiento = None
    
    for direccion in [UP, DOWN, LEFT, RIGHT]:
        posicion_objetivo_temp = data.posicion_objetivo.copy()
        posicion_jugador_temp = data.posicion_jugador.copy()
        move_player(posicion_jugador_temp, direccion)
        
        evaluacion = minimax(data.profundidad, ROLES["THIEF"], posicion_jugador_temp, posicion_objetivo_temp)
        
        if evaluacion < mejor_evaluacion:
            mejor_evaluacion = evaluacion
            mejor_movimiento = direccion
    
    return {
        "direction": mejor_movimiento
    }

@app.get("/non-deterministic")
async def get_non_deterministic():
    return {
        "direction": non_deterministic()
    }
    
# TODO: ACTIVAR el Entorno Virtual