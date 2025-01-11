from flask import Blueprint, jsonify, request

# Cria a Blueprint
product_bp = Blueprint('product_bp', __name__, url_prefix='/products')

# Lista de produtos simulada
produtos = [
    {
        'name': "Produto-1",
        'price': 20
    },
    {
        'name': "Produto-2",
        'price': 100
    }
]

# Rota para listar todos os produtos
@product_bp.route('/', methods=['GET'])
def listar_produtos():
    return jsonify({"produtos": produtos}), 200

# Rota para buscar um produto por ID
@product_bp.route('/<string:id>', methods=['GET'])
def obter_produto(id):
    for produto in produtos:
        if produto['name'] == id:  # Corrigido para acessar o valor pela chave do dicionário
            return jsonify(produto), 200
    return jsonify({'error': 'Produto não encontrado'}), 404


# Rota para criar um novo produto
@product_bp.route('/', methods=['POST'])
def criar_produto():
    produto = request.get_json()
    produtos.append(produto)
    return jsonify({"message": "Produto cadastrado com sucesso"}), 201

# Rota para atualizar um produto por ID
@product_bp.route('/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    produto = request.get_json()
    for p in produtos:
        if p['id'] == id:
            p.update(produto)
            return jsonify({"message": "Produto atualizado com sucesso"}), 200

# Rota para deletar um produto por ID
@product_bp.route('/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    for p in produtos:
        if p['id'] == id:
            produtos.remove(p)
            return jsonify({"message": "Produto deletado com sucesso"}), 200
    return jsonify({"message": "Produto não encontrado"}), 404