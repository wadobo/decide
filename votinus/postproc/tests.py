from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework.test import APITestCase


class PostProcTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def tearDown(self):
        self.client = None

    def test_identity(self):
        data = {
            'type': 'IDENTITY',
            'options': [
                { 'option': 'Option 1', 'votes': 5 },
                { 'option': 'Option 2', 'votes': 0 },
                { 'option': 'Option 3', 'votes': 3 },
                { 'option': 'Option 4', 'votes': 2 },
                { 'option': 'Option 5', 'votes': 5 },
                { 'option': 'Option 6', 'votes': 1 },
            ]
        }

        expected_result = [
            { 'option': 'Option 1', 'votes': 5, 'postproc': 5 },
            { 'option': 'Option 5', 'votes': 5, 'postproc': 5 },
            { 'option': 'Option 3', 'votes': 3, 'postproc': 3 },
            { 'option': 'Option 4', 'votes': 2, 'postproc': 2 },
            { 'option': 'Option 6', 'votes': 1, 'postproc': 1 },
            { 'option': 'Option 2', 'votes': 0, 'postproc': 0 },
        ]

        response = self.client.post('/postproc/', data, format='json')
        self.assertEqual(response.status_code, 200)

        values = response.json()
        self.assertEqual(values, expected_result)
