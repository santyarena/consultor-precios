from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/consultar", methods=["POST"])
def consultar():
    data = request.get_json()
    producto = data.get("producto", "Desconocido")
    return jsonify({
        "producto": producto,
        "precio": "$123456"  # Simulado por ahora
    })

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=3000)

