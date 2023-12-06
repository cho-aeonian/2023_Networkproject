#피코의 GPIO 1번 핀을 제어 핀으로 사용하고
#릴레이 모듈을 1초마다 ON/OFF하는 코드

#from machine import Pin, Timer
#import utime

#relay=Pin(1, Pin.OUT) #GPIO 1번 핀을 출력 모드로 설정

#while True:
#    relay.value(not relay.value()) #현재 핀 상태를 반전시킴
#    utime.sleep(1) #1초 동안 대기