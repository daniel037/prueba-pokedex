import requests

url_api= 'https://pokeapi.co/api/v2/pokemon/'

def main():
    data = get_pokemon_data(url_api)
    contador = 0
    for pokemon in data:
        if pokemon.find('at') != -1 and pokemon.count('a') == 2:
            contador = contador + 1
    print('existen ' + str(contador) + ' pokemon que cumplen las condiciones')


def get_pokemon_data(url_pokemon=''):
    new_url = url_pokemon + '?limit=898'
    respuesta = requests.get(new_url)
    lista_poke = []
    data = respuesta.json()
    for poke in data['results']:
        lista_poke.append(poke['name'])
    return lista_poke


if __name__ == '__main__':
    main()