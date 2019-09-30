from flask import Flask,render_template,request
from get_letters import get_letters
from a_model import ModelIt
import pandas as pd
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    letters = []
    if request.method == "POST":
        # get url that the user has entered
        try:
            drug_check = request.form['drug_check']
            letters = ModelIt(drug_check)
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
    return render_template('index.html', letters=letters, errors=errors)

if __name__ == '__main__':
    app.run()
