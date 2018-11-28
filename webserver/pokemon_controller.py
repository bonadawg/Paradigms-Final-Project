import cherrypy as cp
import re, json
from random import randint

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class PokemonController(object):
    def __init__(self, pdb):
        self.db = pdb
#        self.db.load_pokemon()

    def GET_POKEMON(self, name):
        output = {'result' : 'success'}
        
        if is_number(name):
            pok = self.db.get_pokemon(int(name))
        else:
            pok = self.db.get_pokemon(name.lower())
        if pok is None:
            output['result'] = 'error'
            output['message'] = 'Pokemon does not exist!'
        else:
            output['pokemon'] = pok
        return json.dumps(output)
    
    def GET_ALL(self):
        output = {'result' : 'success'}
        pokemon = self.db.get_all()
        ls = []       

        for key in pokemon:
            ls.append(pokemon[key])
    
        output['pokemon'] = ls
        return json.dumps(output) #returns the list of all pokemon in the database in json format

    def GET_BREEDABLE(self, name):
        output = {'result' : 'success'}
        breed_list = self.db.find_breedable(name)
        if breed_list is None:
            output['result'] = 'error'
            output['message'] = 'Pokemon does not exist!'
        else:
            output['breed_list'] = breed_list
        return json.dumps(output) #returns a list of all breedable pokemon in json format

    def GET_REC(self, name):
        output = {'result' : 'success'}
        pok = self.db.get_recommendation(name.lower())
        if pok is False:
            output['result'] = 'error'
            output['message'] = 'Pokemon does not exist!'
        else:
            output['recommendation'] = pok
        return json.dumps(output) #returns a recommended pokemon in json

    def GET_STATS(self, name, _stat):
        output = {'result' : 'success'}
        st = self.db.get_stat(name, stat=_stat)
        output['stat'] = st

        return json.dumps(output) #returns a specific stat for the pokemon in a list in a json

    def DELETE(self, name):
        output = {'result' : 'success'}
        
        res = self.db.delete_pokemon(name)

        if res:
            return json.dumps(output)
        else:
            ouput['result'] = 'error'
            output['message'] = 'Pokemon does not exist!'
        return json.dumps(output) #ensures the pokemon exists, then deletes it

    def POST(self, name):
        output = {'result' : 'success'}
        t = self.db.add_pokemon(name)

        return json.dumps(output) #posts a custom pokemon
