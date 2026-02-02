# api-y-ataque-de-seguridad
un sistema de autenticación intencionalmente vulnerable para demostrar ataques de fuerza bruta
Lenguaje: Python 3.x

Framework: FastAPI

Modelado de Datos: SQLModel
Estructura del Repositorio
main.py: Código fuente de la API con base de datos quemada.

ataque.py: Script de automatización de ataque de fuerza bruta.

requirements.txt: Dependencias del proyecto

Guía de Instalación y Ejecución
Clonar el repositorio:


git clone -direccion-https...
cd -nombre-del-repo

Instalar dependencias:

Bash
pip install -r requirements.txt

Iniciar el Servidor Terminal 1:

Bash
fastapi dev fastapi.py

Ejecutar el Ataque Terminal 2:

Bash
python bruteforce.py

Funcionalidades de la API (6 Puntos)
La API implementa los siguientes endpoints siguiendo la rúbrica académica:

POST /users: Registro de nuevos usuarios.

GET /users: Listado de usuarios registrados.

GET /users/{id}: Consulta de información por ID.

PUT /users/{id}: Actualización de perfiles (restringido para contraseñas).

DELETE /users/{id}: Eliminación de registros.

POST /login: Punto de acceso para validación de credenciales.

Pruebas fastapi
<img width="1271" height="1668" alt="Captura de pantalla 2026-02-01 221635" src="https://github.com/user-attachments/assets/742b58ca-5bfe-4cc0-ae76-17569ac6721b" />

Codigo de ataque 
<img width="2477" height="1343" alt="Captura de pantalla 2026-02-01 221731" src="https://github.com/user-attachments/assets/6af5cd49-9f15-417b-9061-c89a68d8a8f0" />

comando para ejecutar ataque
<img width="463" height="160" alt="Captura de pantalla 2026-02-01 221916" src="https://github.com/user-attachments/assets/2b858836-ee65-4631-b0d9-a953c2921c1c" />

ataque ejecutandose 
<img width="2002" height="531" alt="Captura de pantalla 2026-02-01 221746" src="https://github.com/user-attachments/assets/b49e41c2-5862-4b85-b0fd-f9cc5d5788db" />

ataque exitoso
<img width="581" height="142" alt="Captura de pantalla 2026-02-01 221851" src="https://github.com/user-attachments/assets/1de2d82a-dc41-429b-8be1-6f0cfa4fa3d6" />





