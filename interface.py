from flask import Flask, render_template,request ,jsonify
import numpy as np

from project_app.utils import heart_prediction
import json
app= Flask(__name__)

@app.route('/Hello',methods=['POST'])
def hello():
    return 'Hello'

@app.route('/test',methods=['POST'])
def test():
    data= request.form
    print(data)

    age = data['age']
    sex = data['sex']
    cp = data['cp']
    trestbps = data['trestbps']
    chol = data['chol']
    fbs = data['fbs']
    restecg = data['restecg']
    thalach = data['thalach']
    exang = data['exang']
    oldpeak = data['oldpeak']
    slop = data['slop']
    ca = data['ca']
    thal = data['thal']
     
    pred= heart_prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slop,ca,thal)
    result= pred.heart_result()

    return jsonify ({'result': {result}})

app.run(debug=True)