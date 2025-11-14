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


