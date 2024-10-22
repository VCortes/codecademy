import os
from flask import Flask
from factorial import factorial
import debugpy


app = Flask(__name__)


@app.route("/api", methods=["GET"])
def hello_world():
    return {"message": "Olá, mundo!"}


@app.route("/api/factorial/<int:n>", methods=["GET"])
def get_factorial(n):
    return {"factorial": factorial(n)}


if __name__ == "__main__":
    # Configurar o debugpy para depuração remota
    debugpy.listen(("0.0.0.0", 5678))
    print("Esperando para se conectar ao depurador...")
    debugpy.wait_for_client()  # Aguarda a conexão do depurador

    port = int(os.environ.get("PORT", 5000))  # Usa a porta do ambiente ou 5000
    app.run(host="0.0.0.0", port=port)
