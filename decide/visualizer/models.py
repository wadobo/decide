from django.db import models
import json 
import numpy as np
 
class ResultadosVotacion:

    def __init__(self,votes,number,option,postproc):
        self.votes =votes 
        self.number = number
        self.option = option
        self.postproc = postproc
       
     

        
stringprueba = '''
[ { "votes": 1, "number": 2, "option": "dos", "postproc": 1 },
 { "votes": 1, "number": 3, "option": "trs", "postproc": 1 }, 
 { "votes": 0, "number": 1, "option": "uno", "postproc": 0 } ] 
'''
def from_json(json_string):
        user_list=[]
        user_data = json.loads(json_string)
        for u in user_data:
            user_list.append(ResultadosVotacion(**u))
        return user_list
def contador(json_string):
    user_list=[]
    user_data = json.loads(json_string)
    listaVotaciones = from_json(json_string)

    i=0
    votos=0
    while i < len(listaVotaciones) :
        votos= votos + listaVotaciones[i].votes
        i=i+1
    return votos

def porcentajeVotos(json_string):
    numero= contador(json_string)
    user_list=[]
    user_data = json.loads(json_string)
    listaVotaciones = from_json(json_string)
    listMedia=[]
    for u in user_data:
            user_list.append(ResultadosVotacion(**u))
    i=0
   
    while i < len(listaVotaciones) :
        
        media = listaVotaciones[i].votes / numero
        listMedia.append(media)
        i=i+1

   
    return listMedia
    