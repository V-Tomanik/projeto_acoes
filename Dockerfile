#Define a imagem como sendo python3, simples
FROM python:3-slim

#Define o diretório /code como sendo o diretorio padrão (Cria ele)
WORKDIR /code  
#Copia o arquivo de requirements para o diretorio atual no docker
COPY requirements.txt .
RUN pip3 install -r requirements.txt

CMD /bin/bash
