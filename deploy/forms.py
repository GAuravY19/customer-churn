from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, BooleanField, SelectField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired

# <!-- age,sex,bmi,children,smoker,Claim_Amount,Hospital_expenditure,NUmber_of_past_hospitalizations,Anual_Salary,northwest,southeast,southwest,target-->


class CollectData(FlaskForm):
    Age = IntegerField('Age',
                       validators=[DataRequired()])

    Gender = SelectField('Gender',
                         choices=[('option1', 'Male'),
                                  ('option2', 'Female')],
                         validators=[DataRequired()])

    BMI = IntegerField('Body Mass Index (BMI)',
                       validators=[DataRequired()])

    children = IntegerField('No. of Children',
                            validators=[DataRequired()])

    Smoke = SelectField("Do you Smoke",
                        choices=[('option1', 'Yes'),
                                 ('option2', 'No')],
                        validators=[DataRequired()])

    claim = IntegerField("Claim Amount($)",
                         validators=[DataRequired()])

    Hospital = IntegerField("Hospital Expenditure($)",
                            validators=[DataRequired()])

    hopitalization = IntegerField("Number of Past Hospitalization",
                                  validators=[DataRequired()])

    Salary = IntegerField("Annual Salary($)",
                          validators=[DataRequired()])

    region = SelectMultipleField('Select Your region',
                                 choices=[('northwest','NorthWest'),
                                          ('northeast','NorthEast'),
                                          ('southwest','SouthWest'),
                                          ('southeast','SouthEast')],
                                 validators=[DataRequired()])

    submit = SubmitField("Calculate Premium")


