
import os
import requests
from datetime import datetime

# === 사용자 맞춤 정보 입력 ===
BOT_TOKEN = "여기에_당신의_Telegram_Bot_Token"
CHAT_ID = "여기에_당신의_Chat_ID"

# === 메시지 생성 ===
def generate_btc_briefing():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    message = f"""
📈 [토미 BTC 9:01 브리핑] ({now})

✔️ 오늘 예상 고가: $104,000
✔️ 오늘 예상 저가: $102,200
✔️ RSI: 58 (중립~강세)
✔️ 진입 제안: $102,600 롱 / 목표 $104,000
✔️ 손절 제안: $101,900

💡 참고: 기술적 지표 및 맥스웰 기반 예측.
Have a profitable day!
"""
    return message

# === 텔레그램 전송 함수 ===
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response

# === 실행 ===
if __name__ == "__main__":
    briefing = generate_btc_briefing()
    send_telegram_message(briefing)
