import smtplib, ssl

host = 'smtp.gmail.com'
port = 465

username = "sam.sampreeth001@gmail.com"
password = "mnxgxwymdfbamnzm"

receiver = "sam.sampreeth001@gmail.com"
message="""\
Subject: Test Email
Hello, how are you?
"""
context = ssl.create_default_context()
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
