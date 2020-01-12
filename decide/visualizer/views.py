import json
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from base import mods


class VisualizerView(TemplateView):
    template_name = 'visualizer/visualizer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        try:
            r = mods.get('voting', params={'id': vid})
            context['voting'] = json.dumps(r[0])
            listaVotaciones = from_json(self.prueba(self))
            i=0
            votos=0
            while i < len(listaVotaciones) :
                votos= votos + listaVotaciones[i].votes
                i=i+1
            j=0
            listMedia=[]
            while j < len(listaVotaciones) :
        
                media = listaVotaciones[j].votes / votos
                listMedia.append(media)
                j=j+1
            context['prueba'] = listMedia
            context['contador'] = votos
            context['mirando'] = json.dumps(r[0])
        except:
            raise Http404

        return context
    def prueba(self,request):
        
        stringprueba = '''
                [ { "votes": 1, "number": 2, "option": "dos", "postproc": 1 },
                { "votes": 1, "number": 3, "option": "trs", "postproc": 1 }, 
                { "votes": 0, "number": 1, "option": "uno", "postproc": 0 } ] 
                '''
        return stringprueba

def prueba(request):
        receptor = request.POST['receptor']
        encuesta = request.POST['encuesta'] 
        encuestaID = request.POST['encuestaID']  
        resultadosEncuesta = request.POST['resultadosEncuesta']

        fromjson = from_json(resultadosEncuesta)
        texto = ""
        for x in range(len(fromjson)):
            texto = texto + str(fromjson[x]) + "\n"


        
        
        send_mail('Resultados de la encuesta "' + encuesta + '" de DECIDE',
        'Se adjuntan a contuniacion los resultado de la encuesta "'+ encuesta + '":\n\n' + texto,
        'decide123456789@gmail.com',
        [receptor],
        fail_silently = False)
        messages.add_message(request, messages.SUCCESS, "El email ha sido enviado!") 

        return redirect('/visualizer/'+encuestaID)





class ResultadosVotacion:
    def __init__(self, votes, number, option, postproc):
        self.votes = votes
        self.number = number
        self.option = option
        self.postproc = postproc

    

    def __repr__(self):
        return f'{self.option} : {self.votes}' 





def from_json(json_string):
        votaciones_list = []
        votaciones_data = json.loads(json_string)
        for u in votaciones_data:
            votaciones_list.append(ResultadosVotacion(**u))
        return votaciones_list

