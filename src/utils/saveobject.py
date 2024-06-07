import pickle
import os

def saveObject(object, name:str):
    with open(f'D:/customer-churn/customer-churn/artifacts/scalers&encoders/{name}', 'wb') as f:
        pickle.dump(object, f)
