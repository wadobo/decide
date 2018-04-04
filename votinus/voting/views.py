import django_filters.rest_framework
from rest_framework.response import Response
from rest_framework import generics

from .models import Voting
from .serializers import VotingSerializer


class VotingView(generics.ListAPIView):
    queryset = Voting.objects.all()
    serializer_class = VotingSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('id', )
