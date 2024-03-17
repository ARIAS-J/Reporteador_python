from pydantic import BaseModel


class ContratoAfiliacion(BaseModel):
    nombre: str
    apellido: str
    ocupacion: str
    salario: int
