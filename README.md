**Crypto Trading Bot 🤖**
A simplified Streamlit-based trading bot for Binance Futures Testnet that allows users to place market and limit orders with a clean web interface.

**🚀 Features**
🔐 Secure API Configuration - Password-protected key input

🎯 Trading Interface - Support for market/limit orders with buy/sell sides

📊 Account Overview - Real-time balance and portfolio information

📝 Comprehensive Logging - All API interactions and errors logged

🚀 One-Click Execution - Simple order placement with immediate feedback

📱 Responsive UI - Clean Streamlit interface that works on all devices

**🛠 Installation**
Prerequisites
Python 3.8+

Binance Testnet Account

Setup Steps
Clone the repository

bash
git clone <your-repo-url>
cd trading-bot
Install dependencies

bash
pip install streamlit python-binance
Get Binance Testnet API Keys

Visit testnet.binancefuture.com

Log in with your GitHub or Binance account

Navigate to API Management

Generate new API Key and Secret

Important: Save your Secret Key immediately - it won't be shown again!

Run the application

bash
streamlit run trading_bot.py
📋 Usage
Configure API Keys

Open the sidebar (click ➡️ in top-left)

Enter your API Key and Secret

Click "Initialize Bot"

View Account Info

Expand "Account Overview" section

Click "Refresh Account Info" to see balances

Place Orders

Select trading pair (e.g., BTCUSDT)

Choose order type (MARKET/LIMIT)

Select side (BUY/SELL)

Enter quantity and price (for limit orders)

Click "Execute Order"

🏗 Project Structure
text
trading-bot/
├── trading_bot.py          # Main Streamlit application
├── requirements.txt        # Python dependencies
├── trading_bot.log        # Generated log file
└── README.md              # This file
🔧 Code Overview
Main Components
BasicBot Class: Core trading functionality

API client initialization

Order placement (market/limit)

Account information retrieval

Streamlit UI: User interface

API configuration sidebar

Trading panel

Account overview

Log display

Key Functions
place_order(): Execute trades on Binance Futures

get_account_info(): Fetch account balances and positions

Comprehensive error handling and logging

⚙️ Configuration
Environment Variables (Optional)
For enhanced security, you can use environment variables:

bash
export BINANCE_API_KEY="your_api_key"
export BINANCE_API_SECRET="your_api_secret"
Logging
The application creates trading_bot.log with:

API requests and responses

Order execution details

Error messages for debugging

🛡 Security Notes
🔒 Never commit API keys to version control

🔒 Use testnet environment only - no real funds

🔒 API keys are stored only in session memory

🔒 All sensitive inputs are password-protected

🐛 Troubleshooting
Common Issues
"Invalid API key" error

Verify your API key and secret are correct

Check that you're using Futures Testnet keys

"Connection failed" error

Verify internet connection

Check Binance API status

"Insufficient balance" error

Testnet provides virtual funds - wait for reset if needed

Logs
Check trading_bot.log for detailed error information and API responses.

📈 Future Enhancements
Advanced order types (Stop-Limit, OCO)

TWAP execution

Portfolio analytics

Multiple exchange support

Backtesting framework

📄 License
This project is for educational purposes only. Use at your own risk.

⚠️ Disclaimer
This software is for educational and testing purposes only. Never use with real funds on mainnet. Cryptocurrency trading involves substantial risk of loss and is not suitable for every investor.

