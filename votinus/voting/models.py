import requests

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings

from mixnet.models import Auth, Key


class Question(models.Model):
    desc = models.TextField()

    def __str__(self):
        return self.desc


class QuestionOption(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    number = models.PositiveIntegerField(blank=True, null=True)
    option = models.TextField()

    def save(self):
        if not self.number:
            self.number = self.question.options.count() + 2
        return super().save()

    def __str__(self):
        return '{} ({})'.format(self.option, self.number)


class Voting(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True, null=True)
    question = models.ForeignKey(Question, related_name='voting', on_delete=models.CASCADE)

    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    pub_key = models.OneToOneField(Key, related_name='voting', blank=True, null=True, on_delete=models.SET_NULL)
    auths = models.ManyToManyField(Auth, related_name='votings')

    tally = JSONField(blank=True, null=True)
    postproc = JSONField(blank=True, null=True)

    def create_pubkey(self):
        if self.pub_key or not self.auths.count():
            return

        auth = self.auths.first()
        url = "{}/mixnet/".format(auth.url)
        data = {
            "voting": self.id,
            "auths": [ {"name": a.name, "url": a.url} for a in self.auths.all() ],
        }
        resp = requests.post(url, json=data)
        key = resp.json()
        pk = Key(p=key["p"], g=key["g"], y=key["y"])
        pk.save()
        self.pub_key = pk
        self.save()

    def get_votes(self):
        STORE = settings.APIS.get('store', settings.BASEURL)
        # gettings votes from store
        response = requests.get('{}/store/?voting_id={}'.format(STORE, self.id))
        votes = response.json()
        # anon votes
        return [[i['a'], i['b']] for i in votes]

    def tally_votes(self):
        '''
        The tally is a shuffle and then a decrypt
        '''

        votes = self.get_votes()

        auth = self.auths.first()
        shuffle_url = "{}/mixnet/shuffle/{}/".format(auth.url, self.id)
        decrypt_url = "{}/mixnet/decrypt/{}/".format(auth.url, self.id)
        auths = [{"name": a.name, "url": a.url} for a in self.auths.all()]

        # first, we do the shuffle
        data = { "msgs": votes }
        resp = requests.post(shuffle_url, json=data)
        shuffled = resp.json()
        # then, we can decrypt that
        data = { "msgs": shuffled }
        response = requests.post(decrypt_url, json=data)
        clear = response.json()

        self.tally = clear
        self.save()

    def __str__(self):
        return self.name
