import numbers
from turtle import st
from pydantic import BaseModel
from typing import Optional

class Cuenta(BaseModel):
    id: Optional[int]
    cedula: str
    cuenta: int
    telefono: str
    factura: int
    monto: int
    moneda: str

