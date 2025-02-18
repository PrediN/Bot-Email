# Autor: Pedro Sanchez
# Data inicial: 18/02/2025
# Última atualização: 18/02/2025
# Objetivo: Código feito para estudo e aprendizado
# Python 3.13.2
# Função: Enviar e-mails com informações no corpo do e-mail	


# Importando bibliotecas
import smtplib


# Declaração de variáveis

email = str(input("Digite o e-mail: ")).strip().lower()
senha = str(input("Digite a senha do e-mail: ")).strip()
destinatario = str(input("Digite o e-mail do destinatário: ")).strip().lower()
assunto = str(input("Digite o assunto: ")).strip()
mensagem = str(input("Digite a mensagem: ")).strip()


# Envio de e-mail

with smtplib.SMTP("smtp.gmail.com", 587) as smtp: # Servidor SMTP do Gmail e o with serve para fechar a conexão automaticamente
    smtp.starttls() # Iniciando a conexão
    smtp.login(email, senha) # Fazendo login
    corpo_email = f"Assunto: {assunto}\n\n{mensagem}" # Corpo do e-mail
    smtp.sendmail(email, destinatario, corpo_email) # Enviando o e-mail
    print("E-mail enviado com sucesso!") # Mensagem de sucesso