import pandas as pn
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Read csv file
df_alim = pn.read_csv("../data/export_alimconfiance.csv", sep=";")
#print(data.columns)

# Drop NA Values
df_alim2 = df_alim.dropna()
# print(df_alim2.columns)

# Slice Dataset into Y to predict variable and X variables
df_alim2['texte'] = df_alim2['APP_Libelle_etablissement'] + " " + df_alim2['filtre']  + " " + df_alim2['ods_type_activite']
#print(df_alim2['texte'].shape)

y = df_alim2['Synthese_eval_sanit']
#print(y)

X = df_alim2["texte"]
#print(X.shape)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
#print(X_train.shape)

# Vectorize X
vectorizer = CountVectorizer()
X_train_text = vectorizer.fit_transform(X_train)
X_test_text = vectorizer.transform(X_test)

# Model training and prediction
clf = LogisticRegression(max_iter=10000)

clf.fit(X_train_text, y_train)

y_pred = clf.predict(X_test_text)

print(classification_report(y_test, y_pred))

print(clf.predict(vectorizer.transform(["toto"])))




import code
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/prediction/{restaurant_name}")
def read_item(restaurant_name: str):
    prediction = code.clf.predict(code.vectorizer.transform([restaurant_name]))
    return {"restaurant_name": restaurant_name,"prediction": str(prediction)}
