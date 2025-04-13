import telegram
import random
import time
from apscheduler.schedulers.blocking import BlockingScheduler

# YOUR BOT TOKEN AND CHAT ID
BOT_TOKEN = '8087870326:AAGh6LZXVpGvF9Un80SbvbDyHEoVoEAsj9w'
CHAT_ID = '518178616'

bot = telegram.Bot(token=BOT_TOKEN)

# Function to predict next round (currently random)
def predict_round():
    prediction = round(random.uniform(1.00, 3.00), 2)  # random float between 1.00 and 3.00
    return prediction

# Function to send prediction
def send_prediction():
    prediction = predict_round()
    message = f"Next Aviator Prediction: {prediction}x\n(Always play responsibly)"
    bot.send_message(chat_id=CHAT_ID, text=message)

# Scheduler to send prediction every 5 minutes
scheduler = BlockingScheduler()
scheduler.add_job(send_prediction, 'interval', minutes=5)

print("Bot is running...")
send_prediction()  # Send one immediately on start
scheduler.start()
