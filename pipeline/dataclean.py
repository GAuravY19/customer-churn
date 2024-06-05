import pandas as pd
import numpy as np

from src.pipeline_funct.dataclean import DataClean
from src.utils.savedata import save_data

df = pd.read_csv(r'D:\customer-churn\customer-churn\data\raw\insurance data.csv')

class DataCleanPipeline:
    def __init__(self):
        self.Clean = DataClean(df=df)

    def RunSteps(self):
        self.Clean.step_01_dropping_cols()
        self.Clean.step_02_Age_column()
        self.Clean.step_03_bmi_column()
        self.Clean.step_04_children_column()
        self.Clean.step_05_claim_amount_column()
        self.Clean.step_06_hospital_expenditure()
        self.clean_data = self.Clean.step_07_annaul_sal()

    def saveData(self):
        save_data(self.clean_data, 'cleandata.csv')


