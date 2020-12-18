# install miniconda on the container
FROM continuumio/miniconda3

# copy the code to the container
COPY . /app

# change working directory
WORKDIR /app 

# create a conda environment
RUN conda env create --file environment.yml 

# add conda path
ENV PATH /opt/conda/envs/Python4DS/bin:$PATH

# define a default onda environment
ENV CONDA_DEFAUT_ENV Python4DS 

# expose a port to communicate with the host
EXPOSE 8080  

CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8080"]
