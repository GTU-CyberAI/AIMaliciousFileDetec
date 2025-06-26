import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report
import joblib

df = pd.read_csv("labeled_dataset.csv")
X = df.drop(columns=["Name", "Malware"])
y = df["Malware"]

# Save feature names
joblib.dump(X.columns.tolist(), "feature_names.pkl")

# Split data for proper evaluation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Cross-validation on training data
model = RandomForestClassifier(n_estimators=100, random_state=42)
cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring="f1")
print("Cross-validation F1 scores:", cv_scores)
print("Mean F1 score:", cv_scores.mean())

# Train the model
model.fit(X_train, y_train)

# Make predictions on test set
y_pred = model.predict(X_test)

#Create a graph of the feature importances
import matplotlib.pyplot as plt
import numpy as np
feature_importances = model.feature_importances_
indices = np.argsort(feature_importances)[::-1]
plt.figure(figsize=(10, 6))
plt.title("Feature Importances")
plt.bar(range(X.shape[1]), feature_importances[indices], align="center")
plt.xticks(range(X.shape[1]), X.columns[indices], rotation=90)
plt.tight_layout()
plt.savefig("feature_importances.png")
plt.close()

# Create a graph of confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
import seaborn as sns
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Benign", "Malware"], yticklabels=["Benign", "Malware"])
plt.title("Confusion Matrix (Test Set)")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("confusion_matrix.png")
plt.close()

#create a output png for model performance metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score
def plot_performance_metrics(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted')
    recall = recall_score(y_true, y_pred, average='weighted')
    
    metrics = {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall
    }
    
    plt.figure(figsize=(8, 6))
    plt.bar(metrics.keys(), metrics.values(), color=['blue', 'orange', 'green'])
    plt.title("Model Performance Metrics")
    plt.ylabel("Score")
    plt.ylim(0, 1)
    plt.savefig("model_performance_metrics.png")
    plt.close()

# Call the performance metrics function
plot_performance_metrics(y_test, y_pred)

# Print classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=["Benign", "Malware"]))

# Train final model on full dataset and save
print("Training final model on full dataset...")
final_model = RandomForestClassifier(n_estimators=100, random_state=42)
final_model.fit(X, y)
joblib.dump(final_model, "exe_malware_model.pkl")
print("Model trained and saved.")
