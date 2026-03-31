from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errores = exc.errors()
    campos = ", ".join([f"'{e['loc'][-1]}'" for e in errores])
    return JSONResponse(
        status_code=200,
        content={
            "correcto": False,
            "mensaje": f"Campos requeridos faltantes o incorrectos: {campos}",
            "objeto": None
        }
    )


async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=200,
        content={
            "correcto": False,
            "mensaje": f"Error interno del servidor: {str(exc)}",
            "objeto": None
        }
    )