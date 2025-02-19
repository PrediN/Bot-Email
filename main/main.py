# Autor: Pedro Sanchez
# Data inicial: 18/02/2025
# Última atualização: 18/02/2025
# Objetivo: Código feito para estudo e aprendizado
# Python 3.13.2
# Função: Enviar e-mails com informações no corpo do e-mail	


# Importando bibliotecas
import smtplib
import json

# Declaração de variáveis

email = "testepedropython@gmail.com"
senha = "ytxh eoxf txln agtr"
destinatario = "testepedropython@hotmail.com"
assunto = str(input("Digite o assunto: ")).strip()
mensagem = str(input("Digite a mensagem: ")).strip()


# Carregando as informações do arquivo JSON
# 
# with open("teste.json", "r") as arquivo:
#     mensagem = json.load(arquivo)

# Construindo o e-mail como uma string
mensagem = f"From: {email}\nTo: {destinatario}\nSubject: {assunto}\n\n{mensagem}"

# Envio de e-mail

with smtplib.SMTP("smtp.gmail.com", 587) as smtp: # Servidor SMTP do Gmail e o with serve para fechar a conexão automaticamente
    smtp.starttls() # Iniciando a conexão
    smtp.login(email, senha) # Fazendo login no e-mail
    # mensagem.encode('utf-8') # Codificando a mensagem para o padrão UTF-8
    smtp.sendmail(email, destinatario, mensagem) # Enviando o e-mail


print("E-mail enviado com sucesso!") # Mensagem de sucesso