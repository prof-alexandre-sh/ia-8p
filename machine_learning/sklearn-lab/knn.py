import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

data = pd.read_csv("data/credit_approval.csv")

print(data.head())
print(data.shape)
print(data['Target'].value_counts(normalize=True))

## KNN no Scikit Learn
from sklearn.neighbors import KNeighborsClassifier # módulo neighbors classe KNeighborsClassifier
metric = 'euclidean' ## Qual a métrica de distância
k = 3 # Número de vizinhos
knn = KNeighborsClassifier(metric=metric, n_neighbors=k) # Cria objeto knn
print(knn.get_params())

X = data.drop('Target', axis=1)
y = data['Target']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3)
print(X_train)
print(y_train)

knn.fit(X_train, y_train) ## Entregamos os dados de treino
preds = knn.predict(X_val) ## Entregamos os dados sem rótulos e realizamos a classificação
print(preds)
cmatrix = confusion_matrix(y_val, preds)
print(cmatrix)
print(accuracy_score(y_val, preds)) # Acurácia

# Fazendo plot da matriz de confusão
cm_display = ConfusionMatrixDisplay(confusion_matrix = cmatrix, display_labels = [False, True])
cm_display.plot()
plt.show() 