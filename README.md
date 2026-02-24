Binance Futures Trading Bot

📌 Project Description

This project is a Python-based automated trading bot that places BUY/SELL market orders on Binance Futures using Binance API.
It demonstrates API integration, secure key handling using environment variables, and automated order execution via command line.

---

🚀 Features

- Place Market BUY/SELL Orders
- Binance Futures API Integration
- Secure API Key Storage using ".env"
- Command Line Order Execution
- Order Summary Output

---

🛠 Tech Stack

- Python 3
- python-binance
- python-dotenv
- REST API

---

📂 Project Structure

trading_bot/
│── main.py
│── binance_client.py
│── requirements.txt
│── .env.example
│── bot.log
│── README.md

---

⚙ Installation

Clone the repository:

git clone https://github.com/yourusername/trading-bot.git

Install dependencies:

pip install -r requirements.txt

---

🔑 Setup Environment Variables

Create a ".env" file:

BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret

---

▶ Run the Bot

python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

---

📊 Sample Output

Order Summary
Symbol : BTCUSDT
Side   : BUY
Type   : MARKET
Qty    : 0.001
