import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import warnings
import pickle

# Suppress warnings
warnings.filterwarnings("ignore")

# Load dataset
data = pd.read_csv("phishing.csv")
print("Initial columns:", data.columns)

# Drop 'Index' and 'URL' columns if they exist
for col in ['Index', 'URL']:
    if col in data.columns:
        data = data.drop([col], axis=1)

# Check and drop missing values if any
if data.isnull().sum().sum() > 0:
    data = data.dropna()

# Separate features and labels
X = data.drop("Label", axis=1)
y = data["Label"]

# Convert label values from text to numeric
y = y.map({'Phishing': 1, 'Legit': 0})

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("\n--- Evaluation Metrics ---")
print(f"Accuracy:  {accuracy_score(y_test, y_pred):.3f}")
print(f"Precision: {precision_score(y_test, y_pred):.3f}")
print(f"Recall:    {recall_score(y_test, y_pred):.3f}")
print(f"F1 Score:  {f1_score(y_test, y_pred):.3f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save the model
with open("phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\n✅ Model saved as phishing_model.pkl")
