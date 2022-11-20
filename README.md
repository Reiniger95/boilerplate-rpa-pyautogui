# Boilerplate Rpa Python
## Comandos de inicalização

Criar um ambiente virtual:

    python -m venv env

Ativar o ambiente virtual:

    .\env\Scripts\activate

Desativar o ambiente virtual:

    deactivate

Instalar dependências:

    pip install -r requirements.txt

Atualizar arquivo de referências:

    pip freeze > requirements.txt

Configurar variáveis de ambiente removendo o .example do arquivo .env e adicionando suas credenciais.

## Rodar em produção com pm2

    pm2 start src/main.py --restart-delay 5000
