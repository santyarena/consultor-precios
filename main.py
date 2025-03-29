from flask import Flask, request, jsonify

app = Flask(__name__)  # ESTA LÍNEA ES CLAVE

@app.route("/")
def home():
    return "¡API funcionando!"

@app.route("/consultar", methods=["POST"])
def consultar_precio():
    data = request.get_json()
    producto = data.get("producto", "")
    
    # Por ahora simulemos la respuesta:
    return jsonify({
        "producto": producto,
        "precio": "$174.899"
    })
