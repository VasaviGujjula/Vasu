from flask import Flask, render_template, request
import pickle
import re
from urllib.parse import urlparse

app = Flask(__name__)

# Load the model
with open("phishing_model.pkl", "rb") as f:
    model = pickle.load(f)

# Feature extraction
def extract_features(url):
    features = {}
    features['Length'] = len(url)
    features['Has_IP_Address'] = 1 if re.match(r"(http|https)://\d+\.\d+\.\d+\.\d+", url) else 0
    features['Has_HTTPS'] = 1 if url.startswith("https") else 0
    features['Special_Chars'] = sum(char in url for char in ['@', '-', '_', '?', '=', '&'])
    domain = urlparse(url).netloc
    digits = sum(c.isdigit() for c in domain)
    features['Domain_Age'] = digits % 10
    return [features['Length'], features['Has_IP_Address'], features['Has_HTTPS'], features['Special_Chars'], features['Domain_Age']]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    features = extract_features(url)
    prediction = model.predict([features])[0]
    result = "Phishing 🚨" if prediction == 1 else "Legitimate ✅"
    return render_template('index.html', url=url, prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
