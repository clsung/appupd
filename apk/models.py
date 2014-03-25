from django.db import models


class Apk(models.Model):
    package_name = models.CharField(max_length=100)
    ver_major = models.PositiveSmallIntegerField(default=0)
    ver_minor = models.PositiveSmallIntegerField(default=1)
    ver_patch = models.PositiveSmallIntegerField(default=0)
    download_link = models.CharField(max_length=1024)
    activity_intent = models.CharField(max_length=100)
    service_intent = models.CharField(max_length=100)
    receiver_intent = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=generate_content_filename)
