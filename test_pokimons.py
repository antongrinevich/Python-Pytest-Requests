import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '47c598021c15792e61a55e7283aac6f7'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '27470'

def test_status_kod():
    response = requests.get(url = f'{URL}/pokemons', params= {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_respons():
    response_get = requests.get(url = f'{URL}/pokemons', params= {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Бульбазавр'


@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'), ('trainer_id', TRAINER_ID), ('id', '259058')])
def test_parametize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params= {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value