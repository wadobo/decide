from django.utils import timezone
from django.utils.dateparse import parse_datetime
import django_filters.rest_framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from .models import Vote
from .serializers import VoteSerializer
from base import mods
from base.perms import UserIsStaff


class StoreView(generics.ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('voting_id', 'voter_id')

    def get(self, request):
        self.permission_classes = (UserIsStaff,)
        self.check_permissions(request)
        return super().get(request)

    def post(self, request):
        """
         * voting: id
         * voter: id
         * vote: { "a": int, "b": int }
        """

        vid = request.data.get('voting')
        voting = mods.get('voting', params={'id': vid})
        if not voting or not isinstance(voting, list):
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)
        start_date = voting[0].get('start_date', None)
        end_date = voting[0].get('end_date', None)
        not_started = not start_date or timezone.now() < parse_datetime(start_date)
        is_closed = end_date and parse_datetime(end_date) < timezone.now()
        if not_started or is_closed:
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)

        uid = request.data.get('voter')
        vote = request.data.get('vote')

        if not vid or not uid or not vote:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        # validating voter
        token = request.auth.key
        voter = mods.post('authentication', entry_point='/getuser/', json={'token': token})
        voter_id = voter.get('id', None)
        if not voter_id or voter_id != uid:
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)

        # the user is in the census
        perms = mods.get('census/{}'.format(vid), params={'voter_id': uid}, response=True)
        if perms.status_code == 401:
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)

        a = vote.get("a")
        b = vote.get("b")

        defs = { "a": a, "b": b }
        v, _ = Vote.objects.get_or_create(voting_id=vid, voter_id=uid,
                                          defaults=defs)
        v.a = a
        v.b = b

        v.save()

        return  Response({})
