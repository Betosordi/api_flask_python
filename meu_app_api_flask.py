from flask import Flask, request, jsonify

api_flask_python = Flask(__name__) # http://127.0.0.1:5000/dados_recebidos

# Lista para armazenar os dados em memória
dados_recebidos = []

# Rota para adicionar uma nova inspeção
@api_flask_python.route('/dados_recebidos', methods=['POST'])
def add_inspecao():
    coluna = request.get_json()  # Pega os dados enviados em JSON

    # Adiciona os dados recebidos à lista de inspeções
    dados_recebidos.append({
        'nome_do_operador': coluna['nome_do_operador'],
        'data_da_inspecao': coluna['data_da_inspecao'],
        'turno': coluna['turno'],
        'maquina': coluna['maquina'],
        'inicio_primeira_parada': coluna['inicio_primeira_parada'],
        'fim_primeira_parada': coluna['fim_primeira_parada'],
        'motivo_primeira_parada': coluna['motivo_primeira_parada'],
        'inicio_segunda_parada': coluna['inicio_segunda_parada'],
        'fim_segunda_parada': coluna['fim_segunda_parada'],
        'motivo_segunda_parada': coluna['motivo_segunda_parada'],
        'inicio_terceira_parada': coluna['inicio_terceira_parada'],
        'fim_terceira_parada': coluna['fim_terceira_parada'],
        'motivo_terceira_parada': coluna['motivo_terceira_parada'],
        'inicio_quarta_parada': coluna['inicio_quarta_parada'],
        'fim_quarta_parada': coluna['fim_quarta_parada'],
        'motivo_quarta_parada': coluna['motivo_quarta_parada'],
        'inicio_quinta_parada': coluna['inicio_quinta_parada'],
        'fim_quinta_parada': coluna['fim_quinta_parada'],
        'motivo_quinta_parada': coluna['motivo_quinta_parada'],
        'quantidade_refugo': coluna['quantidade_refugo'],
        'produto_produzido': coluna['produto_produzido'],
        'quantidade_produzida': coluna['quantidade_produzida']
    })

    #return jsonify({'message': 'Inspeção adicionada com sucesso!'}), 201

# Rota para listar todas as inspeções
@api_flask_python.route('/dados_recebidos', methods=['GET'])
def get_inspecoes():
    return jsonify(dados_recebidos), 200

if __name__ == '__main__':
    api_flask_python.run(debug=True)
###################################################################################################### API

