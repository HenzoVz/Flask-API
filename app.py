import os
from flask import Flask, request
from model import Classifiers

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_iris():

    s_length = request.get_json(force=True)
    s_width = request.get_json(force=True)
    p_length = request.get_json(force=True)
    p_width = request.get_json(force=True)

    prediction = Classifiers.Random_Forest([[s_length['s_length'], s_width['s_width'], p_length['p_length'], p_width['p_width']]])
    if prediction == [0]:
       iris_setosa = 'Iris Setosa'
       print(iris_setosa)
       return iris_setosa
    if prediction == [1]:
       iris_virginica = 'Iris Virginica'
       print(iris_virginica)
       return iris_virginica
    else:
       iris_versicolor = 'Iris Versicolor'
       print(iris_versicolor)
       return iris_versicolor

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)