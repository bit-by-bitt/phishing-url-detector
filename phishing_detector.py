import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score


data = {
    'url': [
        
        'http://paypal.com-login.secure.verify.account.update',
        'http://bankofamerica.verify-id-secure.net',
        'http://facebook.com.account.recovery.attempt',
        'http://amazon.verify.payment.gateway.login.page',
        'http://netflix-update-account-info.com',
        'http://sbisec3-co-jp-wekkgdkhvhbopwwndlmytvtxbhpm.top',
        'http://bx5qdt.top/XpDG57SCXS/',
        'http://lr1bjq.top/XpDG57SCXS/',
        'http://to1lxu.top/XpDG57SCXS',
        'http://rp8qnw.top/nsCCtsCdx',
        'http://xycct.net/E9akU4/',
        'http://yahoo.co.jp/osVliLqKIl/nLQVCxkz/ysdlw...',
        'http://allegrolokalnie.pl-oferta2454925.icu/',
        'http://allegro.pl-oferta674353.icu',
        'http://vk.com/away.php?to=https%3A%2F%2Fsnjsdiowm...',
        'http://garenaevo.site',
        'https://coinmarketcap.rnexc.com/home.html',
        'https://www.google.com',
        'https://github.com',
        'https://openai.com/research',
        'https://stackoverflow.com/questions',
        'https://linkedin.com/in/user-profile'
    ],
    'label': [
        
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  
        0, 0, 0, 0, 0                                    
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
