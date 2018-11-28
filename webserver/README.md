The webserver runs on port 52047.

This webserver connects to the database and provides information about the pokemon on it. In order to get all information about a pokemon, go to student04.cse.nd.edu:52047/pokemon/$POKEMON_NAME. In order to get a specific stat for that pokemon, go to student04.cse.nd.edu:52047/pokemon/POKEMON_NAME/STAT. In order to find breedable pokemon, go to student04.cse.nd.edu:52047/breedable/$POKEMON_NAME. In order to get information about all pokemon, go to student04.cse.nd.edu:52047/pokemon. In order to post a custom pokemon, send a post request to student04.cse.nd.edu:52047/pokemon. In order to delete a custom pokemon, send a delete request to student04.cse.nd.edu:52047/pokemon/$POKEMON_NAME. Lastly, in order to get a recommendation to fight against a pokemon, go to student04.cse.nd.edu:52047/recommend/$POKEMON_NAME.


JSON RESTful:

|Command | Resource           | Input Example    | Output Example                                              |
|--------|--------------------|------------------|-------------------------------------------------------------|
|GET     | /pokemon/          |                  | {'result':'success', 'pokemon': [{'Dex #': '#001', ...}...]}|
|GET     | /pokemon/:id       |                  | {'result':'success', 'pokemon': [{'Dex #': '#001', ...}}    |
|POST    | /pokemon/:id       | {'pokemon': :id} | {'result': 'success'}                                       |
|DELETE  | /pokemon/:id       |                  | {'result': 'success'}                                       |
|GET     | /breedable/:id     |                  | {'result': 'success', 'breed_list': ['#001 Bulbasaur'...]}  |
|GET     | /pokemon/:id/:stat |                  | {'result': 'success', 'stat': [['#212', 'Scizor', 100']]}   |
|GET     | /recommend/:id     |                  | {'result': 'success', 'recommendation': 'Psyduck'}          |