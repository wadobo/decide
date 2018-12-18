from rest_framework.views import APIView
from rest_framework.response import Response
from base import mods


class Gateway(APIView):
    def get(self, request, submodule, route):
        kwargs = {'HTTP_AUTHORIZATION': request.META.get('HTTP_AUTHORIZATION', '')}
        kwargs['params'] = {k: v for k, v in request.data.items()}
        resp = mods.query(submodule, route, method='get', response=True, **kwargs)
        return Response(resp.json(), status=resp.status_code)

    def post(self, request, submodule, route):
        kwargs = {'HTTP_AUTHORIZATION': request.META.get('HTTP_AUTHORIZATION', '')}
        kwargs['json'] = {k: v for k, v in request.data.items()}

        resp = mods.query(submodule, route, method='post', response=True, **kwargs)
        return Response(resp.json(), status=resp.status_code)
