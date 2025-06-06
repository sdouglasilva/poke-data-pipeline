import requests
import logging
from utils.constants import BASE_URL

logger = logging.getLogger(__name__)

def get_pokemon_list(limit=100, offset=0)->list: 
    """Função para buscar a lista de pokemons, com limite definido"""
    url = f"{BASE_URL}/pokemon?limit={limit}&offset={offset}"
    logger.info(f'Requisitando lista de Pokemon: {url}')
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("results",[])
    except requests.RequestException as e:
      logger.error(f"Erro na requisição da lista: {e}")
      return []
    
pokemons = get_pokemon_list(limit=10, offset=0)
if pokemons:
    for poke in pokemons:
        print(f"Nome: {poke['name']} - URL: {poke['url']}")
else:
    print("Nenhum Pokémon foi retornado.")


    
def get_pokemon_details(url):
      """Função que faz a requisição para retornar detalhes do Pokemon"""
      logger.debug(f'Requisitando detalhes do Pokemon:{url}')
      try:
          response = requests.get(url)
          response.raise_for_status()
          return response.json()
      except requests.RequestException as e:
          logger.error(f"Erro na requisição das informações sobre o pokemon:{e}")
          raise
      




