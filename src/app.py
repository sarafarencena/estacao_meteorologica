from flask import Flask, request, jsonify, render_template
from database import (
    init_db, inserir_leitura, listar_leituras,
    buscar_leitura, atualizar_leitura, deletar_leitura, estatisticas
)

app = Flask(__name__)

with app.app_context():
    init_db()

# Painel principal
@app.route('/')
def index():
    leituras = listar_leituras(limite=10)
    return render_template('index.html', leituras=leituras)

# Listar todas as leituras
@app.route('/leituras', methods=['GET'])
def listar():
    formato = request.args.get('formato')
    leituras = listar_leituras(limite=None) # rota para histórico ilimitado de leituras
    if formato == 'json':
        return jsonify([dict(l) for l in leituras])
    return render_template('historico.html', leituras=leituras)

# Criar nova leitura (Arduino)
@app.route('/leituras', methods=['POST'])
def criar():
    dados = request.get_json()
    if not dados:
        return jsonify({'erro': 'JSON inválido'}), 400
    if 'temperatura' not in dados or 'umidade' not in dados:
        return jsonify({'erro': 'Campos obrigatórios ausentes'}), 400
    id_novo = inserir_leitura(
        dados['temperatura'],
        dados['umidade'],
        dados.get('pressao')
    )
    return jsonify({'id': id_novo, 'status': 'criado'}), 201

# Detalhe de uma leitura
@app.route('/leituras/<int:id>', methods=['GET'])
def detalhe(id):
    leitura = buscar_leitura(id)
    if not leitura:
        return jsonify({'erro': 'Não encontrado'}), 404
    return render_template('editar.html', leitura=leitura)

# Atualizar leitura
@app.route('/leituras/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    if not dados:
        return jsonify({'erro': 'JSON inválido'}), 400
    leitura = buscar_leitura(id)
    if not leitura:
        return jsonify({'erro': 'Não encontrado'}), 404
    atualizar_leitura(id, dados)
    return jsonify({'status': 'atualizado'})

# Deletar leitura
@app.route('/leituras/<int:id>', methods=['DELETE'])
def deletar(id):
    leitura = buscar_leitura(id)
    if not leitura:
        return jsonify({'erro': 'Não encontrado'}), 404
    deletar_leitura(id)
    return jsonify({'status': 'removido'})

# Estatísticas
@app.route('/api/estatisticas', methods=['GET'])
def stats():
    dados = estatisticas()
    return jsonify(dict(dados))

if __name__ == '__main__':
    app.run(debug=True)