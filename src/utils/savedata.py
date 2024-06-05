import pandas as pd
import numpy as np

import os

file_path = 'D:\customer-churn\customer-churn\data\clean'

def save_data(df:pd.DataFrame, name:str,filepath = file_path):
    df.to_csv(os.path.join(filepath, name), index=False)
