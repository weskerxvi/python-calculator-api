# 🧮 Python Calculator API

![Python](https://img.shields.io/badge/Python-3.x-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Tests](https://img.shields.io/badge/tests-pytest-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

Uma calculadora desenvolvida em **Python** com interface de linha de comando (CLI) e **API REST** utilizando **FastAPI**.

O projeto foi criado para praticar conceitos importantes de desenvolvimento como:

* organização de projetos Python
* manipulação de arquivos
* criação de APIs
* testes automatizados
* logging
* separação de camadas (CLI + API)

---

# 🚀 Funcionalidades

✔ Calculadora em **linha de comando (CLI)**
✔ Operações matemáticas básicas

* ➕ Adição
* ➖ Subtração
* ✖ Multiplicação
* ➗ Divisão
* 🔢 Potenciação

✔ Histórico de operações salvo em **JSON**
✔ Exportação de histórico
✔ Sistema de **logs**
✔ **API REST** com FastAPI
✔ **Testes automatizados** com pytest

---

# 🧠 Tecnologias Utilizadas

* Python
* FastAPI
* Uvicorn
* Pytest
* JSON
* Logging (biblioteca padrão)

---

# 📂 Estrutura do Projeto

```text
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
```

---

# ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/python-calculator-api.git
cd python-calculator-api
```

Instale as dependências:

```bash
pip install fastapi uvicorn pytest
```

---

# 🖥 Executando a Calculadora (CLI)

```bash
python calculadora.py
```

---

# 🌐 Executando a API

Inicie o servidor:

```bash
uvicorn src.api_web:app --reload
```

A API ficará disponível em:

```
http://127.0.0.1:8000
```

Documentação automática:

```
http://127.0.0.1:8000/docs
```

---

# 📡 Endpoints da API

| Método | Endpoint     | Descrição           |
| ------ | ------------ | ------------------- |
| GET    | `/`          | Status da API       |
| GET    | `/historico` | Retorna o histórico |
| GET    | `/ultima`    | Última operação     |
| POST   | `/calcular`  | Realiza um cálculo  |

---

# 🧪 Testes

Execute os testes com:

```bash
pytest
```

---

# 📊 Exemplo de Histórico

```json
[
  {
    "valor1": 10,
    "valor2": 5,
    "operacao": "+",
    "resultado": 15,
    "data": "2026-03-10"
  }
]
```

---

# 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com objetivo educacional para praticar:

* estruturação de projetos Python
* desenvolvimento de APIs
* manipulação de arquivos
* testes automatizados
* boas práticas de programação

---

# 👨‍💻 Autor

**Rodrigo Santos**

Desenvolvedor em aprendizado focado em **Python e Engenharia de Software**.

---

# 📜 Licença

Este projeto está sob a licença MIT.
