from django.urls import path
from apps.yt_download.views import YTDownloadFormView, after


urlpatterns = [
    path('download_video/', YTDownloadFormView.as_view(), name='yt_dl'),
    path('after/', after, name="done"),
]