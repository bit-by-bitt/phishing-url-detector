import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

data = {
    'url': [
        'http://paypal.com-login.secure.verify.account.update',
        'https://www.google.com',
        'http://bankofamerica.verify-id-secure.net',
        'https://github.com',
        'http://facebook.com.account.recovery.attempt',
        'https://openai.com/research',
        'http://amazon.verify.payment.gateway.login.page',
        'https://stackoverflow.com/questions',
        'http://netflix-update-account-info.com',
        'https://linkedin.com/in/user-profile'
    ],
    'label': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
X_train, X_test, y_train, y_test = train_test_split(df['url'], df['label'], test_size=0.3, random_state=42)
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_tfidf, y_train)

y_pred = model.predict(X_test_tfidf)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred, target_names=["Legitimate", "Phishing"]))
