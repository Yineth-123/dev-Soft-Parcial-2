from fastapi import FastAPI
from App_Parcial.controller.App_Parcial_controller import router

app = FastAPI(title="Gestor de Tareas - Parcial")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente. Visita /docs para probar"}

