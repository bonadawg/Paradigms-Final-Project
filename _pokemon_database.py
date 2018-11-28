#James Bonadonna, Sean Michalec, Chris Heneghan
#Paradigms Final Project Backend

import sys
import os
import requests
import types

class pokemon_database:
    def __init__(self):
        self.URL = 'https://raw.githubusercontent.com/bonadawg/pokedex/master/pokedex-v2.csv'
        self.byNum = {}
        self.byName = {}
        self.vals = []

        r = requests.get(self.URL)
        pok = r.text.splitlines()
        self.vals = pok[0].split(',')[1:-2]
        pok = [i.split(',')[1:-2] for i in pok[2:]]
    
        p = {}
        n = {}

        for j, i in enumerate(pok):
            temp = {}
            for k, l in enumerate(i):
                if l == '-----':
                    pok[j][k] = None #file has '-----' when it is none, so made it a none object
            i[11:] = [int(x) for x in i[11:]] #makes all base stats integers
            for pos, stat in enumerate(i):
                temp[self.vals[pos]] = stat
            if i[1].lower() in p:
                p[i[2].lower() + ' ' + i[1].lower()] = temp #add both name and number as access types to the dict
            else:
                n[int(i[0][1:])] = temp #removes the # sign in order to make it an int
                p[i[1].lower()] = temp #add both name and number as access types to the dict
            
        self.byNum = n
        self.byName = p

    def get_highest(self, stat=""):

        stat = stat.lower()
        if stat == "": #returns sum of base stats
            return self.calculate_highest('Total Stats')
        elif stat == 'hp':
            return self.calculate_highest('Base HP')
        elif stat == 'attack' or stat == 'atk':
            return self.calculate_highest('Base Atk')
        elif stat == 'defense' or stat == 'def':
            return self.calculate_highest('Base Def')
        elif stat == 'special attack' or stat == 'sp. attack' or stat == 'sp attack' or stat == 'sp atk' or stat == 'sp. atk':
            return self.calculate_highest('Base Sp Atk')
        elif stat == 'special defense' or stat == 'sp. defense' or stat == 'sp defense' or stat == 'sp def' or stat == 'sp. def':
            return self.calculate_highest('Base Sp Def')
        elif stat == 'speed' or stat == 'spd':
            return self.calculate_highest('Base Spd')
        else:
            return None

    def calculate_highest(self, stat):
        high = [{stat: 0}]
        for i in range(1, len(self.byNum)):
                if pok.byNum[i][stat] > high[stat]:
                    high = [c]
                elif pok.byNum[i][stat] == high[stat]:
                    high.append(c)

        high.append(stat)
        return high

    def get_stat(self, mon=212, stat=""):
        if stat == "": #returns sum of base stats
            return self.return_stat('Total Stats', mon)
        elif stat == 'hp':
            return self.return_stat('Base HP', mon)
        elif stat == 'attack' or stat == 'atk':
            return self.return_stat('Base Atk', mon)
        elif stat == 'defense' or stat == 'def':
            return self.return_stat('Base Def', mon)
        elif stat == 'special_attack' or stat == 'specialattack' or stat == 'sp_attack' or stat == 'sp_atk' or stat == 'spatk':
            return self.return_stat('Base Sp Atk', mon)
        elif stat == 'special_defense' or stat == 'specialdefense' or stat == 'sp_defense' or stat == 'sp_def' or stat == 'spdef':
            return self.return_stat('Base Sp Def', mon)
        elif stat == 'speed' or stat == 'spd':
            return self.return_stat('Base Spd', mon)
        else:
            return None

    def return_stat(self, stat, mon):
        if type(mon) is int:
            pok = self.byNum
        else:
            pok = self.byName
            mon = mon.lower()

        stats = []
        if pok[mon]['Forme'] != 'Normal':
            temp = pok[mon]['Forme'] + ' ' + pok[mon]['Pokemon']
            stats.append([pok[mon]['Dex #'], temp, pok[mon][stat]])
        else:
            stats.append([pok[mon]['Dex #'], pok[mon]['Pokemon'], pok[mon][stat]])

        return stats

    def get_length(self):
        return len(self.byName)

    def get_pokemon(self, mon=212):
        if type(mon) is int:
            return self.byNum[mon]
        else:
            return self.byName[mon]

    def get_all(self):
        return self.byNum

    def find_breedable(self, mon=212):
        try:
            int(mon)
        except:
            str(mon)

        if type(mon) is not int:
            mon = int(self.byName[mon]['Dex #'][1:])
        pok = self.byNum

        breeds = [pok[mon]['Egg Group 1'], pok[mon]['Egg Group 2']]
        mates = []
        both = True
        if not breeds[0]:
            return None
        if not breeds[1]:
            both = False
            breeds = breeds[0]

        if both:
            for i in range(1, len(self.byNum)):
                if pok[i]['Egg Group 1'] == breeds[0] or pok[i]['Egg Group 1'] == breeds[1] or pok[i]['Egg Group 2'] == breeds[0] or pok[i]['Egg Group 2'] == breeds[1]:
                    mates.append(pok[i]['Dex #'] + " " + pok[i]['Pokemon'])
        else:
            for i in range(1, len(self.byNum)):
                if pok[i]['Egg Group 1'] == breeds or pok[i]['Egg Group 2'] == breeds:
                    mates.append(pok[i]['Dex #'] + " " + pok[i]['Pokemon'])

        return mates

    def add_pokemon(self, mon):
        temp = {}
        temp['Dex #'] = len(self.byNum) + 1
        temp['Pokemon'] = mon
        temp['Forme'] = 'Custom'
        temp['Type 1'] = 'Normal'
        temp['Type 2'] = None
        temp['Ability 1'] = 'Simple'
        temp['Ability 2'] = None
        temp['Hidden Ability'] = 'Adaptability'
        temp['Evolution Details'] = None
        temp['Egg Group 1'] = None
        temp['Egg Group 2'] = None
        for i in range(11, 18):
            temp[self.vals[i]] = 90
        temp['Total Stats'] = 540
        
        self.byNum[len(self.byNum) + 1] = temp
        self.byName[mon.lower()] = temp

        return temp

    def delete_pokemon(self, mon):
        if mon.lower() in self.byName.keys() and self.byName[mon.lower()]['Forme'] == 'Custom':
            loc = self.byName[mon.lower()]['Dex #']
            del self.byName[mon.lower()]
            del self.byNum[loc]
            return True
        else:
            return False

