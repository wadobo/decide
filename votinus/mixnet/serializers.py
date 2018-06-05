from rest_framework import serializers

from .models import Mixnet
from base.serializers import AuthSerializer, KeySerializer


class MixnetSerializer(serializers.HyperlinkedModelSerializer):
    auths = AuthSerializer(many=True)
    pubkey = KeySerializer()

    class Meta:
        model = Mixnet
        fields = ('voting_id', 'auths', 'pubkey')
