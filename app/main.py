from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.db.connection import init_db
from app.routes import auth, reports

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        init_db()
        print("🚀 Base de datos inicializada correctamente (Tablas history y users verificadas)")
    except Exception as e:
        print(f"❌ Error al conectar o inicializar la base de datos: {e}")
    yield
    print("🛑 Servidor FastAPI apagándose limpio.")

app = FastAPI(
    title="The Dutch Boy API",
    description="Backend modular para la gestión de transacciones y autenticación",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(reports.router)

@app.get("/", summary="Ruta raíz de bienvenida")
def read_root():
    return {"message": "Bienvenido a la API de The Dutch Boy"}