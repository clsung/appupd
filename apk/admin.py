from django.contrib import admin
from .models import Apk


class ApkAdmin(admin.ModelAdmin):
    ordering = ('-created',)


admin.site.register(Apk, ApkAdmin)
