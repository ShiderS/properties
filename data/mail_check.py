import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
from flask import render_template, Flask, request


def send_mail(sender_email, sender_password, recipient_email, subject='Подтверждение почты'):
    # Создание сообщения
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    verif_code = random.randint(100_000, 999_999)

    # Добавление текста сообщения
    mail_text = f'Ваш код подтверждения почты:\n{verif_code}'
    msg.attach(MIMEText(mail_text, 'plain'))

    try:
        # Подключение к SMTP серверу gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Аутентификация отправителя
        server.login(sender_email, sender_password)
        # Отправка сообщения
        server.send_message(msg)
        return str(verif_code)
    except Exception as e:
        return str(e)