from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.endpoints import restaurants, reservations, chat
from app.core.config import settings
from app.db.session import engine
from app.db.session import Base
# Import all models to ensure they are registered with Base
from app.models import restaurant, reservation 

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Create tables on startup
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(restaurants.router, prefix=f"{settings.API_V1_STR}/restaurants", tags=["restaurants"])
app.include_router(reservations.router, prefix=f"{settings.API_V1_STR}/reservations", tags=["reservations"])
app.include_router(chat.router, prefix=f"{settings.API_V1_STR}/chat", tags=["chat"])

@app.get("/")
def root():
    return {"message": "Welcome to RAG Resto API - Restaurant Service"}
