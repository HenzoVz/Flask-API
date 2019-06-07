from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

app = Flask(__name__)

# Features and Labels
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
# RandomForestClassifier
clf_forest = RandomForestClassifier(n_estimators=15, max_depth=5)
clf_forest.fit(X_train, y_train)
clf_forest.score(X_test, y_test)

@app.route('/api',methods=['POST'])
def predict():

    s_length = request.get_json(force=True)
    s_width = request.get_json(force=True)
    p_length = request.get_json(force=True)
    p_width = request.get_json(force=True)

    prediction = clf_forest.predict(np.array(s_length['s_length'], s_width['s_width'], p_length['p_length'], p_width['p_width']))
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)