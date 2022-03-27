import requests

url_api_raichu = 'https://pokeapi.co/api/v2/pokemon/raichu'
url_api = 'https://pokeapi.co/api/v2/pokemon/?limit=898'
lista_tipos = {}

def main():
    data_raichu = get_pokemon_data_raichu(url_api_raichu)
    data_pokemons = get_pokemon_data(url_api)
    comparacion = get_resultado(data_raichu, data_pokemons)
    print(comparacion)


def get_resultado(data_raichu, data_pokemons):
    contador = 0
    for pokemon in data_pokemons['eggsGroup']:
        for item in pokemon:
            cc = 0
            if item == data_raichu[0] or item == data_raichu[1] :
                cc = cc + 1
            if cc > 0:
                contador = contador + 1    
    return contador

def get_pokemon_data(url):
    lista_items_pokemon = []
    respuesta_lista_pokemon = (requests.get(url)).json()
    for item_pokemon in respuesta_lista_pokemon['results']:
        respuesta_detalle_pokemon = (requests.get(item_pokemon['url'])).json()
        lista_items_pokemon.append(respuesta_detalle_pokemon['species'])
   
    lista_item_egg = []
    for item_egg in lista_items_pokemon:
        respuesta_detalle_egg = (requests.get(item_egg['url'])).json()
        lista_item_egg.append(respuesta_detalle_egg['egg_groups'])
  
    aux = []
    lista_tipos['eggsGroup'] = []
    for egg in lista_item_egg:
        for egg_2 in egg:
            aux.append(egg_2['name'])
        lista_tipos['eggsGroup'].append(aux)
        aux = []
    return lista_tipos

# ----- funcion para raichu----------------------
def get_pokemon_data_raichu(url):
    respuesta = (requests.get(url)).json()
    especie = (requests.get(respuesta['species']['url'])).json()
    raichu_egg = []
    for egg in especie['egg_groups']:
        raichu_egg.append(egg['name'])
    return raichu_egg



if __name__ == '__main__':
    main()