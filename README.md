# Parcial01_ValentinaCastro

## 1) Clonar o copiar el proyecto
cd <carpeta-del-proyecto>

## 2) (opcional) Crear y activar un virtualenv
python -m venv .venv
## Linux/Mac:
source .venv/bin/activate
## Windows (PowerShell):
.\.venv\Scripts\Activate.ps1

## 3) Instalar dependencias
pip install -r requirements.txt

## 4) Ejecutar la app
python app.py

## 5) Probar
http://127.0.0.1:8000/api/factorial/(número)

## 6) Resultado esperado
{
  "numero": (número ingresado en la url),
  "factorial": "factorial del número ingresado en la url",
  "paridad_factorial": "paridad del número ingresado en la url"
}

## ¿Cómo se modificaría el diseño si este microservicio tuviera que comunicarse con otro servicio que almacena el historial de cálculos en una base de datos externa?

Diseñaría el microservicio para responder rápido y, en segundo plano, 
enviar el resultado al servicio de historial (bajo acoplamiento). 
Ese envío sería asíncrono con un calculation_id (UUID) para idempotencia, más timeouts y 
reintentos con backoff para tolerar fallos del historial. 
La configuración (URL, credenciales, tiempos) 
iría en variables de entorno, y protegería la llamada con token. 
Agregaría logs y un ID de correlación para poder seguir cada cálculo. 
Con esto, el camino crítico queda corto, el sistema escala mejor y el historial se guarda con 
consistencia eventual sin bloquear al usuario.


