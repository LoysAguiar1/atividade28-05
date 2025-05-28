import json

def carregar_dados_json(caminho):
    with open(caminho) as arquivo:
        dados = json.load(arquivo)
    return dados

def buscar_usuario(dados, nome):
    for usuario in dados:
        if usuario.get("nome") == nome:
            return usuario
    return None

def exibir_usuario(usuario):
    if usuario:
        print("Usuário encontrado:")
        print("Nome:", usuario["nome"])
        print("Idade:", usuario["idade"])
    else:
        print("Usuário não encontrado.")

dados = carregar_dados_json("usuarios.json")
nome = input("Digite o nome do usuário: ")
usuario = buscar_usuario(dados, nome)
exibir_usuario(usuario)