from flask import Flask, request, jsonify
from main import calcular_orcamento  # Importa a função do arquivo main.py

app = Flask(__name__)

@app.route('/orcamento', methods=['POST'])
def orcamento_endpoint():
    data = request.json  # Recebe os dados enviados em formato JSON
    resposta = calcular_orcamento(data)  # Chama a função de cálculo do main.py
    return jsonify(resposta)  # Retorna o resultado como JSON

if __name__ == '__main__':
    app.run(debug=True)
