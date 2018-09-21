from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404

from base import mods


# TODO: check permissions and census
class BoothView(TemplateView):
    template_name = 'booth/booth.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        try:
            r = mods.get('voting', params={'id': vid})
            context['voting'] = r[0]
        except:
            raise Http404

        context['store_url'] = settings.APIS.get('store', settings.BASEURL)
        context['auth_url'] = settings.APIS.get('authentication', settings.BASEURL)
        context['KEYBITS'] = settings.KEYBITS

        return context
