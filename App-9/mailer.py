from email.message import EmailMessage

from dotenv import load_dotenv
import os
import smtplib

from pygments.lexers import q

load_dotenv()
app_pass = os.getenv('APP_PASS')
app_id = os.getenv('APP_ID')
receiver = os.getenv('APP_ID')

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New object detected"
    email_message.set_content("I just detected a new object in the video!")

    with open(image_path, "rb") as file:
        content = file.read()

    email_message.add_attachment(content, maintype='image', subtype='PNG')

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(app_id, app_pass)
    gmail.sendmail(app_id, receiver, email_message.as_string())
    gmail.quit()

if __name__ == '__main__':
    send_email(image_path="images/19.png")