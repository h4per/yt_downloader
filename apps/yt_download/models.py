from django.db import models

# Create your models here.
class YTDownload(models.Model):
    video_url = models.URLField(
        verbose_name='Ссылка на видео',
        blank=True
    )
    email = models.EmailField(
        verbose_name='Email',
        blank=True
    )
    status = models.BooleanField(
        verbose_name='Статус',
        default=False
    )

    def __str__(self):
        return self.video_url 
    
    class Meta:
        verbose_name = 'URL братель'
        verbose_name_plural = 'URL братели'