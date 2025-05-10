
import os
import requests
from datetime import datetime
from flask import Flask

# 텔레그램 설정
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def generate_btc_briefing():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    message = f"""
📈 [토미 BTC 9:01 브리핑] ({now})

✔️ 오늘 예상 고가: $104,000
✔️ 오늘 예상 저가: $102,200
✔️ RSI: 58 (중립~강세)
✔️ 진입 제안: $102,600 롱 / 목표 $104,000
✔️ 손절 제안: $101,900

💡 Have a profitable day!
"""
    return message

def send_telegram_message(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg}
    return requests.post(url, data=payload)

# ▶ 웹 서버 구성 (포트 열기용)
app = Flask(__name__)

@app.route("/")
def index():
    msg = generate_btc_briefing()
    res = send_telegram_message(msg)
    return f"✅ 브리핑 전송됨! Telegram 응답 코드: {res.status_code}"

# ▶ Render에서 요구하는 포트를 열기 위한 코드
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

