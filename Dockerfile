FROM continuumio/miniconda3
# installer miniconda sur le container

COPY . /app
# copier notre code sur le container

WORKDIR /app 
# change le pathe de travail, comme un cd

RUN conda env create --file environment.yml 
# créer un environnement conda

ENV PATH /opt/conda/envs/Python4DS/bin:$PATH
# ajoute dans le path mon conda depuis là où elle est

ENV CONDA_DEFAUT_ENV Python4DS 
# définit une variable d'env par défaut (base d'habitude)

EXPOSE 8080  
# il faut exposer un port pour communiquer avec le host

# CMD ["python, "code/code.py"]

CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8080"]
