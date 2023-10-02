from django.contrib import admin
from apps.yt_download.models import YTDownload

# Register your models here.
@admin.register(YTDownload)
class YTDownloadAdmin(admin.ModelAdmin):
    list_display = ('video_url', 'email', 'status')
