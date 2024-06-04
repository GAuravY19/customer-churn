import pandas as pd
import numpy as np
import sys

from src.utils.exceptions import CustomException
from src.utils.logging import logging

from tqdm.auto import tqdm
from math import ceil



class DataClean:
    logging.info("Inside data cleaning class.")

    def __init__(self, df):
        logging.info("Data cleaning Class Initialized.")
        self.data = df

    def step_01_dropping_cols(self):
        """
            This method removes the columns that have no significance.
        """
        logging.info("Inside the step 01 of data cleaning.")
        try:
            logging.info("Dropping columns started.")

            cols_to_remove = ['past_consultations', 'num_of_steps']
            self.data_1 = self.data.drop(cols_to_remove, axis='columns')

            logging.info("Dropping columns ended.")

        except Exception as e:
            logging.info("Dropping columns failed.")
            raise CustomException(e, sys)


    def step_02_Age_column(self):
        """
            This method fills nan values and removes the outliers in Age column.
        """
        logging.info("Inside the step 02 of data cleaning.")
        try:
            logging.info("cleaning Age column started.")

            mean_age = self.data_1['age'].mean()
            self.data_1['age'].fillna(round(mean_age, 2), inplace=True)

            logging.info("cleaning Age column Completed.")

        except Exception as e:
            logging.info("cleaning Age column Completed.")
            raise CustomException(e, sys)


    def step_03_bmi_column(self):
        """
            This method fills nan values and removes the outliers in BMI column.
        """
        logging.info("Inside step 03 of data cleaning.")

        try:
            logging.info("Cleaning bmi column started.")

            mean_bmi = self.data_1['bmi'].mean()
            self.data_1['bmi'].fillna(round(mean_bmi, 2), inplace=True)

            threshold_max = 45
            threshold_min = 18.5

            self.data_2 = self.data_1[self.data_1['bmi'] < threshold_max]
            self.data_3 = self.data_2[self.data_2['bmi'] > threshold_min]

            logging.info("Cleaning bmi column completed.")

        except Exception as e:
            logging.info("Cleaning bmi column failed.")
            raise CustomException(e, sys)


    def step_04_children_column(self):
        """
            This method fills nan values and removes the outliers in children column.
        """
        logging.info("Inside step 04 of data cleaning.")

        try:
            logging.info('cleaning children column started.')

            mode_children = self.data_3['children'].mode()
            self.data_3['children'].fillna(ceil(mode_children), inplace = True)

            logging.info('cleaning children column completed.')

        except Exception as e:
            logging.info('cleaning children column failed.')
            raise CustomException(e, sys)


    def step_05_claim_amount_column(self):
        """
            This method fills nan values and removes the outliers in claim amount column.
        """
        logging.info("Inside step 05 of data cleaning.")

        try:
            logging.info('cleaning clain amount column started.')

            mean_claim_amt = self.data_3['Claim_Amount'].mean()
            self.data_3['Claim_Amount'].fillna(round(mean_claim_amt, 2), inplace = True)

            threshold_max = 4500
            threshold_min = 61000

            self.data_4 = self.data_3[self.data_3['Claim_Amount'] < threshold_max]
            self.data_5 = self.data_4[self.data_4['Claim_Amount'] > threshold_min]

            logging.info('cleaning clain amount column completed.')

        except Exception as e:
            logging.info('cleaning clain amount column failed.')
            raise CustomException(e, sys)


    def step_06_hospital_expenditure(self):
        """
            This method fills nan values and removes the outliers in hospital Expenditure column.
        """
        logging.info("Inside step 06 of data cleaning.")
        try:
            logging.info("cleaning hospital expenditure column started.")

            mean_hos_expend = self.data_5['Hospital_expenditure'].mean()
            self.data_5['Hospital_expenditure'].fillna(round(mean_hos_expend, 2), inplace=True)

            threshold_max = 60000000
            self.data_6 = self.data_5[self.data_5['Hospital_expenditure'] < threshold_max]

            logging.info("cleaning hospital expenditure column completed.")

        except Exception as e:
            logging.info("cleaning hospital expenditure failed.")
            raise CustomException(e, sys)


    def step_07_annaul_sal(self):
        """
            This method fills nan values and removes the outliers in annual salary column.
        """
        logging.info("Inside step 07 of data cleaning.")
        try:
            logging.info("Cleaning Annaul salary column started.")

            mean_sal = self.data_6['Anual_Salary'].mean()
            self.data_6['Anual_Salary'].fillna(round(mean_sal,2), inplace=True)

            threshold_max = 750000000
            self.data_7 = self.data_6[self.data_6['Anual_Salary'] < threshold_max]

            logging.info("Cleaning Annaul salary column completed.")

        except Exception as e:
            logging.info("Cleaning Annaul salary column failed.")
            raise CustomException(e, sys)









