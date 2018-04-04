import random
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from .models import Vote
from .serializers import VoteSerializer

from base import mods


class StoreTextCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        mods.mock_query(self.client)

    def tearDown(self):
        self.client = None

    def gen_votes(self):
        votings = [random.randint(1, 5000) for i in range(10)]
        users = [random.randint(1, 5000) for i in range(50)]
        for v in votings:
            a = random.randint(2, 500)
            b = random.randint(2, 500)
            data = {
                "voting": v,
                "voter": random.choice(users),
                "vote": { "a": a, "b": b }
            }
            self.client.post('/store/', data, format='json')

        return votings, users

    def test_store_vote(self):
        data = {
            "voting": 345,
            "voter": 1,
            "vote": { "a": 96, "b": 184 }
        }

        response = self.client.post('/store/', data, format='json')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(Vote.objects.count(), 1)
        self.assertEqual(Vote.objects.first().voting_id, 345)
        self.assertEqual(Vote.objects.first().voter_id, 1)
        self.assertEqual(Vote.objects.first().a, 96)
        self.assertEqual(Vote.objects.first().b, 184)

    def test_vote(self):
        self.gen_votes()

        response = self.client.get('/store/', format='json')
        self.assertEqual(response.status_code, 200)
        votes = response.json()

        self.assertEqual(len(votes), Vote.objects.count())
        self.assertEqual(votes[0], VoteSerializer(Vote.objects.all().first()).data)

    def test_filter(self):
        votings, voters = self.gen_votes()
        v = votings[0]

        response = self.client.get('/store/?voting_id={}'.format(v), format='json')
        self.assertEqual(response.status_code, 200)
        votes = response.json()

        self.assertEqual(len(votes), Vote.objects.filter(voting_id=v).count())

        v = voters[0]
        response = self.client.get('/store/?voter_id={}'.format(v), format='json')
        self.assertEqual(response.status_code, 200)
        votes = response.json()

        self.assertEqual(len(votes), Vote.objects.filter(voter_id=v).count())

    def test_hasvote(self):
        votings, voters = self.gen_votes()
        vo = Vote.objects.first()
        v = vo.voting_id
        u = vo.voter_id

        response = self.client.get('/store/?voting_id={}&voter_id={}'.format(v, u), format='json')
        self.assertEqual(response.status_code, 200)
        votes = response.json()

        self.assertEqual(len(votes), 1)
        self.assertEqual(votes[0]["voting_id"], v)
        self.assertEqual(votes[0]["voter_id"], u)
