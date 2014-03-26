from django.conf.urls import patterns, url
from django.views.decorators.csrf import ensure_csrf_cookie

from apk import views

urlpatterns = patterns(
    '',
    url(r'^upload/$', ensure_csrf_cookie(
        views.ApkView.as_view()), name='upload-apk'),
    url(r'^update$', views.json_output, name='update-check'),
    url(r'^$', views.ApkListView.as_view(), name='apk-list'),
)
