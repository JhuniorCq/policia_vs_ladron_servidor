from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from algorithms.best_first import best_first
from algorithms.minimax import minimax
from algorithms.non_deterministic import non_deterministic
from utils.constants import ROLES

app = FastAPI()

# class PlayerData(BaseModel):
#     posicion_jugador: list[int]
#     posicion_obketivo: list[int]
#     rol: str
#     pos_policia: list[int]
#     pos_ladron: list[int]
#     profundidad: int = 0
    
class BestFirstData(BaseModel):
    posicion_jugador: list[int]
    posicion_objetivo: list[int]
    rol: str
    pos_policia: list[int]
    pos_ladron: list[int]
    
@app.post("/best-first")
async def get_best_first(data: BestFirstData):
    if data.rol not in ROLES.values():
        raise HTTPException(status_code=400, detail="Rol no válido")
    
    return {
        "direction": best_first(data.posicion_jugador, data.posicion_objetivo, data.rol, data.pos_policia, data.pos_ladron)
    }

# @app.post("/minimax")
# async def get_minimax(data: PlayerData):
#     if data.rol not in ROLES.values():
#         pass

@app.get("/non-deterministic")
async def get_non_deterministic():
    return {
        "direction": non_deterministic()
    }
    
# TODO: ACTIVAR el Entorno Virtual