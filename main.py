from fastapi import FastAPI

from endpoints import generar_reporte

app = FastAPI()


@app.get('/')
def home():
    return 'Hola Mundo'


# Generar Reporte router
app.include_router(generar_reporte.router)
