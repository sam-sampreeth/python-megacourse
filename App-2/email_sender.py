import smtplib, ssl
import os

def sendEmail(message):
    host = 'smtp.gmail.com'
    port = 465
    username = "sam.sampreeth001@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "sam.sampreeth001@gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

