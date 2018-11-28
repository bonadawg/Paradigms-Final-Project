import cherrypy
from _pokemon_database import pokemon_database
from pokemon_controller import PokemonController
import json

def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    conf = { 'global' : {'server.socket_host' : 'student04.cse.nd.edu', 'server.socket_port' : 52047 }, '/' : { 'request.dispatch' : dispatcher}}

    pdb = pokemon_database()
    dictController = PokemonController(pdb)
    # dispatcher shadows what was done in the cherrypy project
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
    start_service()

