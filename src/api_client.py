import requests
import logging
from utils.constants import BASE_URL

logger = logging.getLogger(__name__)


def get_pokemon_list(limit=100, offset=0) -> list:
    """
    Busca uma lista de Pokemons da API
    Args:
        limit (int): Número máximo de Pokémons que a requisiçao retorna.
        offset (int): Início da lista.
    Returns:
        list: Lista de dicionários contendo nome e url de cada Pokemon.
    """
    url = f"{BASE_URL}/pokemon?limit={limit}&offset={offset}"
    logger.info(f"Requisitando lista de Pokemons: {url}")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("results", [])
    except requests.HTTPError as http_err:
        logger.error(f"Erro HTTP: {http_err.response.status_code} - {http_err}")
    except requests.ConnectionError:
        logger.error("Erro de conexão com a API.")
    except requests.Timeout:
        logger.error("Tempo de resposta da API esgotado.")
    except requests.RequestException as e:
        logger.error(f"Erro inesperado na requisição da lista: {e}")
    return []

def get_pokemon_details(url: str) -> dict | None:
    """
    Busca os detalhes de um Pokemon a partir da URL obtida.
    Args:
        url (str): URL específica do pokemon.
    Returns:
        dict ou none: Dicionário com dados de um Pokemon específico
    """
    logger.debug(f"Requisitando detalhes do Pokemon: {url}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    
    except requests.HTTPError as http_err:
        logger.error(f"Erro HTTP ao buscar detalhes: {http_err.response.status_code} - {http_err}")
    except requests.ConnectionError:
        logger.error("Erro de conexão ao buscar detalhes do Pokémon.")
    except requests.Timeout:
        logger.error("Tempo esgotado ao buscar detalhes do Pokémon.")
    except requests.RequestException as e:
        logger.error(f"Erro inesperado ao requisitar detalhes do Pokémon: {e}")
    
    return None



