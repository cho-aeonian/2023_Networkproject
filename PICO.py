from machine import Pin, I2C
import network
import time
import urequests
import random

#마이크로 컨트롤러의 핀을 제어하기 위해 Pin 클래스를 불러옴
from machine import Pin
relay=Pin(1,Pin.OUT) #GPIO 1번 핀을 출력 모드로 설정

#WLAN 객체를 생성하고, 무선 LAN을 활성화함
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

#와이파이에 연결
if not wlan.isconnected():
    wlan.connect("His_Kigdom_1F_2.4Ghz","wkgehome9093")
    print("Waiting for Wi-Fi connection", end="...")
    while not wlan.isconnected():
        print(".",end="")
        time.sleep(1)

else:
    print(wlan.ifconfig())
    print("Wifi is Connected")

#Firebase의 Realtime Database와 연결하기 위한 URL을 설정
url = "https://test"