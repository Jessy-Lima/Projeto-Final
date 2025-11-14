# 🛒 Gerenciador de Produtos – README

Este projeto é um **Gerenciador de Produtos** com interface feita em **Streamlit** e integração com uma API (FastAPI ou outra) para cadastrar, listar, atualizar e deletar produtos.

---

## 📌 Funcionalidades

* 📦 **Catálogo de Produtos** – Lista todos os produtos cadastrados
* 📝 **Cadastrar Produto** – Envia novos produtos para a API
* ❌ **Deletar Produto** – Remove produtos pelo ID
* 🔄 **Atualizar Quantidade** – Atualiza o estoque de um produto
* 📊 **Estoque Completo** – Mostra os níveis atuais de estoque

---

## 🚀 Tecnologias Utilizadas

* **Python**
* **Streamlit** (Frontend)
* **Requests** (para comunicação com API)
* **FastAPI** ou outra API REST (Backend)

---

## 📁 Estrutura do Projeto

```
📂 seu_projeto
 ├── app.py              # Arquivo principal Streamlit
 ├── requirements.txt    # Dependências
 ├── README.md           # Documentação
```

---

## ⚙️ Configuração

### 1. Instale as dependências

```
pip install -r requirements.txt
```

### 2. Inicie a API

```
uvicorn main:app --reload
```

### 3. Rode o Streamlit

```
streamlit run app.py
```

---

## 🔌 Configurando a URL da API

No início do arquivo:

```python
API_URL = "http://127.0.0.1:8000"
```

Altere caso a API esteja em outro endereço.

---

## 🖼️ Interface (Streamlit)

Menu do app:

```python
menu = st.sidebar.radio(
    "Menu",
    [
        "Catalogo",
        "Cadastrar Produto",
        "Deletar Produto",
        "Atualizar quantidade",
        "Estoque",
    ]
)
```

Cada opção chama um bloco de funções relacionadas.

---

## 📚 Exemplos de Uso

### ✔ Cadastrar Produto

Envia POST para a API.

### ✔ Listar Produtos

Envia GET para receber todos os produtos.

### ✔ Deletar Produto

Envia DELETE /produto/{id}

### ✔ Atualizar Quantidade

Envia PUT /produto/{id}

---

## 🧪 Testes

Você pode testar a API diretamente em:

```
http://127.0.0.1:8000/docs
```

(Interface automática Swagger do FastAPI)

---

## 🤝 Contribuição

Sinta-se à vontade para sugerir melhorias ou abrir issues.

---

## 📄 Licença

Este projeto pode ser utilizado livremente para fins educacionais.
