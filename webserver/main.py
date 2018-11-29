import cherrypy
from _pokemon_database import pokemon_database
from pokemon_controller import PokemonController
import json

class OptionsController:
    def OPTIONS(self, *args, **kargs):
        return ""

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "*"

def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    conf = { 'global' : {'server.socket_host' : 'student04.cse.nd.edu', 'server.socket_port' : 52047 }, '/' : { 'request.dispatch' : dispatcher, 'tools.CORS.on' : True}}

    pdb = pokemon_database()
    dictController = PokemonController(pdb)
    optController = OptionsController()
    # dispatcher shadows what was done in the cherrypy project

    dispatcher.connect('opt_get', '/pokemon/:name', controller=optController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('opt_get_all', '/pokemon/', controller=optController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('opt_get_b', '/breedable/:name', controller=optController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('opt_stat', '/pokemon/:name/:_stat', controller=optController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('opt_rec', '/recommend/:name', controller=optController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    
    dispatcher.connect('poke_get', '/pokemon/:name', controller=dictController, action='GET_POKEMON', conditions=dict(method=['GET']))
    dispatcher.connect('poke_get_all', '/pokemon/', controller=dictController, action='GET_ALL', conditions=dict(method=['GET']))
    dispatcher.connect('poke_get_all', '/breedable/:name', controller=dictController, action='GET_BREEDABLE', conditions=dict(method=['GET']))
    dispatcher.connect('poke_post', '/pokemon/:name', controller=dictController, action='POST', conditions=dict(method=['POST']))
    dispatcher.connect('poke_stat', '/pokemon/:name/:_stat', controller=dictController, action='GET_STATS', conditions=dict(method=['GET']))
    dispatcher.connect('poke_rec', '/recommend/:name', controller=dictController, action='GET_REC', conditions=dict(method=['GET']))
    dispatcher.connect('poke_del', '/pokemon/:name', controller=dictController, action='DELETE', conditions=dict(method=['DELETE']))

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)


if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    start_service()

