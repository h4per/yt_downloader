from apps.yt_download.tasks import work
from django import forms
# Создаем нашу форму 
class YTDownloadForm(forms.Form):
    video_url = forms.CharField(
        label="URL"
    )
    email = forms.EmailField(
        label="Email"
    )
# Определяем метод send_email для отправки электронного письма
    def send_email(self):
        work.apply_async(args=[
            self.cleaned_data['video_url'],
            self.cleaned_data['email']
])