from flask import Flask,redirect,render_template,url_for,jsonify,request
from utils import DiabetesPrediction
import config
import numpy as np
import pandas as pd
import sklearn


app = Flask(__name__)

@app.route('/')
def hello_flask():
    return  render_template("home.html")

@app.route('/diabetes', methods= ["GET","POST"])
def prediction_result():
    if request.method == "POST":

    
        data = request.form
        print(data)

        Glucose = float(request.form['Glucose'])
        BloodPressure = float(request.form['BloodPressure'])
        SkinThickness = float(request.form['SkinThickness'])
        Insulin = float(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = float(request.form['Age'])


        pred = DiabetesPrediction(data)
        result = pred.prediction_model()

        # return jsonify({"Result": result})
        return render_template("home.html",prediction = result )

    else:
        data = request.form

        Glucose = float(request.form['Glucose'])
        BloodPressure = float(request.form['BloodPressure'])
        SkinThickness = float(request.form['SkinThickness'])
        Insulin = float(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = float(request.form['Age'])


        pred = DiabetesPrediction(data)
        result = pred.prediction_model()
        # return jsonify({"Result": result})
        return render_template("home.html",prediction = result )

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= config.PORT_NUMBER) 

        
