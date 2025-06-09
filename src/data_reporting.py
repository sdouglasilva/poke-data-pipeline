import os
import matplotlib.pyplot as plt
import seaborn as sns


def save_reports(resultados, output_dir="data/reports"):
    os.makedirs(output_dir, exist_ok=True)
    resultados["contagem_por_tipo"].to_csv(os.path.join(output_dir, "contagem_pokemon_tipo.csv"), index=False)
    resultados["medias_por_tipo"].to_csv(os.path.join(output_dir, "medias_pokemon_tipo.csv"), index=False)
    resultados["dados_com_categoria"].to_csv(os.path.join(output_dir, "dados_pokemon_categorizados.csv"), index=False)


def generate_chart_pokemon_type_distribution(df_type_count):
    """
    Gera e salva o gráfico da distribuição de Pokémon por tipo.
    """
    POKE_COLOR = "#FFCB05"
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='Tipos', y='Quantidade', data=df_type_count, color=POKE_COLOR)
    ax.set_title("Distribuição dos 5 Principais Tipos de Pokémon")
    ax.set_xlabel("Tipo")
    ax.set_ylabel("Quantidade")
    output_path = os.path.join("data", "reports", "distribuicao_pokemon_tipo.png")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
