#Importing the libraries
import pickle
from flask import Flask, render_template, request
import numpy as np

#Global variables
app = Flask(__name__)
loadedModel = pickle.load(open('loan model.pkl', 'rb'))

#User defined functions/ API Routes
@app.route('/', methods=['GET'])
def Home():
    return render_template('loan.html')

@app.route('/prediction', methods=['POST'])
def predict():
    gen = request.form['gender']
    marry = request.form['marriage']
    edu = request.form['edu']
    employ = request.form['employ']
    income = request.form['Income']
    coIncome = request.form['CoapplicantIncome']
    loanAmount = request.form['LoanAmount']
    time = request.form['Time']
    creditHistory = request.form['CreditHistory']
    area = request.form['region']
    depender = request.form['depender']

    prediction = loadedModel.predict([[gen, marry, edu, employ, income, coIncome, loanAmount,time, creditHistory, area, depender]])[0]

    prediction = str(round(prediction, 2))

    return render_template('loan.html', output=prediction)

#Main function
if __name__ == '__main__':
    app.run(debug=True) 