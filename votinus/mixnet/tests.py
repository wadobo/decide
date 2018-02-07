from rest_framework.test import APIClient
from rest_framework.test import APITestCase



class CharacterTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def tearDown(self):
        self.client = None

    def test_generate_key(self):
        response = self.client.get('/mixnet/gen-key/1/', format='json')
        self.assertEqual(response.status_code, 200)

    def authenticate(self, username='admin', pwd='Qwerty123'):
        response = self.client.login(username=username, password=pwd)
        self.assertTrue(response)
