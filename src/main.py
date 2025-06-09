import logging
import pandas as pd
from src.data_extraction import extract_all_pokemon_data
from src.data_analysis import data_analytics

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
    data_analytics(df)



main()
