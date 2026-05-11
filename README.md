# 🪪 CONSULTA CPF COM PYTHON

Aplicação simples desenvolvida em Python para realizar consultas de CPF utilizando interface gráfica com CustomTkinter e API externa.

---

# 🚀 FUNCIONALIDADES

- 🔍 Consulta de CPF via API
- 🖥️ Interface gráfica moderna
- 👤 Exibição do nome do usuário
- 🪪 Exibição do CPF
- 📌 Situação cadastral
- 🎂 Data de nascimento
- ⚠️ Feedback visual de erro
- 🌙 Tema escuro moderno

---

# 🛠️ TECNOLOGIAS UTILIZADAS

- 🐍 Python 3
- 🎨 CustomTkinter
- 🌐 Requests
- 🔎 API CPFHub

---

# 📂 ESTRUTURA DO PROJETO

```text
consulta-cpf/
│
├── main.py
├── icon.ico
├── requirements.txt
└── README.md
```

---

# 💻 PRÉ-REQUISITOS

Antes de executar o projeto, instale:

- 🐍 Python 3.10 ou superior

Download oficial:

https://www.python.org

---

# 📦 INSTALAÇÃO DAS DEPENDÊNCIAS

Instale manualmente:

```bash
pip install customtkinter requests
```

Ou utilize o `requirements.txt`

Crie o arquivo:

```text
customtkinter
requests
```

Depois execute:

```bash
pip install -r requirements.txt
```

---

# ▶️ COMO EXECUTAR

Execute o arquivo principal:

```bash
python main.py
```

---

# 🧠 EXPLICAÇÃO DO CÓDIGO

## 📚 IMPORTAÇÃO DAS BIBLIOTECAS

```python
import customtkinter as ctk
import requests
```

- 🎨 customtkinter → cria a interface gráfica moderna
- 🌐 requests → realiza requisições para a API

---

## 🎨 CONFIGURAÇÃO VISUAL

```python
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
```

Define:

- 🌙 Tema escuro
- 🔵 Cor azul padrão

---

# 🔍 FUNÇÃO DE CONSULTA

```python
def consultar_cpf():
```

Responsável por:

- ✍️ Capturar o CPF digitado
- 🌐 Consultar a API
- 📄 Exibir os dados retornados
- ⚠️ Mostrar erro caso a consulta falhe

---

## 🪪 CAPTURANDO O CPF

```python
cpf = entrada.get().strip()
```

Obtém o CPF digitado pelo usuário.

---

## 🌐 URL DA API

```python
url = f"https://api.cpfhub.io/cpf/{cpf}"
```

Monta o endereço da consulta.

---

## 📡 DADOS DA REQUISIÇÃO

```python
dados = {
    "x-api-key": "SUA_API_KEY",
    "Accept": "application/json"
}
```

Envia:

- 🔑 Sua chave da API
- 📄 Tipo de resposta esperada

---

## 📥 REALIZANDO A CONSULTA

```python
resposta = requests.get(url, headers=dados)
```

Faz a requisição para a API.

---

## 🔄 CONVERTENDO OS DADOS

```python
resultado_api = resposta.json()
```

Transforma a resposta da API em dicionário Python.

---

## 📋 EXIBINDO OS DADOS

```python
texto = (
    f"CPF: {resultado_api.get('cpf','')}\n"
    f"Nome: {resultado_api.get('nome','')}\n"
    f"Situação: {resultado_api.get('situacao','')}\n"
    f"Data de Nascimento: {resultado_api.get('data_nascimento','')}"
)
```

Mostra as informações retornadas.

---

# 🖼️ INTERFACE DA APLICAÇÃO

Exemplo da interface:

<img width="505" height="438" alt="image" src="https://github.com/user-attachments/assets/cb238f68-0b6c-43c7-8286-6d04dd0afb6c" />

---

# 🔒 OBSERVAÇÕES

- 🔑 É necessário possuir uma API KEY válida
- 📌 Algumas consultas podem depender do plano da API
- ⚖️ Utilize apenas para fins educacionais e legais

---

# 👨‍💻 AUTOR

Projeto desenvolvido para estudos de:

- 🐍 Python
- 🌐 APIs
- 🖥️ Interface gráfica
- 📡 Requisições HTTP

---

# 🤝 CONTRIBUIÇÃO

Contribuições são bem-vindas.

Faça um fork do projeto e envie um pull request.

---

# 📄 LICENÇA

📜 Este projeto está sob a licença MIT.
