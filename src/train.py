import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
import joblib
import hashlib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from src.features import preparar_dados
import os


df = pd.read_csv("data/raw/dataset.csv")
df = preparar_dados(df)

X = df.drop("Label", axis=1)
y = df["Label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=150, max_depth=20, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(classification_report(y_test, pred))

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model.pkl")

with open("models/model.pkl", "rb") as f:
    dados = f.read()
hash_modelo = hashlib.sha256(dados).hexdigest()
with open("models/model_hash.txt", "w") as f:
    f.write(hash_modelo)

print("Modelo treinado e hash gerado:", hash_modelo)
