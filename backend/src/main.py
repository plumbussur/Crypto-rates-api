from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.router import router as router_crypto

app = FastAPI()

app.include_router(router_crypto)



