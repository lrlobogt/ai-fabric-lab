from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pickle

print("Entrenando modelo...")
X, y = load_iris(return_X_y=True)
clf = LogisticRegression(random_state=0, max_iter=1000).fit(X, y)

with open('modelo.pkl', 'wb') as f:
    pickle.dump(clf, f)

print("¡Modelo guardado en modelo.pkl!")