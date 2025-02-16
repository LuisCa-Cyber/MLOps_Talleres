import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# Asegura que la carpeta de modelos exista
os.makedirs("/home/app/models", exist_ok=True)

# Carga de datos (ajusta rutas si usas data local)
df1 = pd.read_csv("/home/app/data/penguins_lter.csv", sep=",")
df2 = pd.read_csv("/home/app/data/penguins_size.csv", sep=",")

# Limpieza y combinación (ejemplo)
df1["Sex"] = df1["Sex"].replace({".": None})
df2["sex"] = df2["sex"].replace({".": None})
df1_clean = df1.dropna(subset=["Sex"])
df2_clean = df2.dropna(subset=["sex"])
df1_clean = df1_clean.rename(columns={
    "Species": "species",
    "Island": "island",
    "Culmen Length (mm)": "culmen_length_mm",
    "Culmen Depth (mm)": "culmen_depth_mm",
    "Flipper Length (mm)": "flipper_length_mm",
    "Body Mass (g)": "body_mass_g",
    "Sex": "sex"
})
df1_clean = df1_clean[["species", "island", "culmen_length_mm", "culmen_depth_mm",
                       "flipper_length_mm", "body_mass_g", "sex"]]
df_combined = pd.concat([df1_clean, df2_clean], ignore_index=True)
df_combined["sex"] = df_combined["sex"].map({"MALE": 1, "FEMALE": 0})

# Codificar variable "island"
label_encoder = LabelEncoder()
df_combined["island"] = label_encoder.fit_transform(df_combined["island"])

# Seleccionar características y objetivo
X = df_combined[["culmen_length_mm", "culmen_depth_mm", "flipper_length_mm", "body_mass_g", "island"]]
y = df_combined["sex"]

# Normalizar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

# Modelos
models = {
    "random_forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "decision_tree": DecisionTreeClassifier(),
    "svm": SVC(kernel="linear"),
    "logistic_regression": LogisticRegression()
}

for name, model in models.items():
    model.fit(X_train, y_train)
    joblib.dump({"model": model, "scaler": scaler}, f"/home/app/models/{name}.pkl")

print("Modelos entrenados y guardados en /home/app/models")
