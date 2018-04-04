import requests

from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404


# TODO: check permissions and census
class BoothView(TemplateView):
    template_name = 'booth/booth.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        VOTING = settings.APIS.get('voting', settings.BASEURL)
        try:
            response = requests.get('{}/voting/?id={}'.format(VOTING, vid))
            context['voting'] = response.json()[0]
        except:
            raise Http404

        context['store_url'] = settings.APIS.get('store', settings.BASEURL)
        context['auth_url'] = settings.APIS.get('authentication', settings.BASEURL)

        return context
