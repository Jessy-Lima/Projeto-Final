from conexao import conector

def criar_tabela():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                id SERIAL PRIMARY KEY,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                preco REAL NOT NULL,
                quantidade INTEGER
                )
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()
            
criar_tabela()
def cadastrar_produto(nome, categoria, preco, quantidade):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute("""
                INSERT INTO produtos (nome, categoria, preco, quantidade)
                VALUES (%s, %s, %s, %s)
            """, (nome, categoria, preco, quantidade))
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao adicionar produto: {erro}")
        finally:
            cursor.close()
            conexao.commit()

def listar_produtos():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
            "SELECT * FROM produtos ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar os produtos {erro}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_produto(id_produto, nova_quantidade):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "UPDATE produtos SET quantidade = %s WHERE id = %s",
                (nova_quantidade, id_produto)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar quantidade do produto {erro}")
        finally:
            cursor.close()
            conexao.close()

def deletar_produto(id_produto):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM produtos WHERE id = %s",
                (id_filme,)
            )
            conexao.commit()
            if cursor.rowcount > 0:
                print(f"Produto removido com sucesso!")
            else:
                print("Nenhum produto foi encontrado com o ID fornecido.")
        except Exception as erro:
            print(f"Erro ao tentar deletar o produto {erro}")
        finally:
            cursor.close()
            conexao.close()

def buscar_produto(id_produto):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produtos WHERE id = %s",
                (id_produto,)
            )
            return cursor.fetchall()

        except Exception as erro:
            print(f"Erro ao tentar buscar o produto {erro}")
            return []
        finally:
            cursor.close()
            conexao.close()