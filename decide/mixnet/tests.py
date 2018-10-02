from django.test import TestCase
from django.conf import settings
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from mixnet.mixcrypt import MixCrypt
from mixnet.mixcrypt import ElGamal

from base import mods


class MixnetCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        mods.mock_query(self.client)

    def tearDown(self):
        self.client = None

    def encrypt_msgs(self, msgs, pk, bits=settings.KEYBITS):
        p, g, y = pk
        k = MixCrypt(bits=bits)
        k.k = ElGamal.construct((p, g, y))

        cipher = [k.encrypt(i) for i in msgs]
        return cipher

    def test_create(self):
        data = {
            "voting": 1,
            "auths": [
                { "name": "auth1", "url": "http://localhost:8000" }
            ]
        }

        response = self.client.post('/mixnet/', data, format='json')
        self.assertEqual(response.status_code, 200)

        key = response.json()
        self.key = key

        self.assertEqual(type(key["g"]), int)
        self.assertEqual(type(key["p"]), int)
        self.assertEqual(type(key["y"]), int)

    def test_shuffle(self):
        self.test_create()

        clear = [2, 3, 4, 5]
        pk = self.key["p"], self.key["g"], self.key["y"]
        encrypt = self.encrypt_msgs(clear, pk)
        data = {
            "msgs": encrypt
        }

        response = self.client.post('/mixnet/shuffle/1/', data, format='json')
        self.assertEqual(response.status_code, 200)

        shuffled = response.json()

        self.assertNotEqual(shuffled, encrypt)

    def test_shuffle2(self):
        self.test_create()

        clear = [2, 3, 4, 5]
        pk = self.key["p"], self.key["g"], self.key["y"]
        encrypt = self.encrypt_msgs(clear, pk)
        data = {
            "msgs": encrypt,
            "pk": self.key
        }

        response = self.client.post('/mixnet/shuffle/1/', data, format='json')
        self.assertEqual(response.status_code, 200)

        shuffled = response.json()

        self.assertNotEqual(shuffled, encrypt)

    def test_decrypt(self):
        self.test_create()

        clear = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        pk = self.key["p"], self.key["g"], self.key["y"]
        encrypt = self.encrypt_msgs(clear, pk)

        data = { "msgs": encrypt }

        response = self.client.post('/mixnet/shuffle/1/', data, format='json')
        self.assertEqual(response.status_code, 200)
        shuffled = response.json()
        self.assertNotEqual(shuffled, encrypt)

        data = { "msgs": shuffled }

        response = self.client.post('/mixnet/decrypt/1/', data, format='json')
        self.assertEqual(response.status_code, 200)
        clear2 = response.json()
        self.assertNotEqual(clear, clear2)

        self.assertEqual(sorted(clear), sorted(clear2))

    def test_multiple_auths(self):
        '''
        This test emulates a two authorities shuffle and decryption.

        We create two votings, one with id 1 and another one with id 2, to
        have this separated in the test db.

        Then we compose the PublicKey of both auths.

        Then we encrypt the text with the PK and shuffle two times, once
        with each voting/auth.

        Then we decrypt with the first voting/auth and decrypt the result
        with the second voting/auth.
        '''

        data = { "voting": 1, "auths": [ { "name": "auth1", "url": "http://localhost:8000" } ] }
        response = self.client.post('/mixnet/', data, format='json')
        key = response.json()
        pk1 = key["p"], key["g"], key["y"]

        data = {
            "voting": 2,
            "auths": [ { "name": "auth2", "url": "http://localhost:8000" }],
            "key": {"p": pk1[0], "g": pk1[1]}
        }
        response = self.client.post('/mixnet/', data, format='json')
        key = response.json()
        pk2 = key["p"], key["g"], key["y"]

        self.assertEqual(pk1[:2], pk2[:2])
        pk = (pk1[0], pk1[1], (pk1[2] * pk2[2]) % pk1[0])
        key = {"p": pk[0], "g": pk[1],"y": pk[2]}

        clear = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        encrypt = self.encrypt_msgs(clear, pk)

        data = { "msgs": encrypt, "pk": key }
        response = self.client.post('/mixnet/shuffle/1/', data, format='json')
        shuffled = response.json()
        self.assertNotEqual(shuffled, encrypt)
        data = { "msgs": shuffled, "pk": key }
        response = self.client.post('/mixnet/shuffle/2/', data, format='json')
        self.assertNotEqual(shuffled, encrypt)
        shuffled = response.json()

        data = { "msgs": shuffled, "pk": key, "force-last": False }
        response = self.client.post('/mixnet/decrypt/1/', data, format='json')
        clear1 = response.json()
        data = { "msgs": clear1, "pk": key }
        response = self.client.post('/mixnet/decrypt/2/', data, format='json')
        clear2 = response.json()

        self.assertNotEqual(clear, clear2)
        self.assertEqual(sorted(clear), sorted(clear2))

    def test_multiple_auths_mock(self):
        '''
        This test emulates a two authorities shuffle and decryption.
        '''

        data = {
            "voting": 1,
            "auths": [
                { "name": "auth1", "url": "http://localhost:8000" },
                { "name": "auth2", "url": "http://127.0.0.1:8000" },
            ]
        }
        response = self.client.post('/mixnet/', data, format='json')
        key = response.json()
        pk = key["p"], key["g"], key["y"]

        clear = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        encrypt = self.encrypt_msgs(clear, pk)

        data = { "msgs": encrypt, "pk": key }
        response = self.client.post('/mixnet/shuffle/1/', data, format='json')
        shuffled = response.json()
        self.assertNotEqual(shuffled, encrypt)

        data = { "msgs": shuffled, "pk": key }
        response = self.client.post('/mixnet/decrypt/1/', data, format='json')
        clear1 = response.json()

        self.assertNotEqual(clear, clear1)
        self.assertEqual(sorted(clear), sorted(clear1))
