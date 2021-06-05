from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_clientes, rotas_servicos

app = FastAPI()

# CORS
origins = ['http://localhost:3000', 
            'http://myapp.vercel.com']

app.add_middleware(CORSMiddleware, 
                    allow_origins=origins,
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"],)

# Rotas Clientes
app.include_router(rotas_clientes.router)
# Rotas Serviços
app.include_router(rotas_servicos.router)