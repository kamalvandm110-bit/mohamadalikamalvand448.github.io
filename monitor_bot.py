import requests
import time
import hashlib
from telegram import Bot
from telegram.error import TelegramError

# تنظیمات
BOT_TOKEN = 'YOUR_BOT_TOKEN'  # از BotFather
CHAT_ID = 'YOUR_CHAT_ID'  # از @userinfobot
SITE_URL = 'https://mohamadalikamalvand448.github.io/'
SITEMAP_URL = 'https:/mohamadalikamalvand448.github.io/sitemap.xml'
PREV_HASH = ''  # هش قبلی سایت

bot = Bot(token=BOT_TOKEN)

def check_site():
    try:
        resp = requests.get(SITE_URL)
        if resp.status_code != 200:
            send_alert(f"🚨 سایت {SITE_URL} خطا داد: {resp.status_code}")
            return
        
        current_hash = hashlib.md5(resp.content).hexdigest()
        global PREV_HASH
        if PREV_HASH and current_hash != PREV_HASH:
            send_alert(f"🔄 تغییر در سایت {SITE_URL} تشخیص داده شد! (هش جدید: {current_hash[:8]})")
        
        PREV_HASH = current_hash
        
        # چک sitemap برای ایندکس
        sitemap_resp = requests.get(SITEMAP_URL)
        if sitemap_resp.status_code == 200:
            send_alert(f"✅ Sitemap OK – آماده ایندکس گوگل")
        else:
            send_alert(f"⚠️ Sitemap مشکل دارد: {sitemap_resp.status_code}")
            
    except Exception as e:
        send_alert(f"❌ خطا در نظارت: {str(e)}")

def send_alert(message):
    try:
        bot.send_message(chat_id=CHAT_ID, text=message)
    except TelegramError as e:
        print(f"خطا ارسال: {e}")

# لوپ نظارت (هر 300 ثانیه = 5 دقیقه)
while True:
    check_site()
    time.sleep(300)
