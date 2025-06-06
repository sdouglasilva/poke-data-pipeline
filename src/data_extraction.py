from src.api_client import get_pokemon_list
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def extract_initial_pokemons():
    """
    Extrai a lista inicial de 100 Pokémons da API.
    
    Returns:
        list: Lista de dicionários com os dados dos Pokémons.
    """
    logger.info("Iniciando extração de 100 Pokémons...")
    pokemons = get_pokemon_list(limit=100)
    
    if not pokemons:
        logger.warning("Nenhum Pokémon foi retornado.")
    else:
        logger.info(f"{len(pokemons)} Pokémons foram extraídos com sucesso.")

    return pokemons

pokemons = extract_initial_pokemons()
for pokemon in pokemons[:5]:
  print(f"{pokemon['name']} - {pokemon['url']}")