## Visão Geral do Projeto

O pipeline é dividido em módulos claros que cobrem as etapas de extração, transformação e relatório de dados.

**Funcionalidades Principais:**

* **Extração de Dados:** Coleta detalhes de 100 Pokémons (ID, Nome, Experiência Base, Tipos, HP, Ataque, Defesa) da PokeAPI.
* **Transformação de Dados:**
    * Categoriza Pokémons em "Fraco", "Médio" e "Forte" com base na Experiência Base.
    * Calcula a distribuição de Pokémons por tipo.
    * Determina a média de HP, Ataque e Defesa por tipo.
    * Identifica os 5 Pokémons com maior experiência base.
* **Relatório e Exportação:** Gera relatórios em formato CSV e gráficos em PNG (distribuição por tipo).
* **Pipeline Automatizado:** Orquestra todas as etapas sequencialmente, com logging detalhado e tratamento de erros.

## Estrutura do Projeto

poke-data-pipeline/

|── data/
│   └── reports/             # Saída: Relatórios CSV e Gráficos PNG
├── logs/
│   └── pipeline.log         # Saída: Logs de execução do pipeline
├── src/                     # Raiz do projeto
│   ├── api_client.py        # Realiza requisições na POKEAPI
│   ├── data_analysis.py     # Módulo para orquestrar transformação e análise
│   ├── data_extraction.py   # Extrair dados da PokeAPI
│   ├── data_reporting.py    # Gerar e salvar relatórios/gráficos
│   └── main.py              # Orquestra toda a pipeline
├── utils/                   
│   ├── constants.py         # Constantes do projeto
│   └── logger_config.py     # Configuração personalizada do logging
├── .gitignore               # Arquivo para o Git ignorar arquivos/pastas
├── Dockerfile               # Configuração para construir a imagem Docker
├── README.md                # Este arquivo de documentação
└── requirements.txt         # Dependências do projeto

```
## Requisitos

* Python 3.+
* Docker (para execução containerizada)

As dependências Python estão listadas em `requirements.txt`.

## Como Configurar e Executar

Siga uma das opções abaixo para executar o pipeline.

### Opção 1: Execução Local

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/sdouglasilva/poke-data-pipeline
    cd poke-data-pipeline
    ```
2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv .venv
    # No Windows:
    .venv\Scripts\activate
    # No macOS/Linux:
    source .venv/bin/activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Execute o pipeline:**
    ```bash
    python -m src.main
    ```
    Os logs serão exibidos no console e gravados em `logs/pipeline.log`. Os relatórios CSV e gráficos PNG serão salvos em `data/reports/`.

### Opção 2: Execução com Docker

1.  **Clone o repositório e navegue até o diretório:**
    ```bash
    git clone https://github.com/sdouglasilva/poke-data-pipeline
    cd poke-data-pipeline
    ```
2.  **Construa a imagem Docker:**
    ```bash
    docker build -t pokemon-pipeline .
    ```
3.  **Execute o container:**
    Para garantir que os relatórios e logs sejam persistidos fora do container, mapeie os volumes:
    ```bash
    docker run -v "$(pwd)/data/reports:/app/data/reports" -v "$(pwd)/logs:/app/logs" poke-data-pipeline
    ```
    * Este comando executará o pipeline dentro do container.
    * Os arquivos de log (`pipeline.log`) e os relatórios/gráficos serão gerados e salvos diretamente nas pastas `logs/` e `data/reports/` no seu sistema local.

## O que foi entregue neste projeto

Aqui está um resumo do que o nosso pipeline de dados faz e como ele foi construído:

* **Entender os Pokémons (Extração e Transformação):**
    * Conseguimos buscar informações detalhadas sobre 100 Pokémons diretamente da PokeAPI (como nome, tipos, HP e ataque).
    * Organizamos esses dados em tabelas fáceis de usar.
    * Classificamos cada Pokémon como "Fraco", "Médio" ou "Forte" com base na sua experiência.
    * Descobrimos a quantidade de Pokémons de cada tipo e calculamos a média de HP, Ataque e Defesa por tipo, além de identificar os 5 Pokémons com mais experiência.

* **Apresentar os Resultados (Relatório e Exportação):**
    * Criamos relatórios claros em formato de tabela (CSV) com as análises feitas.
    * Geramos um gráfico visual (em imagem PNG) que mostra a distribuição dos Pokémons por tipo, facilitando a visualização.

* **Processo Automático (Pipeline):**
    * Todo o processo de buscar, organizar e analisar os dados funciona de forma automática, seguindo uma sequência lógica de etapas.
    * Implementamos um sistema para registrar o que está acontecendo (como um diário de bordo), o que nos ajuda a acompanhar o progresso e a identificar se algo deu errado durante a execução.

* **Ferramentas Utilizadas:**
    * Construímos este projeto usando ferramentas e bibliotecas Python que são padrão na indústria, como `pandas` para lidar com as tabelas de dados, `requests` para conversar com a PokeAPI e `matplotlib`/`seaborn` para criar os gráficos.

* **Fácil de Rodar (Docker):**
    * O projeto foi preparado para ser executado facilmente em qualquer computador usando Docker. Isso significa que ele já vem "empacotado" com tudo o que precisa, sem a necessidade de configurações complicadas.

* **Código Organizado:**
    * O código foi dividido em partes menores e bem organizadas, o que torna fácil de ler, entender e fazer futuras melhorias.
