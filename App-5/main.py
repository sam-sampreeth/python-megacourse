import requests
import smtplib, ssl
import os

def mailer(msg):
    host = 'smtp.gmail.com'
    port = 465
    username = "sam.sampreeth001@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "sam.sampreeth001@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg)

api_key = "ff370c0d89aa43f881c8b3405f454cd7"

q = "tesla"
url = f"https://newsapi.org/v2/everything?q={q}&from=2024-08-29&to=2024-08-29&sortBy=popularity&apiKey={api_key}&language=en"
reqs = requests.get(url)
cont = reqs.json()

mailCont = "Subject: News\n\n"
for article in cont["articles"][:20]:
    if article["title"] is not None:
        mailCont += article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

mailCont = mailCont.encode("utf-8")
mailer(mailCont)
