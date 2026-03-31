from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.response import APIResponse
from schemas.ollama import OllamaRequest
from utils.ollama_engine import consultar_modelo

router = APIRouter(
    prefix="/ollama",
    tags=["Ollama"]
)

@router.post("/consultar", response_model=APIResponse)
def consultar(request: OllamaRequest):
    try:
        resultado = consultar_modelo(request.mensaje, request.prompt_sistema)
        return APIResponse(
            correcto=True,
            mensaje="Consulta ejecutada correctamente",
            objeto=resultado
        )
    except Exception as e:
        return JSONResponse(
            status_code=200,
            content={
                "correcto": False,
                "mensaje": f"Error al consultar el modelo: {str(e)}",
                "objeto": None
            }
        )