from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    def test_home_page_returns_welcome_message(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>Welcome to the Home Page!</h1>")


from rest_framework.test import APITestCase


class APIStatusTests(APITestCase):
    def test_status_returns_application_details(self):
        response = self.client.get(reverse('api-status'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'status': 'ok',
            'application': 'CSC325 CI/CD Pipeline',
            'message': 'Ready for the four-stage pipeline!',
        })

    def test_status_rejects_post(self):
        response = self.client.post(reverse('api-status'), {}, format='json')
        self.assertEqual(response.status_code, 405)

    def test_status_includes_pipeline_message(self):
        response = self.client.get(reverse('api-status'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Ready for the four-stage pipeline!')
