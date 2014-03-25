from django.forms import ModelForm
from .models import Apk


class ApkForm(ModelForm):
    class Meta:
        model = Apk
        fields = ['package_name',
                  'ver_major',
                  'ver_minor',
                  'ver_patch',
                  'activity_intent',
                  'service_intent',
                  'receiver_intent',
                  'file', ]
