import sqlite3
import github3
from datetime import datetime
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter o token do GitHub do .env
GITHUB_TOKEN = os.getenv("GITHUB_API_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_API_TOKEN não encontrado no arquivo .env")

# Conectar ao GitHub
gh = github3.login(token=GITHUB_TOKEN)

# Conectar ao banco de dados
conn = sqlite3.connect('repositories.db')
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS repositories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    readme_content TEXT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Buscar repositórios no GitHub
query = "(HTB OR HackTheBox OR WriteUp OR Walkthrough OR Machine OR Easy OR Medium OR Hard) type:repo"
results = gh.search_repositories(query)

# Atualizar o banco de dados
for repo in results:
    name = repo.full_name
    description = repo.description if repo.description else ""
    # Obter conteúdo do README
    try:
        readme = repo.readme()
        readme_content = readme.decoded.decode('utf-8') if readme else ""
    except:
        readme_content = ""

    # Verificar se o repositório já existe no banco
    cursor.execute("SELECT id FROM repositories WHERE name = ?", (name,))
    existing = cursor.fetchone()

    if existing:
        # Atualizar registro existente
        cursor.execute(
            "UPDATE repositories SET description = ?, readme_content = ?, last_updated = ? WHERE name = ?",
            (description, readme_content, datetime.now(), name)
        )
    else:
        # Inserir novo registro
        cursor.execute(
            "INSERT INTO repositories (name, description, readme_content, last_updated) VALUES (?, ?, ?, ?)",
            (name, description, readme_content, datetime.now())
        )

# Salvar alterações e fechar conexão
conn.commit()
conn.close()

print("Banco de dados atualizado com sucesso!")