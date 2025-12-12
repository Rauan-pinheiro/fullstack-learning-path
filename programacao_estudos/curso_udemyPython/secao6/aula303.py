# Enviando e-mails SMPT com python

import os
from dotenv import load_dotenv
import pathlib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()

# Caminho HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / 'aula303.html'

# Dados do remetente e destinatário
remetente = os.getenv('email', '')
destinatario = remetente

# Configurações SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = os.getenv('email', '')
smtp_password = os.getenv('password_email', '')

#Mensagem de texto
with open(CAMINHO_HTML, 'r')as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = Template.substitute(nome= 'Rauan')
    
print(texto_email)

# Transforma nossa mensagem em MIMEMultpart
mimi_multpar = MIMEMultipart()
mimi_multpar['from'] = remetente
mimi_multpar['to'] = destinatario
mimi_multpar['subject'] = 'este é o assunto do e-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mimi_multpar.attach(corpo_email)

# Envia o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(mimi_multpar)
    print('E-mail enviado com sucesso!')
    