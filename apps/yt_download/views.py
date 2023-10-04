from apps.yt_download.forms import YTDownloadForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

class YTDownloadFormView(FormView):
    template_name = "yt/index.html"
    form_class = YTDownloadForm
    success_url = "/api/download_video/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

class SuccessView(TemplateView):
    template_name = "yt/after.html"