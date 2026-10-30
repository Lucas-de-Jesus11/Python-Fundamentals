import pyautogui 
import time 

#para não perder o controle da automação
#pyautogui.FAILSAFE = True

#pausa geral de 0.3 segundos(300 milessegundos)
pyautogui.PAUSE = 0.3

#espera um tempo para rodar
time.sleep(5)

#pegar posição do mouse
print(pyautogui.position())

#pegar o tamanho da tela/resolução
print(pyautogui.size())

#clicar com mouse
pyautogui.click(x=387, y=343, duration=1)

#clicar com botão direito do mouse
#pyautogui.click(x=381, y=835, button="right")

#dois clicks no mouse
#pyautogui.click(x=387, y=343, clicks="2")

#mover o mouse
pyautogui.moveTo(x=671, y=205, duration=1)

pyautogui.click(x=1218, y=292, duration=1)

pyautogui.scroll(-1850)

pyautogui.click(x=1019, y=477, duration=1)

#Funções do teclado
#pyautogui.press("win")

#Para escrever
#pyautogui.write("Clima", interval=0.25)
#pyautogui.press("enter", )

#para prssionar 2 teclas
#pyautogui.hotkey("ctrl", "v")