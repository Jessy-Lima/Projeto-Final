from fastapi import FastAPI
import funcao

app = FastAPI(title="Gerenciador de produtos")

@app.get("/")
def home():
    return {"mensagem": "Bem-Vindo ao gerenciador de produtos"}


@app.post("/produtos")
def cadastrar_produto(nome: str, categoria: str, preco: float, quantidade: int):
    funcao.cadastrar_produto(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto cadastrado com sucesso!"}

@app.get("/produtos")
def listar_produtos():
    produtos = funcao.listar_produtos()
    lista = []
    for linha in produtos:
        lista.append(
            {
                "id": linha[0],
                "nome": linha[1],
                "categoria": linha[2],
                "preco": linha[3],
                "quantidade": linha[4]
            }
        )
    return{"produtos":lista}

@app.delete("/produtos/{id_produto}")
def deletar_filme(id_produto: int):
    filmes = funcao.buscar_produto(id_produto)
    if filmes:
        funcao.deletar_produto(id_produto)
        return {"mensagem": "Produto excluído com sucesso!"}
    else:
        return{"erro": "Filme não encontrado"}

@app.put("/produtos/{id_produto}")
def atualizar_produto(id_produto: int, nova_quantidade: int):
    produtos = funcao.buscar_produto(id_produto)
    if produtos:
        funcao.atualizar_produto(id_produto, nova_quantidade)
        return {"mensagem": "Produto atualizado com sucesso"}
    else:
        return {"erro": "Produto não encontrado"}