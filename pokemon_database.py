import sys
import os
import requests

class pokemon_database:
    def __init__(self):
        #self.URL = 'https://www.kaggle.com/shikhar1/pokemon#pokemon.csv'
        self.URL = 'https://gist.githubusercontent.com/patrickwalls/53654aa26c19b09a1ebc66852acd69c7/raw/a32e46964c8849f9a891569adcff001c40b1cbcf/pokedex.csv'

    def load_pokemon(self):
        r = requests.get(self.URL)
        
        return r.text.splitlines()
        

if __name__ == '__main__':
    
    p = pokemon_database()

    pokemon = p.load_pokemon()
    print(pokemon)
    
