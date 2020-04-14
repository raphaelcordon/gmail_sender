import config
import smtplib
import pandas as pd

from email.message import EmailMessage

Email_Address = config.EMAIL_ADDRESS
Email_pass = config.PASSWORD

contacts = pd.read_excel('contato.xlsx') # O endereço precisa ser a extensão completa do arquivo

for cont in range(0, len(contacts)):
        email = contacts.Email[cont]
        nome = contacts.Nome[cont]
        msg = EmailMessage()
        msg['Subject'] = 'Material impresso - Promoção'
        msg['From'] = 'Gráfica Print'
        msg['To'] = email
        msg.set_content(f"""Bom dia.
        
        Estou testando o app de spam do Denis""")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(Email_Address, Email_pass)
                smtp.send_message(msg)
                print(f'\33[1:34mEmail enviado com sucesso para:\33[m {nome}')

