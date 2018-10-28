import sys
import os
import requests
import types

class pokemon_database:
    def __init__(self):
        #self.URL = 'https://www.kaggle.com/shikhar1/pokemon#pokemon.csv'
        self.URL = 'https://raw.githubusercontent.com/bonadawg/pokedex/master/pokedex.csv'

    def load_pokemon(self):
        r = requests.get(self.URL)
        pok = r.text.splitlines()
        pok = [i.split(',')[1:-2] for i in pok[2:]]
    
        p = {}
        n = {}
        for j, i in enumerate(pok):
            for k, l in enumerate(i):
                if l == '-----':
                    pok[j][k] = None #file has '-----' when it is none, so made it a none object
            i[11:] = [int(x) for x in i[11:]] #makes all base stats integers
            if i[1] in p:
                n[int(i[0][1:])].append(i) #removes the # sign in order to make it an int
                p[i[1]].append(i) #add both name and number as access types to the dict
            else:
                n[int(i[0][1:])] = [i] #removes the # sign in order to make it an int
                p[i[1]] = [i] #add both name and number as access types to the dict

        return [n,p]

    def get_highest(self, stat, pok):
        stat = stat.lower()
        if stat == 'hp':
            return self.calculate_highest(11, pok)
        elif stat == 'attack' or stat == 'atk':
            return self.calculate_highest(12, pok)
        elif stat == 'defense' or stat == 'def':
            return self.calculate_highest(13, pok)
        elif stat == 'special attack' or stat == 'sp. attack' or stat == 'sp attack' or stat == 'sp atk' or stat == 'sp. atk':
            return self.calculate_highest(14, pok)
        elif stat == 'special defense' or stat == 'sp. defense' or stat == 'sp defense' or stat == 'sp def' or stat == 'sp. def':
            return self.calculate_highest(15, pok)
        elif stat == 'speed' or stat == 'spd':
            return self.calculate_highest(16, pok)

    def calculate_highest(self, stat, pok):
        high = [[0] * 18]
        for i in range(1, 722):
            for c in pok[i]:
                if c[stat] > high[0][stat]:
                    high = [c]
                elif c[stat] == high[0][stat]:
                    high.append(c)

        return high

if __name__ == '__main__':
    
    p = pokemon_database()
    pok = p.load_pokemon()
    #print(pok)
    for h in p.get_highest('def', pok[0]):
        print(h)
