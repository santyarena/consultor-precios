from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
@app.route("/")
def home():
    return "Servidor funcionando"


app = Flask(__name__)

@app.route("/consultar", methods=["POST"])
def consultar():
    data = request.get_json()

    if not data or "producto" not in data:
        return jsonify({"error": "Falta el campo 'producto'"}), 400

    producto = data["producto"]
    url = f"https://www.hardgamers.com.ar/search?text={producto}"

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Buscar el primer precio
        precio_tag = soup.select_one("h2.product-price")

        if precio_tag:
            precio = precio_tag.text.strip()
        else:
            precio = "No encontrado"

        return jsonify({
            "producto": producto,
            "precio": precio
        })

    except Exception as e:
        return jsonify({
            "error": str(e),
            "producto": producto,
            "precio": "Error al buscar"
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
