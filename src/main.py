import logging
import pandas as pd
from src.data_extraction import extract_all_pokemon_data
from src.data_analysis import data_analytics
from src.data_reporting import generate_chart_pokemon_type_distribution, save_reports
from utils.logger_config import setup_logging


def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Iniciando extração de dados dos Pokémons...")
    data = extract_all_pokemon_data(limit=100)

    if data.empty:
        logger.warning("Nenhum dado foi extraído. Encerrando execução.")
        return

    df = pd.DataFrame(data)
    logger.info(f"{len(df)} Pokémons carregados no DataFrame.")
    
    resultados = data_analytics(df)
    save_reports(resultados)
    generate_chart_pokemon_type_distribution(resultados["contagem_por_tipo"])



main()
