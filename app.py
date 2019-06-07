from flask import Flask, request
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from flasgger import Swagger
import numpy as np
import pandas as pd

app = Flask(__name__)
swagger = Swagger(app)


# Features and Labels
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
# RandomForestClassifier
clf_forest = RandomForestClassifier(n_estimators=15, max_depth=5)
clf_forest.fit(X_train, y_train)
clf_forest.score(X_test, y_test)

@app.route('/predict')
def predict():

    """Example endpoint returning a prediction of iris
    ---
    parameters:
      - name: s_length
        in: query
        type: number
        required: true
      - name: s_width
        in: query
        type: number
        required: true
      - name: p_length
        in: query
        type: number
        required: true
      - name: p_width
        in: query
        type: number
        required: true
    """
    s_length = request.args.get("s_length")
    s_width = request.args.get("s_width")
    p_length = request.args.get("p_length")
    p_width = request.args.get("p_width")
    print(type(s_length))
    prediction = clf_forest.predict(np.array([[s_length, s_width, p_length, p_width]]))
    print(prediction)
    print(type(prediction))
    return str(prediction)

@app.route('/predict_file', methods=["POST"])
def predict_iris_file():
    """Example file endpoint returning a prediction of iris
    ---
    parameters:
      - name: input_file
        in: formData
        type: file
        required: true
    """
    input_data = pd.read_csv(request.files.get("input_file"), header=None)
    prediction = clf_forest.predict(input_data)
    return str(list(prediction))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)