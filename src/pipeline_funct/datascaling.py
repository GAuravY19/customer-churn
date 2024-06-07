import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder

import sys

from src.utils.saveobject import saveObject
from src.utils.exceptions import CustomException
from src.utils.logging import logging

class DataScaling:
    """
        This class contains all the methods that are required for scaling the data values.
    """

    def __init__(self, df:pd.DataFrame):
        """
        Data scaling class initialized.

        Args:
            df (pd.DataFrame): The dataframe that contains the required columns to be scaled.
        """
        self.data = df


    def step_01_age_column(self):
        """
            This method apply Minmaxscaler on Age column.
        """

        logging.info("Inside step 01 of scaling data values.")

        try:
            logging.info("Scaling age column started.")

            age_scaler = MinMaxScaler()

            age_scaler.fit(self.data[['age']])

            self.data[['age']] = age_scaler.transform(self.data[['age']])

            saveObject(age_scaler, 'age_scaler.pkl')

            logging.info("Scaling age column completed.")

        except Exception as e:
            logging.info("Scaling age column failed.")
            raise CustomException(e, sys)


    def step_02_sex_column(self):
        """
            This method apply one hot encoding on sex column.
        """

        logging.info("Inside step 02 of scaling data values.")

        try:
            logging.info('Scaling sex columns started.')

            gender_encoder = OneHotEncoder(drop='first', sparse_output=False)

            gender_encoder.fit(self.data[['sex']])

            self.data[['sex']] = gender_encoder.transform(self.data[['sex']])

            saveObject(gender_encoder, 'sex_encoder.pkl')

            logging.info('Scaling sex columns Completed.')

        except Exception as e:
            logging.info('Scaling sex columns failed.')
            raise CustomException(e, sys)


    def step_03_bmi_column(self):
        """
            THis method apply Minmaxscaler on bmi column.
        """

        logging.info("Inside step 03 of scaling data values.")
        try:
            logging.info("scaling bmi column started.")

            bmi_scaler = MinMaxScaler()

            bmi_scaler.fit(self.data[['bmi']])

            self.data[['bmi']] = bmi_scaler.transform(self.data[['bmi']])

            saveObject(bmi_scaler,'bmi_scaler.pkl')

            logging.info("scaling bmi column Completed.")

        except Exception as e:
            logging.info("scaling bmi column Failed.")
            raise CustomException(e, sys)


    def step_04_child_column(self):
        """
            This method apply Minmaxscaler on children column.
        """

        logging.info("Inside step 04 of scaling data values.")
        try:
            logging.info("scaling children column started.")

            child_scaler = MinMaxScaler()

            child_scaler.fit(self.data[['children']])

            self.data[['children']] = child_scaler.transform(self.data[['children']])

            saveObject(child_scaler,'children_scaler.pkl')

            logging.info("scaling children column completed.")

        except Exception as e:
            logging.info("scaling children column failed.")
            raise CustomException(e, sys)


    def step_05_smoker_column(self):
        """
            This method apply OneHotencoder on Smoker column.
        """

        logging.info("Inside step 05 of scaling data values.")
        try:
            logging.info("Scaling smoker column started.")

            smoke_encoder = OneHotEncoder(drop = 'first', sparse_output=False)

            smoke_encoder.fit(self.data[['smoker']])

            self.data[['smoker']] = smoke_encoder.transform(self.data[['smoker']])

            saveObject(smoke_encoder,'smoker_encoder.pkl')

            logging.info("Scaling smoker column completed.")

        except Exception as e:
            logging.info("Scaling smoker column failed.")
            raise CustomException(e, sys)


    def step_06_claim_amt(self):
        """
            This method apply Minmaxscaler on claim amount column.
        """

        logging.info("Inside step 06 of scaling data values.")
        try:
            logging.info("scaling claim Amount column started.")

            claim_amt_scaler = MinMaxScaler()

            claim_amt_scaler.fit(self.data[['Claim_Amount']])

            self.data[['Claim_Amount']] = claim_amt_scaler.transform(self.data[['Claim_Amount']])

            saveObject(claim_amt_scaler,'claim_amt_encoder.pkl')

            logging.info("scaling claim Amount column Completed.")

        except Exception as e:
            logging.info("scaling claim Amount column Failed.")
            raise CustomException(e, sys)


    def step_07_Hospital_expenditure_column(self):
        """
            This method apply Minmaxscaler on hospital expenditure column.
        """

        logging.info("Inside step 07 of scaling data values.")
        try:
            logging.info("Scaling of Hospital Expenditure column started.")

            hos_exp_scaler = MinMaxScaler()

            hos_exp_scaler.fit(self.data[['Hospital_expenditure']])

            self.data[['Hospital_expenditure']] = hos_exp_scaler.transform(self.data[['Hospital_expenditure']])

            saveObject(hos_exp_scaler,'hos_exp_encoder.pkl')

            logging.info("Scaling of Hospital Expenditure column completed.")

        except Exception as e:
            logging.info("Scaling of Hospital Expenditure column failed.")
            raise CustomException(e, sys)


    def step_08_NUmber_of_past_hospitalizations_column(self):
        """
            This method apply Minmaxscaler on number of past hospitalization column.
        """

        logging.info("Inside step 08 of scaling data values.")
        try:
            logging.info("scaling of past hospitalization started.")

            num_hos_scaler = MinMaxScaler()

            num_hos_scaler.fit(self.data[['NUmber_of_past_hospitalizations']])

            self.data[['NUmber_of_past_hospitalizations']] = num_hos_scaler.transform(self.data[['NUmber_of_past_hospitalizations']])

            saveObject(num_hos_scaler,'num_hos_scaler.pkl')

            logging.info("scaling of past hospitalization completed.")

        except Exception as e:
            logging.info("scaling of past hospitalization failed.")
            raise CustomException(e, sys)


    def step_09_anual_salary_columns(self):
        """
            This method apply Minmaxscaler on annual salary column.
        """

        logging.info("Inside step 09 of scaling data values.")
        try:
            logging.info("Scaling of salary column started.")

            anl_sal_scaler = MinMaxScaler()

            anl_sal_scaler.fit(self.data[['Anual_Salary']])

            self.data[['Anual_Salary']] = anl_sal_scaler.transform(self.data[['Anual_Salary']])

            saveObject(anl_sal_scaler,'anl_sal_scaler.pkl')

            logging.info("Scaling of salary column Completed.")

        except Exception as e:
            logging.info("Scaling of salary column failed.")
            raise CustomException(e, sys)


    def step_10_region_column(self):
        """
            This method apply Onehotencoder on region column.
        """

        logging.info("Inside step 10 of scaling data values.")
        try:
            logging.info("Scaling of region column started.")

            region_encoder = OneHotEncoder(drop='first', sparse_output=False)

            region_encoder.fit(self.data[['region']])
            region_df = region_encoder.transform(self.data[['region']])

            feature_name = region_encoder.get_feature_names_out()
            final_features = [i.split("_")[1] for i in feature_name]
            final_region_df = pd.DataFrame(region_df, columns=final_features)

            self.data_1 = pd.concat([self.data, final_region_df], axis='columns')

            self.data_1.rename(columns={'charges':'target'}, inplace=True)

            self.data_2 = self.data_1.drop(['region'], axis='columns')
            self.data_3 = self.data_2[['age','sex','bmi','children','smoker',
                                       'Claim_Amount','Hospital_expenditure',
                                       'NUmber_of_past_hospitalizations',
                                       'Anual_Salary','northwest','southeast',
                                       'southwest','target']]

            logging.info("Scaling of region column Completed.")

            return self.data_3

        except Exception as e:
            logging.info("Scaling of region column failed.")
            raise CustomException(e, sys)
