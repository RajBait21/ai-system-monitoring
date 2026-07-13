import pandas as pd
import joblib
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("data/system_metrics.csv")

features = [
    "cpu_usage",
    "memory_usage",
    "disk_usage",
    "network_sent_mb",
    "network_received_mb",
    "process_count",
    "temperature"
]

X = df[features]
y = df["risk_level"]

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded
)

mlflow.set_experiment("system_monitoring_prediction")

with mlflow.start_run():
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=12,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    mlflow.log_param("model", "RandomForestClassifier")
    mlflow.log_param("n_estimators", 200)
    mlflow.log_metric("accuracy", accuracy)

    mlflow.sklearn.log_model(model, "model")

    print("Accuracy:", round(accuracy * 100, 2), "%")
    print(classification_report(y_test, predictions))

joblib.dump(model, "ml/system_risk_model.pkl")
joblib.dump(label_encoder, "ml/label_encoder.pkl")

print("Model and encoder saved successfully.")