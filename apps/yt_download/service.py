# import os
# from django.core.mail import send_mail
# from django.conf import settings
# from youtube_dl import YoutubeDL


# def download_video(self, request):
#         video_url = request.data.get('video_url', '')
#         email_get =  request.data.get('email', '')
#         video_info = YoutubeDL().extract_info(url=video_url, download=False) 
#         file_name = os.path.join('media/',video_info['title'])

#         if video_url:
#             ydl_opts = {
#                 'format': 'bestaudio/best',
#                 'outtmpl': file_name,
#                 'verbose': True,
#                 }
#             with YoutubeDL(ydl_opts) as ydl:
#                 ydl.download([video_url])

# def send(email):
#     send_mail(
#         'Видео',
#         'dfv',
#         settings.EMAIL_HOST_USER,
#         [email],
#         fail_silently=True,
#     )


