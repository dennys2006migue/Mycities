from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def get_traffic():
    return {"status": "Módulo de tráfico listo"}  # Agrega lógica con TomTom después