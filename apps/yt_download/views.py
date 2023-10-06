from apps.yt_download.forms import YTDownloadForm
from django.views.generic.edit import FormView
from django.shortcuts import render

class YTDownloadFormView(FormView):
    template_name = "yt/index.html"
    form_class = YTDownloadForm
    success_url = "/yt/download_video/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

def after(request):
    return render(request, 'after.html')