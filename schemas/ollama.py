from pydantic import BaseModel

class OllamaRequest(BaseModel):
    mensaje: str
    prompt_sistema: str = "Eres un asistente útil que responde de forma clara y concisa."