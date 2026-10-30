import pyautogui as pa 
import random
import time

time.sleep(5)

mensagens = ["Olá", "Boa tarde", "Tudo certo", "Oi", "Bora", "ta doido!"]
for i in range(30):
    msg = random.choices(mensagens)
    pa.write(msg)
    pa.press("enter")