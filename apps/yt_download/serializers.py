from rest_framework import serializers
from apps.yt_download.models import YTDownload

class YTDownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = YTDownload
        fields = "__all__"
