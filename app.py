from flask import Flask, jsonify, request
import math

app = Flask(__name__)

@app.get("/api/factorial/<n>")
def factorial_info(n):
    try:
        num = int(n)
    except ValueError:
        return jsonify(error="El parámetro debe ser un entero."), 400

    if num < 0:
        return jsonify(error="No existe factorial para números negativos."), 400

    fact = math.factorial(num)
    paridad = "par" if (num % 2 == 0) else "impar"

    return jsonify(
        numero=num,
        factorial=str(fact),
        paridad_factorial=paridad
    )

@app.get("/")
def root():
    return jsonify(mensaje="Usa /api/factorial/<numero>"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
