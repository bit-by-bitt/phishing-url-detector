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
        'https://linkedin.com/in/user-profile',
        'https://sbisec3-co-jp-wekkgdkhvbopwwndlmytvtxbhpm.top',
        'http://bx5dqt.top/XpDG57SCXS/',
        'http://lr1bjq.top/XpDG57SCXS/',
        'https://to1lxu.top/XpDG57SCXS',
        'http://rp8qnw.top/nsCCtsCdx',
        'https://xycct.net/E9akU4/',
        'https://yahoo.co.jp/osVLilQKIl/nLQVCxkz/ysdlw...',
        'https://allegrolokalnie.pl-oferta2454925.icu/',
        'http://allegro.pl-oferta674353.icu',
        'https://vk.com/away.php?to=https%3A%2F%2Fnsjdiowm...',
        'http://garenaevo.site',
        'https://coinmarketcap.rnexc.com/home.html',
        'https://www.apple.com',
        'https://www.microsoft.com',
        'https://www.amazon.com',
        'https://www.nytimes.com',
        'https://www.tesla.com',
        'https://www.reddit.com',
        'https://www.youtube.com',
        'https://www.bbc.com/news',
        'https://www.nationalgeographic.com',
        'https://www.airbnb.com',
        'https://www.booking.com',
        'https://www.instagram.com',
        'https://www.facebook.com',
        'https://twitter.com',
        'https://www.dropbox.com',
        'https://www.zoom.us',
        'https://www.adobe.com',
        'https://www.mozilla.org',
        'https://www.paypal.com',
        'https://bankofamerica.com',
    ],
    'label': [
       
        1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ]
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

print("\n🔍 Phishing URL Detection Tool")
while True:
    url = input("Enter a URL to check (or type 'exit' to quit): ").strip()
    if url.lower() == 'exit':
        break
    url_vec = vectorizer.transform([url])
    prediction = model.predict(url_vec)[0]

    if prediction == 1:
        print("⚠️  This URL is likely PHISHING!\n")
    else:
        print("✅  This URL appears LEGITIMATE.\n")
