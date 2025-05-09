import re
from urllib.parse import urlparse

def extract_features(url):
    features = {}
    features['Length'] = len(url)
    features['Has_IP_Address'] = 1 if re.match(r"(http|https)://\d+\.\d+\.\d+\.\d+", url) else 0
    features['Has_HTTPS'] = 1 if url.startswith("https") else 0
    features['Special_Chars'] = sum(char in url for char in ['@', '-', '_', '?', '=', '&'])
    
    domain = urlparse(url).netloc
    digits = sum(c.isdigit() for c in domain)
    features['Domain_Age'] = digits % 10  # Dummy logic — in real cases, you'd query WHOIS data
    
    return [features['Length'], features['Has_IP_Address'], features['Has_HTTPS'], features['Special_Chars'], features['Domain_Age']]
