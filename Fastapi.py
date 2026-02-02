from fastapi import FastAPI, Response
from sqlmodel import SQLModel
from typing import Optional

app = FastAPI()

#  MODELO USER 
class Usuario(SQLModel):
    id: Optional[int] = None
    username: str
    password: str
    email: Optional[str] = None
    is_active: bool = True

#  BASE DE DATOS QUEMADA 
bd_usuarios = {
    1: {"id": 1, "username": "admin", "password": "password123", "email": "admin@uide.edu.ec", "is_active": True},
    2: {"id": 2, "username": "victima", "password": "ac", "email": "victima@uide.edu.ec", "is_active": True},
}

contador_id = max((usua["id"] for usua in bd_usuarios.values()), default=0) + 1

@app.get("/")
def inicio():
    return {"mensaje": "API creada por Sir_Josue"}


#  POST /users  Crear usuario
@app.post("/users", status_code=201)
def crear_usuario(username: str, password: str, email: Optional[str] = None):
    global contador_id
    nuevo = {"id": contador_id, "username": username, "password": password, "email": email, "is_active": True}
    bd_usuarios[contador_id] = nuevo
    contador_id += 1
    return {"mensaje": "Usuario creado", "id": nuevo["id"]}

#  GET /users  Listar usuarios
@app.get("/users")
def listar_usuarios():
    return [
        {"id": usua["id"], "username": usua["username"], "email": usua["email"], "is_active": usua["is_active"], "password": usua["password"]} 
        for usua in bd_usuarios.values()
    ]

#  GET /users/{id}  Obtener usuario
@app.get("/users/{id_usuario}")
def obtener_usuario(id_usuario: int, respuesta: Response):
    usua = bd_usuarios.get(id_usuario)
    if not usua:
        respuesta.status_code = 404
        return {"error": "No encontrado"}
    return usua
#  PUT /users/{id} — Actualizar excepto password
@app.put("/users/{id_usuario}")
def actualizar_usuario(id_usuario: int, username: Optional[str] = None, email: Optional[str] = None):
    usua = bd_usuarios.get(id_usuario)
    if not usua: return {"error": "No encontrado"}
    if username: usua["username"] = username
    if email: usua["email"] = email
    return {"mensaje": "Actualizado"}

# DELETE /users/{id}  Eliminar usuario
@app.delete("/users/{id_usuario}")
def eliminar_usuario(id_usuario: int):
    if id_usuario in bd_usuarios:
        del bd_usuarios[id_usuario]
        return {"mensaje": "Eliminado"}
    return {"error": "No existe"}

# POST /login — Autenticar 
@app.post("/login")
def login(nombre_usuario: str, contrase: str, respuesta: Response):
    for usua in bd_usuarios.values():
        if usua["username"] == nombre_usuario and usua["password"] == contrase:
            return {"mensaje": "Login exitoso"}
    respuesta.status_code = 401
    return {"mensaje": "Login fallido"}