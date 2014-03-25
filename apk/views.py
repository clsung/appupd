from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic import View
from django.views.generic.list import ListView
from django.utils import timezone


from .forms import ApkForm
from .models import Apk


class ApkView(View):
    def get(self, request, *args, **kwargs):
        form = ApkForm()
        return render_to_response('apk/upload.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = ApkForm(request.POST, request.FILES)
        if form.is_valid():
            #f = LogFileResource(logfile=request.FILES['file'])
            form.save()
            return HttpResponseRedirect('/')
        return render_to_response('apk/upload.html', {'form': form})


class ApkListView(ListView):

    model = Apk

    def get_context_data(self, **kwargs):
        context = super(ApkListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
