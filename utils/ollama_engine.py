import ollama
from ollama import ResponseError

MODELO = "qwen2.5:7b"

def consultar_modelo(mensaje: str, prompt_sistema: str) -> dict:
    try:
        respuesta = ollama.chat(
            model=MODELO,
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": mensaje}
            ]
        )

        contenido = respuesta["message"]["content"]
        tokens_entrada = respuesta.get("prompt_eval_count", 0)
        tokens_salida = respuesta.get("eval_count", 0)

        return {
            "respuesta": contenido,
            "modelo": MODELO,
            "tokens": {
                "entrada": tokens_entrada,
                "salida": tokens_salida,
                "total": tokens_entrada + tokens_salida
            }
        }

    except ResponseError as e:
        raise Exception(f"Ollama rechazó la solicitud: {e.error} (status: {e.status_code})")
    except ConnectionError:
        raise Exception("No se pudo conectar con Ollama — verifica que esté corriendo en el puerto 11434")
    except Exception as e:
        raise Exception(f"Error en el modelo {MODELO}: {str(e)}")