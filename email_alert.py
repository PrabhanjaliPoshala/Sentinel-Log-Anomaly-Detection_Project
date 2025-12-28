import smtplib
from email.mime.text import MIMEText

def send_email_alert(subject, message):
    sender = "your_email@gmail.com"
    receiver = "receiver_email@gmail.com"
    password = "APP_PASSWORD"

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)
