import requests

#url_api = 'https://pokeapi.co/api/v2/pokemon/?limit=151'
url_api = 'https://pokeapi.co/api/v2/pokemon/'
lista_tipos = {}

def main():
    
    data_pokemons = get_pokemon_data(url_api)
    print('aqui----------------')
    print(data_pokemons)



def get_tipo_peso(data):
    #print(data)
    tipo = 'noo'
    for pokemon in data:
        if pokemon['type']['name'] == 'flying':
            tipo = True
            return tipo
        
    return False
        

 
def get_pokemon_data(url):
    lista_items_pokemon = []
    respuesta_lista_pokemon = (requests.get(url)).json()
    for item_pokemon in respuesta_lista_pokemon['results']:
        respuesta_detalle_pokemon = (requests.get(item_pokemon['url'])).json()
        data_peso = get_tipo_peso(respuesta_detalle_pokemon['types'])
        
        if data_peso == True:
            aux = []
            aux.append(respuesta_detalle_pokemon['weight'])
            lista_items_pokemon.append(aux)
    return lista_items_pokemon


if __name__ == '__main__':
    main()