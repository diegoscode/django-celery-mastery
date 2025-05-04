# Usando a imagem oficial do Python 3.13-slim
FROM python:3.13-slim

# Definir variáveis de ambiente
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Instalar dependências do sistema, se necessário
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de requisitos e instalar as dependências do Python
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar o restante dos arquivos do projeto
COPY . /app/

# Dar permissão de execução ao script
RUN chmod +x /app/entrypoint.sh

# Expor a porta 8000 para o Django
EXPOSE 8000

# Definir o entrypoint
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
