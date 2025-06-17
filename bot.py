import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler

TOKEN = "YOUR_BOT_TOKEN"  # ← Replace with your token from @BotFather

def start(update: Update, context):
    update.message.reply_text("🚀 Trading Bot Active! Use /price BTC")

def price(update: Update, context):
    crypto = context.args[0].lower() if context.args else "bitcoin"
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    data = requests.get(url).json()
    update.message.reply_text(f"{crypto.upper()}: ${data[crypto]['usd']}")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("price", price))
updater.start_polling()
