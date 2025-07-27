import pandas as pd
import re
from urllib.parse import urlparse
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

def extract_features(url):
    parsed = urlparse(url)
    hostname = parsed.hostname or ""
    path = parsed.path or ""
    features = {
        'url_length': len(url),
        'has_https': 1 if parsed.scheme == 'https' else 0,
        'num_dots': url.count('.'),
        'suspicious_words': int(any(word in url.lower() for word in ['login', 'verify', 'secure', 'account', 'update', 'support'])),
        'has_ip': 1 if re.match(r'^(\d{1,3}\.){3}\d{1,3}', parsed.netloc) else 0,
        'num_subdomains': len(hostname.split('.')) - 2 if len(hostname.split('.')) > 2 else 0
    }
    return pd.Series(features)

data = {
    'url': [
        'https://www.google.com',
        'https://github.com',
        'https://openai.com/research',
        'https://stackoverflow.com/questions',
        'https://linkedin.com/in/user-profile',
        'https://www.microsoft.com',
        'https://www.apple.com',
        'https://www.amazon.com',
        'https://www.facebook.com/login',
        'https://www.netflix.com/browse',
        'http://paypal.com-login.secure.verify.account.update',
        'http://bankofamerica.verify-id-secure.net',
        'http://facebook.com.account.recovery.attempt',
        'http://amazon.verify.payment.gateway.login.page',
        'http://netflix-update-account-info.com',
        'https://secure-login-amazon-support.com',
        'http://123.456.789.123/login',
        'https://paypal.com-login.verify-payment.com',
        'http://allegropl-oferta674353.icu',
        'http://bx5qdt.top/XpDG57SCXS/'
    ],
    'label': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)
features = df['url'].apply(extract_features)
X = pd.DataFrame(features)
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred, target_names=["Legitimate", "Phishing"]))

print("\n🔍 Phishing URL Detection Tool")
while True:
    input_url = input("Enter a URL to check (or type 'exit' to quit): ").strip()
    if input_url.lower() == 'exit':
        break
    input_features = extract_features(input_url).to_frame().T
    prediction = model.predict(input_features)[0]
    if prediction == 1:
        print("⚠️  This URL is likely PHISHING!\n")
    else:
        print("✅  This URL appears LEGITIMATE.\n")
