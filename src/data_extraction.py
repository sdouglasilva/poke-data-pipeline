from src.api_client import get_pokemon_list, get_pokemon_details
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

def extract_pokemon_stats(stats: list) -> dict:
    """
    Extrai as estatísticas base de HP, Ataque e Defesa de um Pokémon.
    Args:
        stats (list): Lista de estatísticas do Pokémon.
    Returns:
        dict: Dicionário com HP, Ataque e Defesa.
    """
    result = {"HP": None, "Ataque": None, "Defesa": None}
    for stat in stats:
        stat_name = stat["stat"]["name"]
        base_value = stat["base_stat"]
        if stat_name == "hp":
            result["HP"] = base_value
        elif stat_name == "attack":
            result["Ataque"] = base_value
        elif stat_name == "defense":
            result["Defesa"] = base_value
    return result

def process_pokemon_details(pokemon_details: dict) -> dict:
    """
    Processa os detalhes completos de um Pokémon para um formato padronizado.
    Args:
        pokemon_details (dict): Dicionário com os dados detalhados do Pokémon.
    Returns:
        dict: Pokémon formatado com atributos principais.
    """
    if not pokemon_details:
        logger.warning('Detalhes do Pokémon não encontrados.')
        return None

    stats = extract_pokemon_stats(pokemon_details.get("stats", []))
    
    processed = {
        "ID": pokemon_details["id"],
        "Nome": pokemon_details["name"].title(),
        "Experiência Base": pokemon_details["base_experience"],
        "Tipos": [t["type"]["name"].title() for t in pokemon_details["types"]],
        "HP": stats["HP"],
        "Ataque": stats["Ataque"],
        "Defesa": stats["Defesa"]
    }
    return processed