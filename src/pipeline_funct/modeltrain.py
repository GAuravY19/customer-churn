import pandas as pd
import numpy as np

import pickle

from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split

class ModelBuilding:
    """
        THis class contains all the methods required for Model building.
    """
    def __init__(self, df:pd.DataFrame):
        """
        Model Building class initialized.

        Args:
            df (pd.DataFrame): Dataframe on which model will be trained.
        """
        self.data = df


    def trainTestSplit(self):
        """
            This method splits the data into train and test sets.
        """
        X = self.data.drop(['target'], axis='columns')
        Y = self.data['target']

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42, shuffle=True)

        return (X_train, X_test, Y_train, Y_test)


    def ModelBuilding(self):
        """
            This method trains the model and saves the model.
        """
        X_train, X_test, Y_train, Y_test = self.trainTestSplit()

        K_neigh = KNeighborsRegressor(n_neighbors=30)
        K_neigh.fit(X_train, Y_train)

        file_path = "D:/customer-churn/customer-churn/artifacts/model/model.pkl"

        with open(file_path, 'wb') as f:
            pickle.dump(K_neigh, f)
