from django.conf import settings
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.urlresolvers import reverse


class UploadAPKTests(TestCase):
    def setUp(self):
        self.c = Client()
        User.objects.create_user('temp', 'temp@gmail.com', 'temp')
        settings._original_file_storage = settings.DEFAULT_FILE_STORAGE
        settings.DEFAULT_FILE_STORAGE = \
            'django.core.files.storage.FileSystemStorage'

    def tearDown(self):
        settings.DEFAULT_FILE_STORAGE = settings._original_file_storage
        del settings._original_file_storage

    def test_upload_need_login(self):
        url = reverse('upload-apk')
        response = self.c.post(url, {"package_name": "apk0"})
        self.assertEqual(response.status_code, 302)

    def test_upload_single_apk(self):
        url = reverse('upload-apk')
        self.c.login(username='temp', password='temp')
        f = SimpleUploadedFile("apk1_1.0.0.apk", "file_content")
        response = self.c.post(
            url,
            {
                "package_name": "apk1",
                "version": "1.0.0",
                "activity_intent": "activity",
                "service_intent": "service",
                "reverse_intent": "receiver",
                "file": f,
            }
        )
        self.assertEqual(response.status_code, 201)
