import unittest
import requests
import json

class TestCherrypyPrimer(unittest.TestCase):

        SITE_URL = 'http://student04.cse.nd.edu:52047' #Replace this with your port number 52MMM 
        
        DICT_URL = SITE_URL + '/pokemon/'
        REC_URL = SITE_URL + '/recommend/'
        BREED_URL = SITE_URL + '/breedable/'

        def reset_data(self):
                r = requests.delete(self.DICT_URL)

        def is_json(self, resp):
                try:
                        json.loads(resp)
                        return True
                except ValueError:
                        return False

        def test_pokemon_get(self): #tests a get request for a pokemon
                key = 'scizor'
                r = requests.get(self.DICT_URL + key)
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['pokemon']['Pokemon'], 'Scizor')

        def test_dict_put(self): #tests a post request for a new pokemon
                key = 'bonadawg'

                r = requests.post(self.DICT_URL + key, data = json.dumps({}))
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                r = requests.get(self.DICT_URL + key)
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['pokemon']['Pokemon'], key)

        def test_dict_delete(self): #tests a post and delete request for pokemon
                key = 'sean'

                r = requests.post(self.DICT_URL + key, data = json.dumps({}))
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                r = requests.delete(self.DICT_URL + key)
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

        def test_breed_get(self): #tests getting breedable pokemon

                key = 'scizor'

                r = requests.get(self.BREED_URL + key)
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

        def test_rec_get(self): #tests getting a recommendation

                key = 'scizor'

                r = requests.get(self.REC_URL + key)
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

        def test_stat_get(self): #tests getting a pokemon's stats

                key = 'scizor'

                r = requests.get(self.DICT_URL + key + '/defense')
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                r = requests.get(self.DICT_URL + key + '/attack')
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                r = requests.get(self.DICT_URL + key + '/hp')
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                r = requests.get(self.DICT_URL + key + '/speed')
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

if __name__ == "__main__":
        unittest.main()

