# Generated by Django 4.2.4 on 2023-10-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yt_download', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ytdownload',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
