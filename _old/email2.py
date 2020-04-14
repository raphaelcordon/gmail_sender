# Youtube video: https://www.youtube.com/watch?v=JRCJ6RtE3xU
from email.contentmanager import subtype

import config
import smtplib
from email.message import EmailMessage
from email.mime.image import MIMEImage

Email_Address = config.EMAIL_ADDRESS
Email_pass = config.PASSWORD

contacts = ['Raphael Gmail', 'cordonraphael@gmail.com', 'Raphael Outlook', 'cordon@outlook.com', 'Denis Nappa',
            'denisnappa@gmail.com']

contact_name = ''
contact_email = ''

for email in range(0, len(contacts)):
    if email % 2 == 0:
        contact_name = contacts[email]
    else:
        contact_email = contacts[email]
        try:
            msg = EmailMessage()
            msg['Subject'] = 'Email com instruções :) '
            msg['From'] = 'Raphael Cordon'
            msg['To'] = contact_email
            msg.set_content(f"""
Testando emails com assinatura no rodapé,\n\n
{contact_name}, testando assinatura.jpeg.
""")
            msg.set_raw(file_data, maintype ='image', subtype='file_type', filename='file_name')
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(Email_Address, Email_pass)

                smtp.send_message(msg)
                print(f'\33[1:34mEmail enviado com sucesso para:\33[m {contact_name} - {contact_email}')
        except:
            print(f'\33[1:34mFalha no envio para:\33[m {contact_name} - {contact_email}')
