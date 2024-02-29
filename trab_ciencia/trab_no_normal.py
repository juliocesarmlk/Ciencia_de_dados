from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
# Carregar o conjunto de dados Iris
iris = datasets.load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
random_state=42)

model_loigistc = LogisticRegression()
model_loigistc.fit(X_train, y_train)

previsao_previsiva = model_loigistc.predict(X_test)
acerto = accuracy_score(y_test, previsao_previsiva)

print(acerto)