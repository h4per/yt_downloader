import os
import smtplib

from youtube_dl import YoutubeDL
from celery import shared_task

from django.conf import settings

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Создаем задачу Celery для отправки видео там чего угодно на электронную почту
@shared_task
def work(video_url, email):
    # Извлекаем информацию о видео с помощью youtube_dl
    video_info = YoutubeDL().extract_info(url=video_url, download=True)
    # Создаем переменныу для сохранения видео или аудио у нас
    file_name = os.path.join('media/', video_info['title'])
    # Проверка на юрл если есть то скачиваем
    if video_url:
        # Настройки загрузки
        ydl_opts = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': file_name,
            'verbose': True,
        }
        # Загружаем аудио с указанной ссылки и применяем опции
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            # Тут настраиваем чо и отправлять вместе с аудио
            subject = f"Видео"
            body = f"На держи свое видео ---> {video_info['title']}"

            msg = MIMEMultipart()
            msg['From'] = settings.EMAIL_HOST_USER
            msg['To'] = email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            # Настройки отправления на почту
            part = MIMEBase('audio', 'mp3')
            part.set_payload(open(file_name, 'rb').read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename="audio.mp3")
            msg.attach(part)
            # Настройки Smtp там кто отправляет куда 
            with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
                server.starttls()
                server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                server.send_message(msg)
