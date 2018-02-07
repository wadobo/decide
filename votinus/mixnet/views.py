from rest_framework.response import Response
from rest_framework.views import APIView


class GenerateKey(APIView):

    def get(self, request, id_votation, format=None):
        return Response('qwe')
