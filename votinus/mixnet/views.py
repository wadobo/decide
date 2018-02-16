from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import MixnetSerializer, KeySerializer, AuthSerializer
from .models import Auth, Mixnet, Key

from django.conf import settings


# GEN_KEY ID, [AUTHS], k.p, k.g
# DECRYPT ID, [AUTHS], [msgs]
# SHUFFLE ID, [AUTHS], epk, [msgs]


class MixnetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows mixnets to be viewed or edited.
    """
    queryset = Mixnet.objects.all()
    serializer_class = MixnetSerializer

    def create(self, request):
        """
        This create a new mixnet and public key

         * auths: [ {"name": str, "url": str} ]
         * vote: id
         * key: { "p": int, "g": int } / nullable
        """

        auths = request.data.get("auths")
        vote = request.data.get("vote")
        key = request.data.get("key", {"p": 0, "g": 0})
        p, g = int(key["p"]), int(key["g"])

        dbauths = []
        for auth in auths:
            isme = auth["url"] == settings.BASEURL
            a, _ = Auth.objects.get_or_create(name=auth["name"],
                                              url=auth["url"],
                                              me=isme)
            dbauths.append(a)

        # TODO: avoid the creation of multiple Mixnets with the same
        # vote_id
        mn = Mixnet(vote_id=vote)
        mn.save()

        for a in dbauths:
            mn.auths.add(a)
        mn.save()

        mn.gen_key(p, g)

        data = { "key": { "p": mn.key.p, "g": mn.key.g } }
        # chained call to the next auth to gen the key
        resp = mn.chain_call("mixnet", data)
        if resp:
            y = (resp["y"] * mn.key.y) % mn.key.p
        else:
            y = mn.key.y

        pubkey = Key(p=mn.key.p, g=mn.key.g, y=y)
        pubkey.save()
        mn.pubkey = pubkey
        mn.save()

        return  Response(KeySerializer(pubkey, many=False).data)
