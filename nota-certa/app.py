# app.py
from flask import Flask
from factorial import factorial

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello_world():
    return {'message': 'Olá, mundo!'}

@app.route('/api/factorial/<int:n>', methods=['GET'])
def get_factorial(n):
    return {'factorial': factorial(n)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
