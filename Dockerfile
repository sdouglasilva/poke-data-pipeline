# Etapa 1: Imagem base
FROM python:3.10-slim

# Etapa 2: Definir o diretório de trabalho dentro do container
WORKDIR /app

# Etapa 3: Copiar o arquivo de dependências (requirements.txt) para o container
COPY requirements.txt .

# Etapa 4: Instalar as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app

# Etapa 5: Copiar o restante dos arquivos do projeto para o container
COPY . .

# Etapa 6: Definir o comando que será executado quando o container iniciar
CMD ["python", "src/main.py"]
