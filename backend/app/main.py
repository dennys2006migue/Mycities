from fastapi import FastAPI
from .database import engine
from .models import Base
from .routers import traffic, pollution, incidents, ai, satellite

app = FastAPI()

Base.metadata.create_all(bind=engine)  # Crea tablas en DB

app.include_router(traffic.router, prefix="/traffic")
app.include_router(pollution.router, prefix="/pollution")
app.include_router(incidents.router, prefix="/incidents")
app.include_router(ai.router, prefix="/ai")
app.include_router(satellite.router, prefix="/satellite")

@app.get("/")
def root():
    return {"message": "Backend de MyCity Dashboard listo!"}