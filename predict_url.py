import pickle

# Load the trained model
with open("phishing_model.pkl", "rb") as f:
    model = pickle.load(f)

# Define feature extraction function (copy from above or import if in separate file)
def extract_features(url):
    import re
    from urllib.parse import urlparse
    features = {}
    features['Length'] = len(url)
    features['Has_IP_Address'] = 1 if re.match(r"(http|https)://\d+\.\d+\.\d+\.\d+", url) else 0
    features['Has_HTTPS'] = 1 if url.startswith("https") else 0
    features['Special_Chars'] = sum(char in url for char in ['@', '-', '_', '?', '=', '&'])
    domain = urlparse(url).netloc
    digits = sum(c.isdigit() for c in domain)
    features['Domain_Age'] = digits % 10
    return [features['Length'], features['Has_IP_Address'], features['Has_HTTPS'], features['Special_Chars'], features['Domain_Age']]

# Input URL to check
input_url = input("Enter URL to check: ")

# Extract features and predict
features = extract_features(input_url)
prediction = model.predict([features])[0]

# Output
print("\n🔍 Prediction:", "Phishing 🚨" if prediction == 1 else "Legit ✅")
