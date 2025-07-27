# 🛡️ Phishing URL Detector

This project is a simple machine learning model that classifies URLs as **phishing** or **legitimate** using **TF-IDF vectorization** and a **Random Forest Classifier**. It's a great example of how cybersecurity and AI can work together to identify malicious links.

---

## 📌 Project Overview

Phishing is a common attack method used to trick users into giving away sensitive information by disguising malicious links. This tool analyzes the structure of a URL and predicts whether it's likely to be part of a phishing attempt.

---

## 🧠 Features

- URL-based phishing detection
- TF-IDF vectorization of URL text
- Random Forest classification
- Performance metrics (accuracy, precision, recall, F1-score)

---

## 📁 Dataset

This example uses a small, manually labeled dataset of URLs:

- `1` = Phishing  
- `0` = Legitimate

You can easily expand it with datasets from:
- [PhishTank](https://www.phishtank.com/)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/)

---

## ⚙️ Installation

Clone the repo and install the requirements:

```bash
git clone https://github.com/bit-by-bitt/phishing-url-detector.git
cd phishing-url-detector
pip install -r requirements.txt
