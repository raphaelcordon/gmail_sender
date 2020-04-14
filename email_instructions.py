from email.message import EmailMessage
from smtplib import SMTP_SSL
import pandas as pd


class EmailInstructions():
    def __init__(self, email_address, email_pass, email_from, spreadsheet_address_viewer, Email_body_text, Welcoming_Message, Email_title):

        contacts = pd.read_excel(spreadsheet_address_viewer)
        for cont in range(0, len(contacts)):
            email = contacts.Email[cont]
            nome = contacts.Nome[cont]
            msg = EmailMessage()
            msg['Subject'] = Email_title
            msg['From'] = email_from
            msg['To'] = email

            if Welcoming_Message == '':
                msg.set_content(Email_body_text)
            else:
                Complete_Welcoming_Message = (Welcoming_Message + ' ' + nome + ',\n\n' + Email_body_text)
                msg.set_content(Complete_Welcoming_Message)

            with SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(email_address, email_pass)
                smtp.send_message(msg)
                print(f'Email enviado com sucesso para: {nome}')
