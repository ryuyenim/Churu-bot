import requests
from datetime import datetime, timedelta

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1367394347380768798/hzwiJLVkLh5bfhaKn1Z4hi7rh71QoIQxZhe8t5EqNII1LABpoIvRgpyVO-UEKqwpAbWK"

# 한국 시간 구하기
kst = datetime.utcnow() + timedelta(hours=9)
now = kst.strftime("%H:%M")

# 현재 시각별로 메시지 결정
alert = ""

if now in ["02:55", "05:55", "08:55", "11:55", "14:55", "17:55", "20:55", "23:55"]:
    alert = f"@everyone\n🔔 **[츄르봇 알림]**\n`{now}` │ ⚠️ 불길한 소환의 결계 5분 전! 모두 사냥터로 모이세요!"

elif now in ["12:00", "18:00", "20:00", "22:00"]:
    alert = f"@everyone\n🔔 **[츄르봇 알림]**\n`{now}` │ ⚔️ 필드 보스 등장 시간입니다! **<늑대의 숲-페리>, <여신의 뜰-크라브바흐>, <얼음 협곡-크라마>"

# 메시지가 있으면 전송
if alert:
    response = requests.post(WEBHOOK_URL, json={"content": alert})
    print(f"전송 완료! 상태 코드: {response.status_code}")
else:
    print(f"[{now}] 알림 시간 아님. 패스.")
