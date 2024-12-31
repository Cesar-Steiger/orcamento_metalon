from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Função para calcular o orçamento
def calcular_orcamento(data):
    tipo = data.get("tipo")
    comprimento = float(data.get("comprimento", 0))
    largura = float(data.get("largura", 0))
    preco_por_metro = float(data.get("preco_por_metro", 0))
    quantidade = int(data.get("quantidade", 0))

    # Calcula o custo total
    custo_total = preco_por_metro * comprimento * quantidade

    # Retorna a resposta em formato dicionário
    return {
        "tipo": tipo,
        "dimensoes": f"{comprimento}m x {largura}cm",
        "quantidade": quantidade,
        "preco_por_metro": f"R${preco_por_metro:.2f}",
        "custo_total": f"R${custo_total:.2f}"
    }

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Recebe os dados do formulário
        data = request.form
        resultado = calcular_orcamento(data)
        return render_template("resultado.html", resultado=resultado)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
