from rest_framework import serializers

from .models import Auth, Key


class AuthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Auth
        fields = ('name', 'url', 'me')


class KeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Key
        fields = ('p', 'g', 'y')
