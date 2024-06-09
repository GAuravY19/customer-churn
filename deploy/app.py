from flask import Flask, redirect, render_template, url_for, flash
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
        flash(f'Values were successfully Entered.', 'success')
        print('form accepted')
        return redirect(url_for('results'))

    else:
        for fieldname, errormsg in form.errors.items():
            for err in errormsg:
                print(f"The error in {fieldname} is {err}")


    return render_template('info.html', form = form)

@app.route('/results')
def results():
    return "hello wolrd"


if __name__ == "__main__":
    app.run(debug=True)
