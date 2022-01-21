import cv2
import numpy as np
import requests

message = "2 People detected not wearing Personal Protective Equipment on Camera TC1-1"
chat_id = #"-621237173"
token = "2056724981:AAFUwGHdfFueiobcVddhJV0z0o6ozM8Qcnw"

image = cv2.imread('send.png')
color = (0, 0, 255)
thickness = 2

image = cv2.rectangle(image, (900,170), (915,227), color, thickness)
image = cv2.rectangle(image, (1084,211), (1106,250), color, thickness)


try:
    baseUrl = f'https://api.telegram.org/bot{token}/'
    print("1")
    parameters= {'chat_id':chat_id, 'text':message}
    resp= requests.post(baseUrl+'sendMessage',data= parameters)
    print("1")
    _, imgen = cv2.imencode('.jpg', image)
    filee = {'photo': imgen.tobytes()}
    parameters = {'chat_id': chat_id}
    resp = requests.post(baseUrl + 'sendPhoto', data=parameters, files=filee)
except Exception as e:
    print(f"[Telegram Exception] Exception: {e}")
    pass