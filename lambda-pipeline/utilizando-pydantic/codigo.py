usuario = {"nome": "João", "email": "joao@email.com", "investimentos": 10000}

print(usuario)

usuario["investimentos"] += 1000

print(usuario)

from pydantic import BaseModel, EmailStr


class Usuario(BaseModel):
    nome: str
    email: EmailStr
    investimentos: float

usuario = Usuario(nome="João", email="joao@email.com", investimentos=10000)
print(usuario)
print(usuario.email)

usuario.investimentos += 1000

print(usuario)

print(usuario.model_dump())
usuario_json = usuario.model_dump_json()
print(usuario_json)