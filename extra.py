#James Bonadonna, Sean Michalec, Chris Heneghan
#Paradigms Final Project Backend

import sys
import os
import requests
import types

class pokemon_database:
    def __init__(self):
        self.URL = 'https://raw.githubusercontent.com/bonadawg/pokedex/master/pokedex-v2.csv'

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
            if i[1].lower() in p:
                n[int(i[0][1:])].append(i) #removes the # sign in order to make it an int
                p[i[1].lower()].append(i) #add both name and number as access types to the dict
            else:
                n[int(i[0][1:])] = [i] #removes the # sign in order to make it an int
                p[i[1].lower()] = [i] #add both name and number as access types to the dict

        return [n,p]

    def get_highest(self, stat="", pok=None):
        if not pok:
            pok = self.load_pokemon()
            pok = pok[0]

        stat = stat.lower()
        if stat == "": #returns sum of base stats
            return self.calculate_highest(17, pok)
        elif stat == 'hp':
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
        else:
            return None

    def calculate_highest(self, stat, pok):
        high = [[0] * 18]
        for i in range(1, 722):
            for c in pok[i]:
                if c[stat] > high[0][stat]:
                    high = [c]
                elif c[stat] == high[0][stat]:
                    high.append(c)

        high.append(stat)
        return high

    def get_stat(self, mon=212, stat="", pok=None):
        if not pok:
            pok = self.load_pokemon()
            if type(mon) is int:
                pok = pok[0]
            else:
                pok = pok[1]

        if stat == "": #returns sum of base stats
            return self.return_stat(17, mon, pok)
        elif stat == 'hp':
            return self.return_stat(11, mon, pok)
        elif stat == 'attack' or stat == 'atk':
            return self.return_stat(12, mon, pok)
        elif stat == 'defense' or stat == 'def':
            return self.return_stat(13, mon, pok)
        elif stat == 'special attack' or stat == 'sp. attack' or stat == 'sp attack' or stat == 'sp atk' or stat == 'sp. atk':
            return self.return_stat(14, mon, pok)
        elif stat == 'special defense' or stat == 'sp. defense' or stat == 'sp defense' or stat == 'sp def' or stat == 'sp. def':
            return self.return_stat(15, mon, pok)
        elif stat == 'speed' or stat == 'spd':
            return self.return_stat(16, mon, pok)
        else:
            return None

    def return_stat(self, stat, mon, pok):
        stats = []
        for c in pok[mon]:
            if c[2] != 'Normal':
                temp = c[2] + ' ' + c[1]
                stats.append([c[0], temp, c[stat]])
            else:
                stats.append([c[0], c[1], c[stat]])

        return stats

    def get_pokemon(self, mon=212, pok=None):
        if not pok:
            pok = self.load_pokemon()
            if type(mon) is int:
                pok = pok[0]
            else:
                pok = pok[1]
        return pok[mon]

    def find_breedable(self, mon=212, pok=None):
        if not pok:
            pok = self.load_pokemon()
            if type(mon) != int:
                mon = int(pok[1][mon][0][0][1:])
            pok = pok[0]

        breeds = [pok[mon][0][9], pok[mon][0][10]]
        mates = []
        both = True
        if not breeds[0]:
            return None
        if not breeds[1]:
            both = False
            breeds = breeds[0]

        if both:
            for i in range(1, 722):
                if pok[i][0][9] == breeds[0] or pok[i][0][9] == breeds[1] or pok[i][0][10] == breeds[0] or pok[i][0][10] == breeds[1]:
                    mates.append(pok[i][0][0] + " " + pok[i][0][1])
        else:
            for i in range(1, 722):
                if pok[i][0][9] == breeds or pok[i][0][10] == breeds:
                    mates.append(pok[i][0][0] + " " + pok[i][0][1])

        return mates

    def new_pokemon(self, name):
        pass

    def delete_pokemon(self, mon):
        pass

