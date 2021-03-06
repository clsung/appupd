from django.db import models
from hashlib import md5
from datetime import datetime


def generate_content_filename(instance, filename):
    #ext = os.path.splitext(filename)[1]
    #return 'converted/{0}.{1}'.format(uuid4(), ext)
    return u'apk/{0}-{1}'.format(
        md5(datetime.now().isoformat()).hexdigest()[:8],
        filename)


class Apk(models.Model):
    package_name = models.CharField(max_length=100)
    ver_major = models.PositiveSmallIntegerField(default=0)
    ver_minor = models.PositiveSmallIntegerField(default=1)
    ver_patch = models.PositiveSmallIntegerField(default=0)
    device_type = models.CharField(max_length=100)
    activity_intent = models.CharField(max_length=100, null=True, blank=True)
    service_intent = models.CharField(max_length=100, null=True, blank=True)
    receiver_intent = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=generate_content_filename)
