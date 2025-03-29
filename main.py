from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "API funcionando correctamente."

@app.route("/consultar", methods=["POST"])
def consultar():
    data = request.get_json()
    producto = data.get("producto", "").lower()

    # Simulación de precios
    precios_simulados = {
        "5600g": "$134.999",
        "5700g": "$144.999",
        "5800x": "$164.999"
    }

    precio = precios_simulados.get(producto, "Producto no encontrado")

    return jsonify({
        "producto": producto,
        "precio": precio
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(debug=False, host="0.0.0.0", port=port)
