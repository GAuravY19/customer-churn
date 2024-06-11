from .utils.predict import MakePrediction
from flask import Flask, redirect, render_template, url_for, request
from .forms import CollectData


app = Flask(__name__)

app.config['SECRET_KEY'] = 'fd6a4f49c47514f6e4fc44b45c60c68f5fcd3be4d7fea6b58814aa5c059f00f2ccb0558de80411f4ccb4ac6d2f0359360711be818fd07fa964c3c796f1c89b5f'

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/information", methods=['POST', 'GET'])
def information():
    form = CollectData()

    if form.validate_on_submit():
        age = form.Age.data
        gender = form.Gender.data
        bmi = form.BMI.data
        children = form.children.data
        smoke = form.Smoke.data
        claim = form.claim.data
        hos = form.Hospital.data
        num_hos = form.hopitalization.data
        sal = form.Salary.data
        region = form.region.data

        predict = MakePrediction()
        predict.LoadModel()
        predict.LoadScalerandEncoder()
        value = predict.PredictValue(age=age, anl_sal=sal, bmi=bmi, child=children,
                             claim_amt=claim, hos_exp=hos, num_hos=num_hos,
                             gender=gender, smoker=smoke, region=region)

        value = round(float(value),2)

        print("Yeh mera noob values hai",value)
        print("Yeh uska noob type hai", type(value))

        return redirect(url_for('results', predicted_value = value))

    else:
        for fieldname, errormsg in form.errors.items():
            for err in errormsg:
                print(f"The error in {fieldname} is {err}")

    return render_template('info.html', form = form)


@app.route('/results')
def results():
    predicted_value = request.args.get('predicted_value')
    print("Yeh mera values hai",predicted_value)
    print("Yeh uska type hai", type(predicted_value))
    return render_template('result.html', predicted_value=predicted_value)


if __name__ == "__main__":
    app.run(debug=True)
