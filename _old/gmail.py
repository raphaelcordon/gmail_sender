import smtplib
import config as gconfig
import pandas as pd

print('Lendo planilha...')
data = pd.read_excel(r'gmaillist.xlsx')
df = pd.DataFrame(data, columns=['email'])
print(f'{df[c]}')


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(gconfig.EMAIL_ADDRESS, gconfig.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(gconfig.EMAIL_ADDRESS, df['email'], message)
        server.quit()
        print('Success: Email sent!')
    except:
        print('Email failed to send.')

subject = 'Test Subject'
msg = 'Testando'

send_email(subject, msg)
