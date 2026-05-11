Consulta CPF com Python

Aplicação simples desenvolvida em Python para realizar consultas de CPF utilizando interface gráfica com CustomTkinter e API externa.

Tecnologias Utilizadas
Python 3
CustomTkinter
Requests
API CPFHub

Estrutura do Projeto
consulta-cpf/
│
├── main.py
├── icon.ico
├── requirements.txt
└── README.md
Funcionalidades
Interface gráfica moderna
Consulta de CPF via API
Exibição de:
Nome
CPF
Situação cadastral
Data de nascimento
Feedback visual de erro
Tema escuro moderno

Pré-requisitos

Antes de executar o projeto, instale:

Python 3.10 ou superior

Download oficial:

Python

Instale manualmente:

pip install customtkinter requests

Ou utilize o requirements.txt

Crie o arquivo:

customtkinter
requests

Depois execute:

pip install -r requirements.txt

Como Executar

Execute o arquivo principal:

python main.py
Explicação do Código
Importação das Bibliotecas
import customtkinter as ctk
import requests
customtkinter → cria a interface gráfica moderna
requests → realiza requisições para a API
Configuração Visual
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

Define:

Tema escuro
Cor azul padrão
Função de Consulta
def consultar_cpf():

Responsável por:

Capturar o CPF digitado
Consultar a API
Exibir os dados retornados
Mostrar erro caso a consulta falhe
Capturando o CPF
cpf = entrada.get().strip()

Obtém o CPF digitado pelo usuário.

URL da API
url = f"https://api.cpfhub.io/cpf/{cpf}"

Monta o endereço da consulta.

Dados da Requisição
dados = {
    "x-api-key": "SUA_API_KEY",
    "Accept": "application/json"
}

Envia:

Sua chave da API
Tipo de resposta esperada
Realizando a Consulta
resposta = requests.get(url, headers=dados)

Faz a requisição para a API.

Convertendo os Dados
resultado_api = resposta.json()

Transforma a resposta da API em dicionário Python.

Exibindo os Dados
texto = (
    f"CPF: {resultado_api.get('cpf','')}\n"
    f"Nome: {resultado_api.get('nome','')}\n"
    f"Situação: {resultado_api.get('situacao','')}\n"
    f"Data de Nascimento: {resultado_api.get('data_nascimento','')}"
)

Observações
É necessário possuir uma API KEY válida.
Algumas consultas podem depender do plano da API.
Utilize apenas para fins educacionais e legais.
📸 Interface da Aplicação

Exemplo da interface:

<img width="505" height="438" alt="image" src="https://github.com/user-attachments/assets/cb238f68-0b6c-43c7-8286-6d04dd0afb6c" />

Projeto desenvolvido para estudos de:

Python
APIs
Interface gráfica
Requisições HTTP
⭐ Contribuição

Contribuições são bem-vindas.

📄 Licença

Este projeto está sob a licença MIT.
