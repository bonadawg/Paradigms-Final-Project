James Bonadonna, Sean Michalec, Chris Heneghan

The API works by parsing the data from the URL and creating different ways to access it, then having those different access methods get called by the main class and give data to the user from the server.

Run the server using the command: /afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 main.py

The webserver runs on port 52047.

This webserver connects to the database and provides information about the pokemon on it. In order to get all information about a pokemon, go to student04.cse.nd.edu:52047/pokemon/$POKEMON_NAME. In order to get a specific stat for that pokemon, go to student04.cse.nd.edu:52047/pokemon/POKEMON_NAME/STAT. In order to find breedable pokemon, go to student04.cse.nd.edu:52047/breedable/$POKEMON_NAME. In order to get information about all pokemon, go to student04.cse.nd.edu:52047/pokemon. In order to post a custom pokemon, send a post request to student04.cse.nd.edu:52047/pokemon. In order to delete a custom pokemon, send a delete request to student04.cse.nd.edu:52047/pokemon/$POKEMON_NAME. Lastly, in order to get a recommendation to fight against a pokemon, go to student04.cse.nd.edu:52047/recommend/$POKEMON_NAME.

The json RESTful table is shown below and also in the webserver/json_specs.md file.

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

The client is located at http://student04.cse.nd.edu/jbonadon/GK03gwaD/final_project/client_1/

Use the dropdown menu to select a feature, then hit 'Go!' The client will either prompt the user to enter more information i.e. a pokemon name, or will display the results. In order to get the results of an entered name, hit the 'Find!' button under the input box(es).
