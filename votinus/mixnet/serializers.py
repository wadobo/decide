from rest_framework import serializers

from .models import Auth, Mixnet, Key


class AuthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Auth
        fields = ('name', 'url', 'me')


class KeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Key
        fields = ('p', 'g', 'y')


class MixnetSerializer(serializers.HyperlinkedModelSerializer):
    auths = AuthSerializer(many=True)
    pubkey = KeySerializer()

    class Meta:
        model = Mixnet
        fields = ('vote_id', 'auths', 'pubkey')
