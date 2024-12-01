from machine import Pin, I2C
import network
import time
import urequests
import random

# 마이크로컨트롤러의 핀을 제어하기 위해 Pin 클래스를 불러옵니다
from machine import Pin
relay = Pin(1, Pin.OUT) # GPIO 1번 핀을 출력 모드로 설정합니다.

# WLAN 객체를 생성하고, 무선 LAN을 활성화합니다
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# 와이파이에 연결합니다
if not wlan.isconnected():
    wlan.connect("His_Kigdom_1F_2.4Ghz", "wkgehome9093")
    print("Waiting for Wi-Fi connection", end="...")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
else:
    print(wlan.ifconfig())
    print("WiFi is Connected")

# Firebase의 Realtime Database와 연결하기 위한 URL을 설정합니다
url = "https://test230729-default-rtdb.firebaseio.com"

# 초기 상태를 설정하여 Firebase에 업데이트합니다
초기값 = {'led': 1,}
urequests.patch(url+"/led.json", json = 초기값).json()

# Firebase에서 데이터를 가져오고, 이를 JSON 형태로 변환합니다
response = urequests.get(url+"/led.json").json()
print(response)
print(response['led'])

# 무한 루프를 실행하면서 Firebase에서 데이터를 계속 가져와서 LED와 팬의 상태를 제어합니다
while True:
    response = urequests.get(url+"/led.json").json()
    time.sleep(0.1)
    print("led:", response['led'])

    # 가져온 데이터에 따라서 LED 핀의 출력 값을 변경합니다
    if (response['led'] == 1) :
        relay.value(1) 
    else :
        relay.value(0)