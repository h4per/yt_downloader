from apps.yt_download.tasks import send_feedback_email_task
from django import forms


class YTDownloadForm(forms.Form):
    video_url = forms.CharField(
        label="URL"
    )
    email = forms.EmailField(
        label="Email"
    )

    def send_email(self):
        send_feedback_email_task.apply_async(args=[
            self.cleaned_data['video_url'], self.cleaned_data['email']
            ]
        )