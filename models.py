from pydantic import BaseModel, EmailStr

class Formulario(BaseModel):
    nombre: str
    email: EmailStr
    subject: str
    telefono: str
    mensaje: str





