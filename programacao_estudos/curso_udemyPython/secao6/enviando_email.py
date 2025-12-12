import yagmail
import os
from dotenv import load_dotenv

load_dotenv()

meu_email = os.getenv('email')
minha_senha = os.getenv('password_email')

try:
    yag = yagmail.SMTP(user= meu_email, password= minha_senha)
    yag.send(
    to='destinatario@exemplo.com', subject='Tá com medo?', contents='Fica de boa, Rauan aqui. Tô aprendendo a enviar e-mail com python'
    )
    print('e-mail enviado com sucesso!')
except:
    print('ERRO ao enviar o e-mail.')
