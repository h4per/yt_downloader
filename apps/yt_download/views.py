from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response

from apps.yt_download.models import YTDownload
from apps.yt_download.serializers import YTDownloadSerializer
from youtube_dl import YoutubeDL

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from django.conf import settings

# Create your views here.
class YTDownloadAPIView(GenericViewSet,
                        mixins.CreateModelMixin, 
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin):
    queryset = YTDownload.objects.all()
    serializer_class = YTDownloadSerializer

    def download_video(self, request):
        video_url = request.data.get('video_url', '')
        email_get =  request.data.get('email', '')
        video_info = YoutubeDL().extract_info(url=video_url, download=False) 
        file_name = os.path.join('media/',video_info['title'])

        if video_url:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': file_name,
                'verbose': True,
                }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])

            subject = f"Видео"
            body = f"На держи свое видео ---> {video_info['title']}"

            msg = MIMEMultipart()
            msg['From'] = settings.EMAIL_HOST_USER
            msg['To'] = email_get
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            part = MIMEBase('audio', 'mp3')
            part.set_payload(open(file_name, 'rb').read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename="audio.mp3")
            msg.attach(part)

            with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
                server.starttls()
                server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                server.send_message(msg)

            return Response({'status': 'Успех э'})
        return Response({'status': 'Не успех', 'Ошибка': 'Неправильный URL'}, status=400)

        