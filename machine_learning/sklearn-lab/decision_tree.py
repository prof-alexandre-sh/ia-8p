import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, ConfusionMatrixDisplay
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn import tree

data = pd.read_csv("data/Iris.csv")

#print(data.head())
#print(data.shape)

encode = LabelEncoder()
data['target'] = encode.fit_transform(data.Species)
print(data)

X = data.drop(['Species', 'target'], axis=1)
y = data['target']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3)
print(X_train)
print(y_train)

dt = tree.DecisionTreeClassifier()
model = dt.fit(X_train, y_train)
predictions = model.predict(X_val)
print(predictions)

cmatrix = confusion_matrix(y_val, predictions)
print(cmatrix)
print(accuracy_score(y_val, predictions)) # Acurácia

tree.plot_tree(model)