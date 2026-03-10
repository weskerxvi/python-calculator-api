Python Calculator API

Um projeto de calculadora desenvolvido em Python que possui interface de linha de comando (CLI), armazenamento de histórico de operações, sistema de logs, testes automatizados e uma API REST construída com FastAPI.

Este projeto foi criado para praticar fundamentos de engenharia de software como organização modular do código, manipulação de arquivos, testes, logging e desenvolvimento de APIs.

🚀 Funcionalidades

Calculadora em linha de comando (CLI)

Operações matemáticas básicas:

Adição

Subtração

Multiplicação

Divisão

Potenciação

Histórico de operações salvo em JSON

Sistema de logs

API REST construída com FastAPI

Testes automatizados com pytest

Exportação do histórico de operações

🧠 Tecnologias Utilizadas

Python

FastAPI

Uvicorn

Pytest

JSON

Logging (biblioteca padrão do Python)

📂 Estrutura do Projeto
calculator/
│
├── src/
│   ├── api.py
│   ├── api_web.py
│   ├── interface.py
│   ├── logger.py
│
├── resultados/
│   ├── historico.json
│   └── calculo.txt
│
├── logs/
│   └── calculadora.log
│
├── tests/
│
├── calculadora.py
└── README.md
⚙️ Instalação

Clone o repositório:

git clone https://github.com/seu-usuario/python-calculator-api.git
cd python-calculator-api

Instale as dependências:

pip install fastapi uvicorn pytest
🖥 Executando a Calculadora CLI
python calculadora.py
🌐 Executando a API

Inicie o servidor da API:

uvicorn src.api_web:app --reload

A API estará disponível em:

http://127.0.0.1:8000

Documentação interativa:

http://127.0.0.1:8000/docs
📡 Endpoints da API
Método	Endpoint	Descrição
GET	/	Status da API
GET	/historico	Retorna o histórico de operações
GET	/ultima	Retorna a última operação
POST	/calcular	Realiza um cálculo
🧪 Executando os Testes

Execute os testes com pytest:

pytest
📊 Exemplo de Histórico em JSON
[
  {
    "valor1": 10,
    "valor2": 5,
    "operacao": "+",
    "resultado": 15,
    "data": "2026-03-10"
  }
]
📌 Objetivos de Aprendizado

Este projeto foi desenvolvido para praticar:

Estrutura de projetos em Python

Manipulação de arquivos

Tratamento de exceções

Sistema de logs

Desenvolvimento de APIs REST

Testes automatizados

📜 Licença

Este projeto é open-source e está disponível sob a licença MIT.
📜 License

This project is open-source and available under the MIT License.
