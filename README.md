# AI Financial News Verification dApp on Stellar

## 🚀 Overview
This project is a decentralized application (dApp) that combines Machine Learning and blockchain technology to verify the authenticity of financial news.

It uses:
- AI model for fake news detection
- Sentiment analysis using VADER
- Stellar blockchain to store immutable hashes

---

## 🧠 Features
- Fake news classification (ML model)
- Sentiment analysis (Positive / Negative / Neutral)
- SHA256 hash generation
- Blockchain storage using Stellar testnet
- Transaction verification

---

## ⚙️ Tech Stack
- Python
- Streamlit
- Scikit-learn
- VADER Sentiment Analysis
- Stellar SDK
- Stellar Testnet Blockchain

---

## 🔗 Blockchain Integration
Each news article is hashed using SHA256 and stored on the Stellar blockchain using a Manage Data operation, ensuring immutability and transparency.

---

## 🛠 Setup Instructions

### 1. Clone repository

git clone https://github.com/amjadzkwn/AI-powered-financial-news-verification-dApp.git

cd stellar-fake-news-dapp

### 2. Install dependencies

pip install -r requirements.txt

### 3. Train model

python train.py

### 4. Run application

streamlit run app.py

---

## 🌐 Testnet Deployment
This project uses the Stellar Testnet for blockchain transactions.

Faucet:
https://lab.stellar.org/#account-creator?network=test

---

## 📊 How it works
1. User inputs financial news
2. AI model predicts fake or real
3. SHA256 hash is generated
4. Hash is stored on Stellar blockchain
5. Transaction ID is returned

---

## 🔐 Security
Only hashes are stored on blockchain. Original data remains off-chain for efficiency.

---

## 👨‍💻 Author
Muhammad Amjad Zakwan Bin Abu Hanipah
