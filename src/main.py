import logging
from src.api_client import get_pokemon_list, get_pokemon_details
from src.data_extraction import process_pokemon_details

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def main():
    logger.info("Iniciando extração de dados dos Pokémons...")

    pokemons_list = get_pokemon_list(limit=10, offset=0)

    if not pokemons_list:
        logger.warning("Nenhum Pokémon foi retornado.")
        return

    logger.info(f"{len(pokemons_list)} Pokémons encontrados. Iniciando coleta de detalhes...")

    for poke in pokemons_list:
        nome = poke['name']
        url = poke['url']
        logger.info(f"Processando {nome.title()}...")

        detalhes = get_pokemon_details(url)
        pokemon_formatado = process_pokemon_details(detalhes)

        if pokemon_formatado:
            print(pokemon_formatado)
        else:
            logger.warning(f"Não foi possível processar o Pokémon: {nome}")

if __name__ == "__main__":
    main()
