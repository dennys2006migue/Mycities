from fastapi import FastAPI
from .database import engine
from .models import Base
from .routers import traffic, pollution, ai

app = FastAPI()

# Crea todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluye los routers con sus prefijos
app.include_router(traffic.router, prefix="/traffic")
app.include_router(pollution.router, prefix="/pollution")
app.include_router(ai.router, prefix="/ai")

# Endpoint raíz para verificar que el backend está funcionando
@app.get("/")
def root():
    return {"message": "Backend de MyCity Dashboard listo!"}