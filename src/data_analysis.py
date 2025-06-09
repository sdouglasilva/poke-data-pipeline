import logging
from src.data_transformation import add_category, count_pokemons_by_type,avg_by_type


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def data_analytics(df):
  "Realiza a análise dos dados dos Pokémons"
  logger.info("Iniciando análise dos dados dos pokémons")


  df = add_category(df)
  types = count_pokemons_by_type(df)
  avg = avg_by_type(df)
  print("\n--- Pokémons Categorizados ---")
  print(df[["Nome", "Experiência Base", "Categoria"]].head())

  print("\n--- 5° Pokémons com maior experiência base ---")
  print(types)

  print("\n--- Médias de pontuação por Tipo ---")
  print(avg)
  logger.info("Análise finalizada com sucesso")
  return {
    "dados_com_categoria":df,
    "contagem_por_tipo": types,
    "medias_por_tipo": avg
  }