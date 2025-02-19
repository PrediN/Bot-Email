# Autor: Pedro Sanchez
# Data inicial: 18/02/2025
# Última atualização: 18/02/2025
# Objetivo: Código feito para estudo e aprendizado
# Python 3.13.2
# Função: Enviar e-mails com informações no corpo do e-mail	


# Importando bibliotecas
import smtplib
import json
import email.message

# Função para enviar e-mail
def enviar_email():

    # Corpo do e-mail
    corpo_email = """
    <p><h1>Olá Pedro</h1></p>
    <p>Segue meu email automatico</p>
    """


    # Criando objeto de mensagem
    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'testepedropython@gmail.com'
    msg['To'] = 'testepedropython@gmail.com'
    password = 'ytxh eoxf txln agtr'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    # Conexão com servidor SMTP
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(msg['From'],password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
    
if __name__ == "__main__":
    enviar_email()
