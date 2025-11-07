import streamlit as st
import requests 

API_URL = "http://10.104.82.31:8501"

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
        