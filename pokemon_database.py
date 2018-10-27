import sys
import os
import requests

class pokemon_database:
    def __init__(self):
        #self.URL = 'https://www.kaggle.com/shikhar1/pokemon#pokemon.csv'
        self.URL = 'https://gist.githubusercontent.com/patrickwalls/53654aa26c19b09a1ebc66852acd69c7/raw/a32e46964c8849f9a891569adcff001c40b1cbcf/pokedex.csv'

    def load_pokemon(self):
        r = requests.get(self.URL)
        pok = r.text.splitlines()
        pok = [i.split(',')[1:-2] for i in pok[2:]]

        pok[35][1] = "Nidoran (male)"
        pok[38][1] = "Nidoran (female)" #male and female symbols not recognized, so had to be manually input"

        p = {}
        for j, i in enumerate(pok):
            for k, l in enumerate(i):
                if l == '-----':
                    pok[j][k] = None
            p[int(i[0][1:])] = i
            p[i[1]] = i

        return p
        

if __name__ == '__main__':
    
    p = pokemon_database()
    pok = p.load_pokemon()
    print(pok)
