import numpy as np
import os
import sys

from src.utils.exceptions import CustomException
# from src.utils.logging import logging

from pathlib import Path

from .openpklfiles import load_pkl_file

class MakePrediction:
    """
        This class contains all the methods required for making predictions.
    """

    def __init__(self):
        # logging.info("Making prediction class initialized.")
        self.scalers_encoders_file_path = Path(r'D:\customer-churn\customer-churn\artifacts\scalers&encoders')
        self.model_file_path = Path(r'D:\customer-churn\customer-churn\artifacts\model')

        self.x = np.zeros(12)

        self.age_scaler_path = os.path.join(self.scalers_encoders_file_path, 'age_scaler.pkl')
        self.annual_salary_path = os.path.join(self.scalers_encoders_file_path, 'anl_sal_scaler.pkl')
        self.bmi_scaler_path = os.path.join(self.scalers_encoders_file_path, 'bmi_scaler.pkl')
        self.children_scaler_path = os.path.join(self.scalers_encoders_file_path, 'children_scaler.pkl')
        self.claim_amt_scaler_path = os.path.join(self.scalers_encoders_file_path, 'claim_amt_encoder.pkl')
        self.hospital_exp_scaler_path = os.path.join(self.scalers_encoders_file_path, 'hos_exp_encoder.pkl')
        self.number_hos_scaler_path = os.path.join(self.scalers_encoders_file_path, 'num_hos_scaler.pkl')
        self.region_scaler_path = os.path.join(self.scalers_encoders_file_path, 'region_encoder.pkl')
        self.gender_encoder_path = os.path.join(self.scalers_encoders_file_path, 'sex_encoder.pkl')
        self.smoker_encoder_path = os.path.join(self.scalers_encoders_file_path, 'smoker_encoder.pkl')
        self.model_path = os.path.join(self.model_file_path, 'model.pkl')

    def LoadScalerandEncoder(self):
        """
            This method loads the scaler and encoder for scaling and encoding the data values.
        """
        # logging.info("Inside LoadScalerandEncoder method.")
        try:
            # logging.info("Loading of scaler and encoder started.")

            self.AGE = load_pkl_file(self.age_scaler_path)
            self.ANNUAL_SALARY = load_pkl_file(self.annual_salary_path)
            self.BMI = load_pkl_file(self.bmi_scaler_path)
            self.CHILDREN = load_pkl_file(self.children_scaler_path)
            self.CLAIM_AMT = load_pkl_file(self.claim_amt_scaler_path)
            self.HOSPITAL_EXP = load_pkl_file(self.hospital_exp_scaler_path)
            self.NUMBER_HOS = load_pkl_file(self.number_hos_scaler_path)
            self.REGION = load_pkl_file(self.region_scaler_path)
            self.GENDER = load_pkl_file(self.gender_encoder_path)
            self.SMOKER = load_pkl_file(self.smoker_encoder_path)

            # logging.info("Loading of scaler and encoder completed.")

        except Exception as e:
            # logging.info("Loading of scaler and encoder failed.")
            raise CustomException(e, sys)

    def LoadModel(self):
        """
            This method loads the model.
        """
        # logging.info("Inside LoadModel method.")
        try:
            # logging.info("Loading of scaler and encoder started.")
            self.MODEL = load_pkl_file(self.model_path)
            # logging.info("Loading of scaler and encoder completed.")

        except Exception as e:
            # logging.info("Loading of scaler and encoder failed.")
            raise CustomException(e, sys)


    def PredictValue(self, age:int,
                    anl_sal:int, bmi:float, child:int,
                    claim_amt:int, hos_exp:int, num_hos:int, region:str, gender:str, smoker:str) -> float:
        """
        Makes the actual predictions based on the provided respondent data.

        Args:
            age (int): The age of the respondent.
            anl_sal (int): Annual salary of the respondent.
            bmi (float): Body Mass Index of the respondent.
            child (int): Number of children the respondent has.
            claim_amt (int): Amount claimed by the respondent.
            hos_exp (int): Hospital expenses incurred by the respondent.
            num_hos (int): Number of hospital visits by the respondent.
            region (str): Region where the respondent resides.
            gender (str): Gender of the respondent.
            smoker (str): Indicates if the respondent is a smoker ('yes' or 'no').

        Returns:
            float: The predicted value based on the input parameters.
        """
        # logging.info("Inside PredictValue method.")
        try:
            # logging.info("Making prediction started.")
            final_age = self.AGE.transform([[age]])
            final_anl_sal = self.ANNUAL_SALARY.transform([[anl_sal]])
            final_bmi = self.BMI.transform([[bmi]])
            final_child = self.CHILDREN.transform([[child]])
            final_claim_amt = self.CLAIM_AMT.transform([[claim_amt]])
            final_hos_exp = self.HOSPITAL_EXP.transform([[hos_exp]])
            final_num_hos = self.NUMBER_HOS.transform([[num_hos]])
            # final_region = self.REGION.transform(region)
            final_gender = self.GENDER.transform([[gender]])
            final_smoker = self.SMOKER.transform([[smoker]])

            self.x[0] = final_age
            self.x[1] = final_gender
            self.x[2] = final_bmi
            self.x[3] = final_child
            self.x[4] = final_smoker
            self.x[5] = final_claim_amt
            self.x[6] = final_hos_exp
            self.x[7] = final_num_hos
            self.x[8] = final_anl_sal

            final_region = ['northwest','southeast','southwest']
            if region in final_region:
                reg_ind = final_region.index(region[0])
                self.x[reg_ind + 9] = 1

            prediction = self.MODEL.predict([self.x])
            # logging.info("Making prediction complete.")

            return prediction

        except Exception as e:
            # logging.info("Making prediction failed.")
            raise CustomException(e, sys)
