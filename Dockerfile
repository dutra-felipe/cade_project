FROM python:3.11

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput

# Porta que o Render vai usar
ENV PORT=8000

# Comando para iniciar a aplicação
CMD gunicorn app.wsgi:application --bind 0.0.0.0:$PORT