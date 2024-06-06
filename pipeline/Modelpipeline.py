import pandas as pd
import numpy as np

from src.pipeline_funct.modeltrain import ModelBuilding

df = pd.read_csv(r'D:\customer-churn\customer-churn\data\scaleddata\scaleddata.csv')

class ModelBuildPipeline:
    def __init__(self):
        self.model = ModelBuilding(df=df)

    def RunSteps(self):
        self.model.ModelBuilding()
