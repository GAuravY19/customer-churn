import pickle
import os

file_path = 'D:\customer-churn\customer-churn\artifacts\scalers&encoders'

def saveObject(object, name:str, file_path = file_path):
    with open(os.path.join(file_path, name), 'wb') as f:
        pickle.dump(object, f)
