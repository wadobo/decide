import random
import itertools

from django.core.management.base import BaseCommand

from mixnet.mixcrypt import MixCrypt
from mixnet.mixcrypt import ElGamal

from voting.models import Voting, Question, QuestionOption
from mixnet.models import Auth

from base import mods

from django.conf import settings
STORE = settings.APIS.get('store', settings.BASEURL)


class Command(BaseCommand):
    help = 'Test the full voting process with one auth (self)'

    def encrypt_msg(self, msg, v, bits=8):
        pk = v.pub_key
        p, g, y = (pk.p, pk.g, pk.y)
        k = MixCrypt(bits=bits)
        k.k = ElGamal.construct((p, g, y))
        return k.encrypt(msg)

    def create_voting(self):
        q = Question(desc='test question')
        q.save()
        for i in range(5):
            opt = QuestionOption(question=q, option='option {}'.format(i+1))
            opt.save()
        v = Voting(name='test voting', question=q)
        v.save()

        a, _ = Auth.objects.get_or_create(url=settings.BASEURL,
                                          defaults={'me': True, 'name': 'test auth'})
        a.save()
        v.auths.add(a)

        return v

    def store_votes(self, v):
        voter = 1
        clear = {}
        for opt in v.question.options.all():
            clear[opt.number] = 0
            for i in range(random.randint(0, 5)):
                a, b = self.encrypt_msg(opt.number, v)
                data = {
                    'voting': v.id,
                    'voter': voter,
                    'vote': { 'a': a, 'b': b },
                }
                clear[opt.number] += 1
                voter += 1
                mods.post('store', json=data)
        return clear

    def handle(self, *args, **options):
        print("Creating voting")
        v = self.create_voting()
        print("Creating pubkey")
        v.create_pubkey()

        print("Storing votes")
        clear = self.store_votes(v)
        print("Tally")
        v.tally_votes()

        tally = v.tally
        tally.sort()
        tally = {k: len(list(x)) for k, x in itertools.groupby(tally)}

        print("Result:")
        for q in v.question.options.all():
            print(" * {}: {} tally votes / {} emitted votes".format(q, tally.get(q.number, 0), clear.get(q.number, 0)))
