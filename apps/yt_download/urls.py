from django.urls import path
from apps.yt_download.views import YTDownloadAPIView


urlpatterns = [
    path('download_video/', YTDownloadAPIView.as_view({'post': 'download_video'}), name='download_video'),
]

