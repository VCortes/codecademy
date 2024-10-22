# Usar uma imagem base do Python
FROM python:3.12.4-slim

# Definir o diretório de trabalho
WORKDIR /

# Copiar o arquivo de requisitos e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Instalar o debugpy
RUN pip install debugpy

# Expor as portas necessárias
EXPOSE 5000 5678

# Copiar o código da aplicação
COPY . .


# Comando para rodar a aplicação com debugpy e desativar módulos congelados
CMD ["python", "-m", "debugpy", "--wait-for-client", "--listen", "0.0.0.0:5678", "app.py"]
