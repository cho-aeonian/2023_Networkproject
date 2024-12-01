from machine import Pin, Timer
import utime

relay = Pin(1, Pin.OUT) #GPIO 1번 핀을 출력 모드로 설정

while True:
    relay.value(not relay.value()) #현재 핀 상태 반전
    utime.sleep(1)