from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from routers import ollama
from utils.exceptions import validation_exception_handler, general_exception_handler

app = FastAPI(title="API Ollama", version="1.0.0")

app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

app.include_router(ollama.router)

@app.get("/")
def root():
    return {"correcto": True, "mensaje": "API Ollama activa", "objeto": None}