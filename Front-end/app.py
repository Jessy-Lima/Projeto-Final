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

elif menu == "Deletar Produto":
    st.subheader("🗑 Deletar produto")
    id_produto = st.number_input("Id do produto e excluir", min_value=1, step=1)
    if st.button("Excluir"):
        response = requests.delete(f"{API_URL}/produtos/{id_produto}")
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                st.success("Produto excluido com sucesso!")
            else:
                st.error("Erro ao tentar excluir o filme")
        else:
            st.error("Erro ao excluir o produto")

elif menu == "Atualizar quantidade":
    st.subheader("Atualizar Produto")
    id_produto = st.number_input("Id do produto a atualizar", min_value=1, step=1)
    nova_quantidade = st.number_input("Nova quantidade", min_value=1, step=1)
    if st.button("Atualizar"):
        dados = {
            "id_produto": id_produto, 
            "nova_quantidade": nova_quantidade
        }
        response = requests.put(f"{API_URL}/produtos/{id_produto}", params=dados)
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                st.success("Produto atualizado com sucesso!")
            else:
                st.warning(data["erro"])
        else:
            st.error("Erro ao atualizar produto.")