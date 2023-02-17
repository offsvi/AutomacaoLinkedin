import pyautogui
import time

# Esse comando é um alerta para que enquanto o programa é executado não seja interrompido
pyautogui.alert("O código vai começar não mexa em nada no computador")
# PAUSE serve para que em cada tecla digitada tenha uma pausa de meio segundo
pyautogui.PAUSE = 0.5
# comando press serve para precionar uma tecla
pyautogui.press('winleft')
# Serve para digitar o texto que sera colocado entre aspas
pyautogui.write('brave')
pyautogui.press('enter')
# Biblioteca time serve para que vc adcione um tempo ao seu código somete naquela posição
time.sleep(1)
pyautogui.write('https://linkedin.com.br')
pyautogui.press('enter')
# Serve para que utilize combinações de teclas
# pyautogui.hotkey('winleft', 'd')

pyautogui.position()
