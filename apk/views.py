import logging
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import View
from django.views.generic.list import ListView
from django.utils import timezone


from .forms import ApkForm
from .models import Apk


logger = logging.getLogger(u"apk.views")


class ApkView(View):
    def get(self, request, *args, **kwargs):
        form = ApkForm()
        c = {'form': form}
        c.update(csrf(request))
        return render_to_response('apk/upload.html', c)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = ApkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        c = {'form': form}
        c.update(csrf(request))
        return render_to_response('apk/upload.html', c)


class ApkListView(ListView):

    model = Apk

    def get_context_data(self, **kwargs):
        context = super(ApkListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def json_output(request):
    import json
    response_data = []
    # only works on PgSQL
    #all_apks = Apk.objects.order_by('created').distinct('package_name')
    all_apk_names = Apk.objects.values_list('package_name').distinct()
    logger.debug(all_apk_names)
    for apk_name in all_apk_names:
        logger.debug(apk_name)
        apk = Apk.objects.filter(
            package_name__exact=apk_name[0]).order_by('created')[:1][0]
        response_data.append({
            'package_name': apk_name,
            'version': '{0}.{1}.{2}'.format(apk.ver_major,
                                            apk.ver_minor,
                                            apk.ver_patch),
            'download_link': apk.file.url,
            'activity_intent': apk.activity_intent,
            'service_intent': apk.service_intent,
            'receiver_intent': apk.receiver_intent,
        })
    return HttpResponse(json.dumps(response_data),
                        content_type="application/json")
