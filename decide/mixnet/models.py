from django.db import models

from .mixcrypt import MixCrypt

from base import mods
from base.models import Auth, Key
from base.serializers import AuthSerializer
from django.conf import settings


# number of bits for the key, all auths should use the same number of bits
B = settings.KEYBITS


class Mixnet(models.Model):
    voting_id = models.PositiveIntegerField()
    auth_position = models.PositiveIntegerField(default=0)
    auths = models.ManyToManyField(Auth, related_name="mixnets")
    key = models.ForeignKey(Key, blank=True, null=True,
                            related_name="mixnets",
                            on_delete=models.SET_NULL)
    pubkey = models.ForeignKey(Key, blank=True, null=True,
                               related_name="mixnets_pub",
                               on_delete=models.SET_NULL)

    def __str__(self):
        auths = ", ".join(a.name for a in self.auths.all())
        return "Voting: {}, Auths: {}\nPubKey: {}".format(self.voting_id,
                                                          auths, self.pubkey)

    def shuffle(self, msgs, pk):
        crypt = MixCrypt(bits=B)
        k = crypt.setk(self.key.p, self.key.g, self.key.y, self.key.x)

        return crypt.shuffle(msgs, pk)

    def decrypt(self, msgs, pk, last=False):
        crypt = MixCrypt(bits=B)
        k = crypt.setk(self.key.p, self.key.g, self.key.y, self.key.x)
        return crypt.shuffle_decrypt(msgs, last)

    def gen_key(self, p=0, g=0):
        crypt = MixCrypt(bits=B)
        if self.key:
            k = crypt.setk(self.key.p, self.key.g, self.key.y, self.key.x)
        elif (not g or not p):
            k = crypt.genk()
            key = Key(p=int(k.p), g=int(k.g), y=int(k.y), x=int(k.x))
            key.save()

            self.key = key
            self.save()
        else:
            k = crypt.getk(p, g)
            key = Key(p=int(k.p), g=int(k.g), y=int(k.y), x=int(k.x))
            key.save()

            self.key = key
            self.save()

    def chain_call(self, path, data):
        next_auths=self.next_auths()

        data.update({
            "auths": AuthSerializer(next_auths, many=True).data,
            "voting": self.voting_id,
            "position": self.auth_position + 1,
        })

        if next_auths:
            auth = next_auths.first().url
            r = mods.post('mixnet', entry_point=path,
                           baseurl=auth, json=data)
            return r

        return None

    def next_auths(self):
        next_auths = self.auths.filter(me=False)

        if self.auths.count() == next_auths.count():
            next_auths = next_auths[1:]

        return next_auths
