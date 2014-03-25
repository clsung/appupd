from django.test import TestCase
from django.test.client import Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.urlresolvers import reverse


class UploadAPKTests(TestCase):
    def setUp(self):
        self.c = Client()

    def tearDown(self):
        pass

    def test_upload_single_apk(self):
        url = reverse('upload_apk')
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
