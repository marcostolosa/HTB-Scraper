import streamlit as st
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('repositories.db')
cursor = conn.cursor()

# Função para buscar repositórios no banco de dados
def search_repositories(query):
    query = f'%{query}%'
    cursor.execute(
        "SELECT name, description, readme_content FROM repositories WHERE name LIKE ? OR description LIKE ? OR readme_content LIKE ?",
        (query, query, query)
    )
    return cursor.fetchall()

# Interface do Streamlit
st.title("HTB WriteUp Finder")
st.write("Encontre write-ups e walkthroughs de HackTheBox rapidamente!")

search_term = st.text_input("Digite o termo de busca (ex.: Easy, Medium, Hard, nome da máquina):")

if search_term:
    results = search_repositories(search_term)
    if results:
        st.write("### Resultados da Busca")
        for result in results:
            st.write(f"**Nome do Repositório:** {result[0]}")
            st.write(f"**Descrição:** {result[1] if result[1] else 'Sem descrição disponível'}")
            st.write(f"**Conteúdo do README:** {result[2][:500] + '...' if result[2] else 'Sem README disponível'}")
            st.write("---")
    else:
        st.write("Nenhum resultado encontrado. Tente outro termo!")

# Fechar conexão com o banco de dados
conn.close()