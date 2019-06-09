from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report,confusion_matrix
from sklearn import metrics
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd

class Classifiers():

    @staticmethod
    def Random_Forest(data):
        iris = load_iris()
        X = iris.data
        y = iris.target

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)
        clf_forest = RandomForestClassifier(n_estimators=15, max_depth=5)
        clf_forest.fit(X_train, y_train)

        y_pred = clf_forest.predict(X_test)
        #print(classification_report(y_test, y_pred))
        #print("Random Forest model accuracy(in %):", metrics.accuracy_score(y_test, y_pred) * 100)
        #print(confusion_matrix(y_test, y_pred))

        return clf_forest.predict(data)

    @staticmethod
    def Decision_Tree(data):
        iris = load_iris()
        features = iris.data
        target = iris.target
        target = pd.DataFrame(target, columns=['Class'])
        target['Class'] = target['Class'].map({0: "Iris setosa ", 1: "Iris virginica", 2: "Iris versicolor"}).values

        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.33, random_state=42)

        classifier_dt = DecisionTreeClassifier(random_state=0, criterion='gini', max_depth=5)
        classifier_dt.fit(X_train, y_train)

        y_pred = classifier_dt.predict(X_test)
        #print(classification_report(y_test, y_pred))
        #print("Decision Tree model accuracy(in %):", metrics.accuracy_score(y_test, y_pred) * 100)
        #print(confusion_matrix(y_test, y_pred))

        return classifier_dt.predict(data)

#print(Classifiers.Random_Forest([[1.8, 3, 2, 3]]))
#print(Classifiers.Decision_Tree([[1.8, 3, 2, 3]]))