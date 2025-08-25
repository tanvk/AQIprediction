from flask import Flask, render_template
import pickle
import numpy as np
from sklearn.metrics import mean_squared_error

app = Flask(__name__)

#model1 = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def forecast():
    return render_template("forecast.html")

'''@app.route('/predict',methods=['POST','GET'])
def predict():
    test_input = 1
    model1 = pickle.load(open('model.pkl', 'rb'))
    error = mean_squared_error(test, predictions)
    #print('Test MSE: %.3f' % error)
    return error
'''
@app.route('/indira')
def indira():
    return render_template("indira.html")

@app.route('/mit')
def mit():
    return render_template("mit.html")

@app.route('/imd')
def imd():
    return render_template("imd.html")

@app.route('/sat')
def sat():
    return render_template("sat.html")

@app.route('/bapat_home')
def bapat_home():
    return render_template("bapat_home.html")

if __name__ == "__main__":
    app.run(debug = True)