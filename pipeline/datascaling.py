import pandas as pd
import numpy as np

from src.pipeline_funct.datascaling import DataScaling

df = pd.read_csv(r'D:\customer-churn\customer-churn\data\clean\cleandata.csv')

class DataScalePipeline:
    def __init__(self):
        self.Scale = DataScaling(df=df)

    def RunPipeline(self):
        self.Scale.step_01_age_column()
        self.Scale.step_02_sex_column()
        self.Scale.step_03_bmi_column()
        self.Scale.step_04_child_column()
        self.Scale.step_05_smoker_column()
        self.Scale.step_06_claim_amt()
        self.Scale.step_07_Hospital_expenditure_column()
        self.Scale.step_08_NUmber_of_past_hospitalizations_column()
        self.Scale.step_09_anual_salary_columns()
        self.scaledata = self.Scale.step_10_region_column()

    def savedata(self):
        self.scaledata.to_csv('D:/customer-churn/customer-churn/data/scaleddata/scaleddata.csv', index=False)

