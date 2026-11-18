# LogiMove MVC - Sistema de Gestão de Transporte e Movimentação Logística

Projeto desenvolvido para a disciplina **Projeto Integrador Transdisciplinar em Engenharia de Software II**.

## Arquitetura e Tecnologias
- **Padrão Arquitetural:** MVC (Model-View-Controller)
- **Back-end:** Python 3.11+ com Flask
- **Front-end:** HTML5, CSS3 e JavaScript ES6+ (Fetch API)
- **Banco de Dados:** PostgreSQL 16 (Script DDL e Dicionário de Dados em `/sql` e `/docs`)
- **Testes Automatizados:** Pytest

## Como Executar o Projeto Localmente

1. Instale as dependências:
pip install -r requirements.txt

2. Execute a suíte de testes unitários (Verificação):
pytest -v

3. Inicie o servidor web:
python app.py

4. Acesse no navegador:
http://localhost:5000