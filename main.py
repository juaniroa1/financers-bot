from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Pregunta(BaseModel):
    mensaje: str

@app.post("/preguntar")
async def responder(pregunta: Pregunta):
    texto = pregunta.mensaje.lower()

    if "abrir una empresa" in texto or "llc" in texto:
        return {"respuesta": "Podés abrir una LLC 100% online desde tu país. ¿Querés que te pase requisitos y costos?"}
    elif "impuesto" in texto or "irs" in texto:
        return {"respuesta": "Si tenés una LLC en EE.UU., debés declarar todos los años. ¿Sabés si es Single Member o Multi Member?"}
    elif "cuenta" in texto or "bancaria" in texto:
        return {"respuesta": "Necesitás una LLC + EIN para abrir cuentas en Mercury o Relay. Te puedo ayudar."}
    else:
        return {"respuesta": "¿Querés que agendemos una llamada para asesorarte mejor? https://calendly.com/financers/llamada"}
