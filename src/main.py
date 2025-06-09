import logging
import pandas as pd
from src.data_extraction import extract_all_pokemon_data
from src.data_transformation import add_category, avg_by_type, count_pokemons_by_type

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Iniciando extração de dados dos Pokémons...")
    data = extract_all_pokemon_data(limit=100)

    if data.empty:
        logger.warning("Nenhum dado foi extraído. Encerrando execução.")
        return

    df = pd.DataFrame(data)
    logger.info(f"{len(df)} Pokémons carregados no DataFrame.")
    df = add_category(df)
    types = count_pokemons_by_type(df)
    avg = avg_by_type(df)
    print("\n--- Pokémons com Categoria ---")
    print(df[["Nome", "Experiência Base", "Categoria"]].head())

    print("\n--- Quantidade por Tipo ---")
    print(types)

    print("\n--- Médias por Tipo ---")
    print(avg)


main()
