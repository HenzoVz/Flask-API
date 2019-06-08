from flask import Flask, request
from model import Classifiers

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_iris():

    data1 = request.get_json(force=True)
    data2 = request.get_json(force=True)
    data3 = request.get_json(force=True)
    data4 = request.get_json(force=True)

    prediction = Classifiers.Random_Forest([[data1['s_length'], data2['s_width'], data3['p_length'], data4['p_width']]])
    return str(prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)