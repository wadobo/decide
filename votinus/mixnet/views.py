from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MixnetSerializer
from .models import Auth, Mixnet, Key
from base.serializers import KeySerializer, AuthSerializer


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
         * voting: id
         * position: int / nullable
         * key: { "p": int, "g": int } / nullable
        """

        auths = request.data.get("auths")
        voting = request.data.get("voting")
        key = request.data.get("key", {"p": 0, "g": 0})
        position = request.data.get("position", 0)
        p, g = int(key["p"]), int(key["g"])

        dbauths = []
        for auth in auths:
            isme = auth["url"] == settings.BASEURL
            a, _ = Auth.objects.get_or_create(name=auth["name"],
                                              url=auth["url"],
                                              me=isme)
            dbauths.append(a)

        mn = Mixnet(voting_id=voting, auth_position=position)
        mn.save()

        for a in dbauths:
            mn.auths.add(a)

        mn.gen_key(p, g)

        data = { "key": { "p": mn.key.p, "g": mn.key.g } }
        # chained call to the next auth to gen the key
        resp = mn.chain_call("/", data)
        if resp:
            y = (resp["y"] * mn.key.y) % mn.key.p
        else:
            y = mn.key.y

        pubkey = Key(p=mn.key.p, g=mn.key.g, y=y)
        pubkey.save()
        mn.pubkey = pubkey
        mn.save()

        return  Response(KeySerializer(pubkey, many=False).data)


class Shuffle(APIView):

    def post(self, request, voting_id):
        """
         * voting_id: id
         * msgs: [ [int, int] ]
         * pk: { "p": int, "g": int, "y": int } / nullable
         * position: int / nullable
        """

        position = request.data.get("position", 0)
        mn = get_object_or_404(Mixnet, voting_id=voting_id, auth_position=position)

        msgs = request.data.get("msgs", [])
        pk = request.data.get("pk", None)
        if pk:
            p, g, y = pk["p"], pk["g"], pk["y"]
        else:
            p, g, y = mn.key.p, mn.key.g, mn.key.y

        msgs = mn.shuffle(msgs, (p, g, y))

        data = {
            "msgs": msgs,
            "pk": { "p": p, "g": g, "y": y },
        }
        # chained call to the next auth to gen the key
        resp = mn.chain_call("/shuffle/{}/".format(voting_id), data)
        if resp:
            msgs = resp

        return  Response(msgs)


class Decrypt(APIView):

    def post(self, request, voting_id):
        """
         * voting_id: id
         * msgs: [ [int, int] ]
         * pk: { "p": int, "g": int, "y": int } / nullable
         * position: int / nullable
        """

        position = request.data.get("position", 0)
        mn = get_object_or_404(Mixnet, voting_id=voting_id, auth_position=position)

        msgs = request.data.get("msgs", [])
        pk = request.data.get("pk", None)
        if pk:
            p, g, y = pk["p"], pk["g"], pk["y"]
        else:
            p, g, y = mn.key.p, mn.key.g, mn.key.y

        next_auths = mn.next_auths()
        last = next_auths.count() == 0

        # useful for tests only, to override the last value
        last = request.data.get("force-last", last)

        msgs = mn.decrypt(msgs, (p, g, y), last=last)

        data = {
            "msgs": msgs,
            "pk": { "p": p, "g": g, "y": y },
        }
        # chained call to the next auth to gen the key
        resp = mn.chain_call("/decrypt/{}/".format(voting_id), data)
        if resp:
            msgs = resp

        return  Response(msgs)
