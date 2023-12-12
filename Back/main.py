from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from config.database import engine, Base

app = FastAPI()

app.title = "My flower shop inventory application."
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)

@app.get("/", tags=["Main"])
def message():
  return HTMLResponse(content = "<h1>¡Hola Mundo!</h1>")