# Generated by Django 4.2.4 on 2023-10-02 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yt_download', '0002_ytdownload_video_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ytdownload',
            name='video_file',
        ),
    ]