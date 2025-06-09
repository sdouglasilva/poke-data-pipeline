import os
import logging
import matplotlib.pyplot as plt
import seaborn as sns

def save_reports(resultados, output_dir="data/reports"):
    """Salva dados já tratados em arquivos .csv"""
    try:
        os.makedirs(output_dir, exist_ok=True)
        logging.info(f"Pasta '{output_dir}' verificada/criada com sucesso.")
        contagem_path = os.path.join(output_dir, "contagem_pokemon_tipo.csv")
        medias_path = os.path.join(output_dir, "medias_pokemon_tipo.csv")
        categorizados_path = os.path.join(output_dir, "dados_pokemon_categorizados.csv")
        resultados["contagem_por_tipo"].to_csv(contagem_path, index=False)
        logging.info(f"Relatório salvo: {contagem_path}")
        resultados["medias_por_tipo"].to_csv(medias_path, index=False)
        logging.info(f"Relatório salvo: {medias_path}")
        resultados["dados_com_categoria"].to_csv(categorizados_path, index=False)
        logging.info(f"Relatório salvo: {categorizados_path}")

    except Exception as e:
        logging.error(f"Erro ao salvar relatórios: {e}", exc_info=True)

def generate_chart_pokemon_type_distribution(df_type_count):
    """Gera e salva o gráfico da distribuição de Pokémon por tipo."""
    try:
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

        logging.info(f"Gráfico salvo com sucesso: {output_path}")
    except Exception as e:
        logging.error(f"Erro ao gerar gráfico de distribuição de tipos: {e}", exc_info=True)
