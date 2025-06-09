import pandas as pd
import logging
from collections import Counter, defaultdict

logger = logging.getLogger(__name__)

def add_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adiciona uma coluna chamada 'Categoria' com base na experiência base.
    """
    logger.info("Adicionando coluna 'Categoria'...")

    def classify_category(exp):
        if exp < 50:
            return "Fraco"
        elif 50 <= exp <= 100:
            return "Médio"
        else:
            return "Forte"

    df["Categoria"] = df["Experiência Base"].apply(classify_category)
    logger.info("Coluna 'Categoria' adicionada com sucesso.")
    return df


def count_pokemons_by_type(df: pd.DataFrame) -> pd.DataFrame:
    """
    Conta quantos Pokémons existem por tipo e retorna o DataFrame com a contagem.
    """
    logger.info("Contando Pokémons por tipo...")

    all_pokemons_type = []

    for types in df["Tipos"]:
        all_pokemons_type.extend(types)

    counting = Counter(all_pokemons_type)
    df_types = pd.DataFrame.from_dict(counting, orient='index', columns=["Quantidade"])
    df_types = df_types.sort_values("Quantidade", ascending=False).head(5)
    df_types = df_types.reset_index()
    df_types.rename(columns={"index": "Tipos"}, inplace=True)

    logger.info("Contagem por tipo concluída.")
    return df_types


def avg_by_type(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula as médias de HP, Ataque e Defesa agrupadas por tipo.
    """
    logger.info("Calculando médias de HP, Ataque e Defesa por tipo...")

    data_for_type = defaultdict(list)

    for _, line in df.iterrows():
        for type in line["Tipos"]:
            data_for_type[type].append({
                "HP": line["HP"],
                "Ataque": line["Ataque"],
                "Defesa": line["Defesa"]
            })

    results = []

    for tipo, stats in data_for_type.items():
        df_stats = pd.DataFrame(stats)
        results.append({
            "Tipo": tipo,
            "HP Médio": df_stats["HP"].mean(),
            "Ataque Médio": df_stats["Ataque"].mean(),
            "Defesa Média": df_stats["Defesa"].mean()
        })

    df_results = pd.DataFrame(results)
    df_results = df_results.sort_values("Ataque Médio", ascending=False)
    df_results.index = [f"{i+1}." for i in range(len(df_results))]
    df_results.index.name = "Rank"

    logger.info("Médias calculadas com sucesso.")
    return df_results
