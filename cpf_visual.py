import customtkinter as ctk
import requests

# Configuração da janela
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#janela
app = ctk.CTk()
app.title("Consulta CPF")
app.geometry("500x400")

# Função de consulta
def consultar_cpf():
    cpf = entrada.get().strip()

    url = f"https://api.cpfhub.io/cpf/{cpf}"

    dados = {
        "x-api-key": "SUA_API_KEY",
        "Accept": "application/json"
    }

    resposta = requests.get(url, headers=dados)

    resultado_api = resposta.json()

    texto = (
        f"CPF: {resultado_api.get('cpf','')}\n"
        f"Nome: {resultado_api.get('nome','')}\n"
        f"Situação: {resultado_api.get('situacao','')}\n"
        f"Data de Nascimento: {resultado_api.get('data_nascimento','')}"
    )

    resultado.configure(text=texto)

# Título
titulo = ctk.CTkLabel(app, text="Consulta de CPF", font=("Arial", 20))
titulo.pack(pady=20)

# Entrada
entrada = ctk.CTkEntry(app, placeholder_text="Digite o CPF")
entrada.pack(pady=10)

# Botão
botao = ctk.CTkButton(app, text="Consultar", command=consultar_cpf)
botao.pack(pady=10)

# Resultado
resultado = ctk.CTkLabel(app, text="", justify="left")
resultado.pack(pady=20)

# Executar
app.mainloop()