import streamlit as st
import requests 

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Produtos", layout="wide")

st.title("Gerenciador de Produtos")

menu = st.sidebar.radio("Menu", 
    ["Catalogo", "Cadastrar Produto", "Deletar Produto", "Atualizar quantidade","Estoque"]
    )
if menu == "Catalogo":
    st.subheader("Todos os Produtos")
    response = requests.get(f"{API_URL}/produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            st.dataframe(produtos)
        else:
            st.info("Nenhum produto cadastrado ainda!")
    else:
        st.error("Erro ao conectar com a API.")
        
elif menu == "Cadastrar Produto":
    st.subheader("➕Adicionar Produto")
    nome = st.text_input("Nome do Produto")
    categoria = st.text_input("Categoria do Produto")
    preco = st.number_input("Preço do Produto")
    quantidade = st.number_input("Quantidade do Produto", step=1)
    if st.button("Salvar Produto"):
        dados = {"nome":nome, "categoria":categoria, "preco":preco, "quantidade":quantidade}
        response = requests.post(f"{API_URL}/produtos", params=dados)
        if response.status_code == 200:
            st.success("Produto adicionado comsucesso!")
        else:
            st.error("Erro ao adicionar produto.")