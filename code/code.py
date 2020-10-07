import pandas as pn
from sklearn.linear_model import LogisticRegression

data = pn.read_csv("../data/export_alimconfiance.csv", sep=";")
print(data.columns)

data_y = data['Synthese_eval_sanit']
print(data_y)

data_x = 

