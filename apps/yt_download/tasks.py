
# import smtplib

# from celery import shared_task
# from rest_framework.response import Response
# from youtube_dl import YoutubeDL
# import os
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
# from django.conf import settings

# @shared_task
# def work(video_url, email_get):
#     video_info = YoutubeDL().extract_info(url=video_url, download=True)
#     file_name = os.path.join('media/', video_info['title'])

#     if video_url:
#         ydl_opts = {
#             'format': 'bestaudio/best',
#             'outtmpl': file_name,
#             'verbose': True,
#         }
#         with YoutubeDL(ydl_opts) as ydl:
#             ydl.download([video_url])

#             subject = f"Видео"
#             body = f"На держи свое видео ---> {video_info['title']}"

#             msg = MIMEMultipart()
#             msg['From'] = settings.EMAIL_HOST_USER
#             msg['To'] = email_get
#             msg['Subject'] = subject
#             msg.attach(MIMEText(body, 'plain'))

#             part = MIMEBase('audio', 'mp3')
#             part.set_payload(open(file_name, 'rb').read())
#             encoders.encode_base64(part)
#             part.add_header('Content-Disposition', 'attachment', filename="audio.mp3")
#             msg.attach(part)

#             with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
#                 server.starttls()
#                 server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
#                 server.send_message(msg)

#             return Response({'status': 'success'})

#     return Response({'status': 'error', 'error_message': 'Ошибка: неправильный URL'})

import os
from django.conf import settings
from youtube_dl import YoutubeDL
from django.core.mail import EmailMessage
from celery import shared_task

@shared_task()
def send_feedback_email_task(email, video_url):
    video_info = YoutubeDL().extract_info(url=video_url, download=False) 
    file_name = os.path.join('media/', video_info['title'])

    if video_url:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': file_name,
            'verbose': True,
            }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        email_bek = EmailMessage(
            'Файл готов',
            'На держи брат',
            settings.EMAIL_HOST_USER,
            [email]
        )
        email_bek.attach_file(file_name)
        email_bek.send() 