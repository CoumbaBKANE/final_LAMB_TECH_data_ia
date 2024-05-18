from fastapi import FastAPI, UploadFile, File
import numpy as np
import pandas as pd
from joblib import load 
from upload import upload 
from sklearn.cluster import KMeans

def features(df):

  df['TransactionFrequency'] = df.groupby(['Origine','Destination'])['Timestamp'].transform('count')
  # Transaction Duration (for P2P transactions)
  df['TransactionDuration'] = (df['Timestamp'] - df['Timestamp'].shift(1)).dt.total_seconds() 
  # Fill the first NaN value with a reasonable default:
  df['TransactionDuration'].fillna(300, inplace=True)
  df['AmountDifference'] = df['Montant'] - df['Montant'].shift(1)
  df['AmountDifference'].fillna(0, inplace=True) # Fill the first NaN value with 0
  return df[['Montant' ,'TransactionFrequency', 'TransactionDuration']]

app = FastAPI()

#@app.get("/")


def myLoad():
  model_path = "kmeans.hdf5"
  model = load(model_path, compile=False)
  return model


 
 # return df

@app.post("/predict")

def predict(file: UploadFile = File(...)) -> dict:  
  model = myLoad()
  myCSV = upload()
  y_pred = model.predict(features(myCSV))
  index= np.where(y_pred == 1)
  df = myCSV.loc[index[0]].groupby(['Origine','Destination'])
  print(y_pred)
  prediction = model.predict(myCSV)
  return {"prediction": "prediction.tolist()"}  # Convertir le résultat en liste pour la sérialisation JSON
  df = pd.read_csv(file.file)
  print(df.head(4))
  df =df.to_dict()

  return {'coumba':'kane'}
    