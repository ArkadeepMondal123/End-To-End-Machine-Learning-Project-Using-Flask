from flask import Flask, render_template,request
import pandas as pd
import pickle
import sklearn
import numpy as np
import warnings
from datetime import datetime
warnings.filterwarnings('ignore')

app = Flask(__name__, template_folder='template')
model=pickle.load(open('log_model.pkl','rb'))

@app.route('/',methods=['GET'])  
def home_fun():
    return render_template('home.html') 

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender=request.form['Gender']
        if (Gender=='Male'):
            Gender=0
        else:
            Gender=1
        Married=request.form['Married']
        if (Married=='Yes'):
            Married=1
        else:
            Married=0
        Dependents=float(request.form['Dependents'])
        Education=request.form['Education']
        if (Education=='Graduate'):
            Education=1
        else:
            Education=0
        Self_Employed=request.form['Self_Employed']
        if (Self_Employed=='Yes'):
            Self_Employed=1
        else:
            Self_Employed=0
        ApplicantIncome=float(request.form['ApplicantIncome'])
        CoapplicantIncome=float(request.form['CoapplicantIncome'])
        LoanAmount=float(request.form['LoanAmount'])
        Loan_Amount_Term=float(request.form['Loan_Amount_Term'])
        Credit_History=int(request.form['Credit_History'])
        Property_Area=request.form['Property_Area']
        if (Property_Area=='Rural'):
            Property_Area=0
        elif(Property_Area=='Urban'):
            Property_Area=1
        else:
            Property_Area=2
        data={'Gender':Gender,
              'Married':Married,
              'Dependents':Dependents,
              'Education':Education,
              'Self_Employed':Self_Employed,
              'ApplicantIncome':ApplicantIncome,
              'CoapplicantIncome':CoapplicantIncome,
              'LoanAmount':LoanAmount,
              'Loan_Amount_Term':Loan_Amount_Term,
              'Credit_History':Credit_History,
              'Property_Area':Property_Area,
              }
        df=pd.DataFrame([data])   
        prediction=model.predict(df)
        output=prediction[0]
        print(output)
        if output == 0:
            return render_template('home.html', Prediction_text='Sorry!!!Your Loan has not been approved.')
        else:
            return render_template('home.html', Prediction_text='Yes!!!Your Loan has been approved')
    else:
        render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)