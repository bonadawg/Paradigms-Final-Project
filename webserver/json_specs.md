|Command | Resource           | Input Example    | Output Example                                              |
|--------|--------------------|------------------|-------------------------------------------------------------|
|GET     | /pokemon/          |                  | {'result':'success', 'pokemon': [{'Dex #': '#001', ...}...]}|
|GET     | /pokemon/:id       |                  | {'result':'success', 'pokemon': [{'Dex #': '#001', ...}}    |
|POST    | /pokemon/:id       | {'pokemon': :id} | {'result': 'success'}                                       |
|DELETE  | /pokemon/:id       |                  | {'result': 'success'}                                       |
|GET     | /breedable/:id     |                  | {'result': 'success', 'breed_list': ['#001 Bulbasaur'...]}  |
|GET     | /pokemon/:id/:stat |                  | {'result': 'success', 'stat': [['#212', 'Scizor', 100']]}   |
|GET     | /recommend/:id     |                  | {'result': 'success', 'recommendation': 'Psyduck'}          |