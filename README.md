# Docker - Python4DS M2DM
Alim'Confiance Classifier - Python for Data Science Course

#### -- Project Status: Finished

## Project Intro/Objective
This project exemplifies a data science pipeline

### Methods Used
* Machine Learning

### Technologies
* Scikit-learn
* Numpy
* Docker
* FastAPI

## Getting Started
1. Download the following dataset and put it in a directory called "data" (in your project directory) : https://www.data.gouv.fr/fr/datasets/r/fff0cc27-977b-40d5-9c11-f7e4e79a0b72
2. Create an Anaconda Environment :  
 > conda env create -f environment.yml
3. Activate the environment by running :  
  > conda activate Python4DS (Python4DS is the given environment name in environment.yml)
4. Run the app :  
 > uvicorn src.api:app

## Docker
1. Build Docker image :  
 > docker build --tag  appli:1.0 .
2. Run Docker image :   
 > docker run --name APP_NAME -p 8080:8080 -it IMAGE_ID  
*(run "docker image ls" to get IMAGE_ID)*
3. Run in your browser :  
 > 127.0.0.1:8080 or 127.0.0.1:8080/prediction/RESTAURANT_NAME  
*(example: 127.0.0.1:8080/prediction/KFC)*
