from django.urls import path
from apps.yt_download.views import YTDownloadFormView


urlpatterns = [
    path('download_video/', YTDownloadFormView.as_view(), name='yt_dl'),
]