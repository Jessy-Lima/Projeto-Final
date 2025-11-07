from fastapi import FastAPI
import funcao

app = FastAPI(title="Gerenciador de produtos")

@app.get("/")
def home():
    return {"mensagem": "Bem-Vindo ao gerenciador de produtos"}


@app.post("/produtos")
def cadastrar_produto(nome: str, categoria: str, preco: float, quantidade: int):
    funcao.adicionar_produto(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto cadastrado com sucesso!"}

