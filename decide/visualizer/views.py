import json
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404

from base import mods


class VisualizerView(TemplateView):
    template_name = 'visualizer/visualizer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        try:
            r = mods.get('voting', params={'id': vid})
            context['voting'] = json.dumps(r[0])
            
        except:
            raise Http404

        return context
    def contador(self,request):
        resultadosEncuesta = request.POST['resultadosEncuesta']
        fromjson = from_json(resultadosEncuesta)
        user_list=[]
        user_data = json.loads(fromjson)
        listaVotaciones = from_json(fromjson)

        i=0
        votos=0
        while i < len(listaVotaciones) :
            votos= votos + listaVotaciones[i].votes
            i=i+1
        return votos
    def porcentaje(self,request): 
        resultadosEncuesta = request.POST['resultadosEncuesta']

        fromjson = from_json(resultadosEncuesta)
        
        numero= contador(fromjson)
        user_list=[]
        user_data = json.loads(fromjson)
        listaVotaciones = from_json(fromjson)
        listMedia=[]
        for  u in user_data:
            user_list.append(ResultadosVotacion(**u))
        i=0
   
        while i < len(listaVotaciones) :
        
            media = listaVotaciones[i].votes / numero
            listMedia.append(media)
            i=i+1

        
        return listaVotaciones




class ResultadosVotacion:
    def __init__(self, votes, number, option, postproc,porcentaje):
        self.votes = votes
        self.number = number
        self.option = option
        self.postproc = postproc
        self.porcentaje = porcentaje
    

    def __repr__(self):
        return f'{self.option} : {self.votes}' 





def from_json(json_string):
        votaciones_list = []
        votaciones_data = json.loads(json_string)
        for u in votaciones_data:
            votaciones_list.append(ResultadosVotacion(**u))
        return votaciones_list