import streamlit as st
import pandas as pd
from binance.client import Client
import logging
from datetime import datetime
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('trading_bot.log'),
        logging.StreamHandler()
    ]
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        try:
            self.client = Client(api_key, api_secret, testnet=testnet)
            logging.info("Binance client initialized successfully")
        except Exception as e:
            logging.error(f"Failed to initialize client: {str(e)}")
            raise

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='MARKET',
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                if not price:
                    raise ValueError("Price required for limit orders")
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='LIMIT',
                    timeInForce='GTC',
                    quantity=quantity,
                    price=price
                )
            
            logging.info(f"Order placed: {order}")
            return order
            
        except Exception as e:
            logging.error(f"Order failed: {str(e)}")
            raise

    def get_account_info(self):
        try:
            info = self.client.futures_account()
            return info
        except Exception as e:
            logging.error(f"Account info failed: {str(e)}")
            return None

# Streamlit UI
st.set_page_config(page_title="Crypto Trading Bot", page_icon="🚀", layout="centered")

st.title("🚀 Binance Futures Trading Bot")
st.markdown("**Testnet Demo** - No real funds involved")

# Sidebar for API configuration
with st.sidebar:
    st.header("🔐 API Configuration")
    api_key = st.text_input("API Key", type="password")
    api_secret = st.text_input("API Secret", type="password")
    
    if st.button("Initialize Bot"):
        if api_key and api_secret:
            try:
                st.session_state.bot = BasicBot(api_key, api_secret)
                st.success("✅ Bot initialized successfully!")
            except Exception as e:
                st.error(f"❌ Initialization failed: {str(e)}")
        else:
            st.warning("Please enter both API key and secret")

# Main trading interface
if 'bot' in st.session_state:
    bot = st.session_state.bot
    
    # Account info
    with st.expander("📊 Account Overview", expanded=True):
        if st.button("Refresh Account Info"):
            account_info = bot.get_account_info()
            if account_info:
                st.metric("Total Wallet Balance", f"{float(account_info['totalWalletBalance']):.2f} USDT")
                st.metric("Available Balance", f"{float(account_info['availableBalance']):.2f} USDT")
    
    # Trading panel
    st.header("🎯 Place Order")
    
    col1, col2 = st.columns(2)
    
    with col1:
        symbol = st.text_input("Trading Pair", "BTCUSDT", help="e.g., BTCUSDT, ETHUSDT")
        order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
        side = st.selectbox("Side", ["BUY", "SELL"])
    
    with col2:
        quantity = st.number_input("Quantity", min_value=0.001, value=0.001, step=0.001)
        price = st.number_input("Price (for LIMIT orders)", min_value=0.0001, value=20000.0) if order_type == "LIMIT" else None
    
    # Order execution
    if st.button("🚀 Execute Order", type="primary"):
        with st.spinner("Placing order..."):
            try:
                order_result = bot.place_order(
                    symbol=symbol.upper(),
                    side=side,
                    order_type=order_type,
                    quantity=quantity,
                    price=price
                )
                
                st.success("✅ Order placed successfully!")
                st.json(order_result)
                
            except Exception as e:
                st.error(f"❌ Order failed: {str(e)}")
    
    # Order history and logs
    with st.expander("📋 Recent Logs"):
        if os.path.exists('trading_bot.log'):
            with open('trading_bot.log', 'r') as f:
                logs = f.readlines()[-20:]  # Last 20 lines
            st.text_area("Logs", "\n".join(logs), height=200)
        else:
            st.info("No logs available yet")

else:
    st.info("👈 Please configure your API keys in the sidebar to get started")
    st.markdown("""
    ### Getting Started:
    1. Register at [Binance Testnet](https://testnet.binancefuture.com)
    2. Generate API keys from the dashboard
    3. Enter your keys in the sidebar
    4. Start trading with virtual funds!
    """)

# Footer
st.markdown("---")
st.markdown("*This is a demo application for educational purposes only*")