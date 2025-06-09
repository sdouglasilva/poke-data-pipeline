import logging
import pandas as pd
from src.data_extraction import extract_all_pokemon_data
from src.data_analysis import data_analytics
from src.data_reporting import generate_chart_pokemon_type_distribution, save_reports
from utils.logger_config import setup_logging


def main():
    """
    Função  que orquestra todo o pipeline de extração,
    transformação, análise e exportação de dados de Pokémons.
    """
    # Tarefa 4: Pipeline Automatizado - Logs e Erros
    # Inicializa a configuração de logging para todo o pipeline.
    # Garante que os logs sejam formatados e direcionados para o arquivo 'pipeline.log'
    # e para o console, conforme definido em 'utils/logger_config.py'.
    setup_logging()

    #Configura logger pelo root, definido na setup_logging
    logger = logging.getLogger(__name__)
    logger.info("Iniciando extração de dados dos Pokémons...")

    #Tarefa 1: Extração de Dados:
    # Consumo de Dados: Acessa a PokeAPI para obter uma lista de 100 Pokémon e seus detalhes.
    # Estruturação com pandas: A função 'extract_all_pokemon_data' é responsável
    # por retornar os dados já estruturados em um formato adequado para criar o DataFrame.
    data = extract_all_pokemon_data(limit=100)

    # Tarefa 4: Pipeline Automatizado - Tratamento de Erros
    # Verifica se a extração de dados resultou em um DataFrame vazio.
    # Isso pode indicar falhas na API ou ausência de dados.
    if data.empty:
        logger.warning("Nenhum dado foi extraído. Encerrando execução.")
        return
    # Instanciando o Dataframe
    df = pd.DataFrame(data)


    # Tarefa 2: Transformação de Dados e Análise Estatística
    # A função 'data_analytics' (em src/data_analysis.py) é responsável por:
    # - Categorização: Adicionar a coluna 'Categoria' ('Fraco', 'Médio', 'Forte').
    # - Transformações de Tipos: Calcular a contagem de Pokémon por tipo.
    # - Análise Estatística: Calcular médias de ataque, defesa e HP por tipo.
    # - Identificar os 5 Pokémon com maior experiência base.

    #Informa a quantidade de pokemons carregados no df
    logger.info(f"{len(df)} Pokémons carregados no DataFrame.")
    
    resultados = data_analytics(df)#retorna um dicionário
    # Tarefa 3: Geração do Relatório Consolidado (Tabelas CSV) e Exportação.
    # A função 'save_reports' é responsável por tomar os dados processados (resultados)
    # e exportá-los para arquivos CSV, conforme os requisitos do relatório.
    save_reports(resultados)
    #gera os gráficos requisitados
    generate_chart_pokemon_type_distribution(resultados["contagem_por_tipo"])



main()
