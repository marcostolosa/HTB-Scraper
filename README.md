# HTB WriteUp Finder

O **HTB WriteUp Finder** é uma ferramenta que facilita a busca por write-ups e walkthroughs de HackTheBox. Ele utiliza uma interface amigável baseada em Streamlit e armazena informações de repositórios do GitHub em um banco de dados SQLite, atualizado automaticamente.

## Funcionalidades
- Busca por repositórios no GitHub relacionados a HackTheBox.
- Armazenamento local em um banco de dados SQLite.
- Interface simples para pesquisar write-ups por palavras-chave (ex.: nível de dificuldade ou nome da máquina).

## Pré-requisitos
- Python 3.8 ou superior
- Um token de acesso pessoal do GitHub (para evitar limites de taxa na API)

## Instalação
1. Clone este repositório:

``` Bash
git clone https://github.com/marcostolosa/HTB-Sraper.git
cd HTB-Sraper
```

2. Instale as dependências:

``` Bash
pip install -r requirements.txt
```

3. Crie um arquivo `.env` na raiz do projeto com seu token de acesso pessoal do GitHub:
   - Crie um token em `Settings > Developer settings > Personal access tokens` no GitHub.
   - Escolha permissões de leitura de repositórios (`repo`).
   - Adicione ao `.env`:

``` Bash
echo "GITHUB_API_TOKEN=seu_token_aqui" > .env
```

## Uso
1. Atualize o banco de dados com repositórios do GitHub:

``` Bash
python update_db.py
```

2. Inicie a interface do Streamlit:

``` Bash
streamlit run app.py
```

3. Abra seu navegador em `http://localhost:8501` e comece a buscar o que precisa!

## Dicas
- Para atualizações automáticas semanais, configure um agendador:
  - No Linux/Mac: Use `cron` com `crontab -e` e adicione `0 0 * * 0 python /caminho/para/update_db.py`.
  - No Windows: Use o Task Scheduler.
- O banco de dados (`repositories.db`) será criado automaticamente na primeira execução do `update_db.py`.
- Adicione `.env` ao `.gitignore` para evitar expor seu token no controle de versão.

## Contribuição
Sinta-se à vontade para abrir issues ou enviar pull requests no repositório. Sugestões de melhorias são sempre bem-vindas!

