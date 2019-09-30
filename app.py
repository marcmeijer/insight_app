from flask import Flask,render_template,request
from get_letters import get_letters
from a_model import ModelIt
import pandas as pd
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
   # pull 'drug_check' from input field and store it
   rx = request.args.get('drug_check')

   # read in our csv file
   dbname = './static/data/cvs_oncology_formulary.csv'
   drug_db = pd.read_csv(dbname)

   # let's only select Oncology drugs with the specified drug check
   #drug_db = drug_db[drug_db['specialty'] == 'oncology']
   drug_db = drug_db[drug_db['drug'] == rx]

   # we really only need the likelihood and drug check for this one
   drug_db = drug_db[['drug','likelihood_short','brand_name']]

   # just select oncology  from the drug data base for the drug that the user inputs
   drugs = []
   for i in range(0, drug_db.shape[0]):
      drugs.append(dict(index=drug_db.iloc[i]['drug'], attendant=drug_db.iloc[i]['likelihood_short'],
                        drug_check=drug_db.iloc[i]['brand_name']))
   the_result = ModelIt(rx, drugs)
   return render_template("model_output.html", births=drugs, the_result=the_result)

if __name__ == '__main__':
    app.run()
