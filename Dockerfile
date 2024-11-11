# Escolhe uma imagem base Python
FROM python:3.11

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o requirements.txt e instala as dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia o restante dos arquivos do projeto
COPY . .

# Define o comando de entrada padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
