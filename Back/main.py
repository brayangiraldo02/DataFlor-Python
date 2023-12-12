from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base

from models.flowershops import FlowerShop
from models.providers import Provider
from models.products import Product
from models.inventory import Inventory
from models.users import User

app = FastAPI()

app.title = "My flower shop inventory application."
app.version = "0.0.1"

# Crea las tablas antes de iniciar el servidor
Base.metadata.create_all(bind=engine)

@app.get("/", tags=["Main"])
def message():
    return HTMLResponse(content="<h1>¡Hola Mundo!</h1>")
