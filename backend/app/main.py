from fastapi import FastAPI
from database import engine
from models import Base
from routers.traffic import router as traffic_router
from routers.pollution import router as pollution_router
from routers.ai import router as ai_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(traffic_router, prefix="/traffic")
app.include_router(pollution_router, prefix="/pollution")
app.include_router(ai_router, prefix="/ai")

@app.get("/")
def root():
    return {"message": "Backend de MyCity Dashboard listo!"}