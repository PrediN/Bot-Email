# Autor: Pedro Sanchez
# Data inicial: 18/02/2025
# Última atualização: 18/02/2025
# Objetivo: Código feito para estudo e aprendizado
# Python 3.13.2
# Função: Enviar e-mails com informações no corpo do e-mail	


# Importando bibliotecas
import smtplib
from email.mime.text import MIMEText
import json
import subprocess

def enviar_email(remetente, senha, destinatario, assunto):
    """
    Executa o search.py, carrega os resultados do JSON e envia um e-mail.
    """
    try:
        # Executar o search.py como um subprocesso
        subprocess.run(["python", "C:\\Users\\passa\\Documents\\GitHub\\Bot-Email\\main\\search.py"], check=True)

        # Carregar os resultados da busca do arquivo JSON
        with open('resultados_busca.json', 'r', encoding='utf-8') as arquivo_json:
            resultados_busca = json.load(arquivo_json)

        # Formatar o corpo do email com os resultados da busca
        corpo_email = f"""
        <p>Olá!</p>
        <p>Resultados da busca por '{assunto}':</p>
        <ul>
        """
        for resultado in resultados_busca:
            corpo_email += f"""
            <li>
                <a href="{resultado['href']}">{resultado['title']}</a><br>
                {resultado['body']}
            </li>
            """
        corpo_email += "</ul>"

        # Criar e enviar o email
        msg = MIMEText(corpo_email, 'html')
        msg['Subject'] = assunto
        msg['From'] = remetente
        msg['To'] = destinatario

        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(remetente, senha)
            s.sendmail(remetente, [destinatario], msg.as_string())
            print('Email enviado')

    except Exception as e:
        print(f"Erro ao enviar email: {e}")

# Exemplo de uso
if __name__ == '__main__':
    remetente = 'testepedropython@gmail.com'
    senha = 'ytxh eoxf txln agtr'
    destinatario = 'testepedropython@gmail.com'
    assunto = 'Resultados de pesquisa: Inteligência artificial avanços'
    enviar_email(remetente, senha, destinatario, assunto)