from pydantic import BaseModel
from typing import Any

class APIResponse(BaseModel):
    correcto: bool
    mensaje: str
    objeto: Any = None