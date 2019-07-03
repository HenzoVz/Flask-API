from flask import Flask, request, json
from src.model import Classifiers

app = Flask(__name__)

@app.route('/predict',methods=['POST'])
def predict_iris():

    data1 = request.get_json(force=True)
    data2 = request.get_json(force=True)
    data3 = request.get_json(force=True)
    data4 = request.get_json(force=True)

    prediction = Classifiers.Random_Forest([[data1['s_length'], data2['s_width'], data3['p_length'], data4['p_width']]])
    #print(prediction)
    #print(type(prediction))

    if prediction == [0]:
       prediction_setosa = 'íris setosa'
       #print(prediction_setosa)
       return json.dumps(prediction_setosa)
    if prediction == [1]:
       prediction_virginica = 'íris virginica'
       #print(prediction_virginica)
       return  json.dumps(prediction_virginica)
    else:
       prediction_versicolor = 'íris versicolor'
       #print(prediction_versicolor)
       return json.dumps(prediction_versicolor)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)