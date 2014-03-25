from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.


class ApkView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')
