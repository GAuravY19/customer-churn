from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SelectMultipleField, SubmitField, FloatField
from wtforms.validators import DataRequired, InputRequired

# <!-- age,sex,bmi,children,smoker,Claim_Amount,Hospital_expenditure,NUmber_of_past_hospitalizations,Anual_Salary,northwest,southeast,southwest,target-->


class CollectData(FlaskForm):
    Age = IntegerField('Age',
                       validators=[DataRequired()])

    Gender = SelectField('Gender',
                         choices=[('male', 'Male'),
                                  ('female', 'Female')],
                         validators=[DataRequired()])

    BMI = FloatField('Body Mass Index (BMI)',
                       validators=[DataRequired()])

    children = IntegerField('No. of Children',
                            validators=[InputRequired()])

    Smoke = SelectField("Do you Smoke",
                        choices=[('yes', 'Yes'),
                                 ('no', 'No')],
                        validators=[DataRequired()])

    claim = FloatField("Claim Amount($)",
                         validators=[DataRequired()])

    Hospital = FloatField("Hospital Expenditure($)",
                            validators=[DataRequired()])

    hopitalization = IntegerField("Number of Past Hospitalization",
                                  validators=[InputRequired()])

    Salary = FloatField("Annual Salary($)",
                          validators=[DataRequired()])

    region = SelectMultipleField('Select Your region',
                                 choices=[('northwest','NorthWest'),
                                          ('northeast','NorthEast'),
                                          ('southwest','SouthWest'),
                                          ('southeast','SouthEast')],
                                 validators=[DataRequired()])

    submit = SubmitField("Calculate Premium")


