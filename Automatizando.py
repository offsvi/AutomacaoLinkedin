import pyautogui
import time

# Esse comando é um alerta para que enquanto o programa é executado não seja interrompido
pyautogui.alert("O código vai começar não mexa em nada no computador")

# PAUSE serve para que em cada tecla digitada tenha uma pausa de 1 segundo
pyautogui.PAUSE = 1

# comando press serve para precionar uma tecla
pyautogui.press('winleft')

# Serve para digitar o texto que sera colocado entre aspas
pyautogui.write('brave')
pyautogui.press('enter')

# Biblioteca time serve para que vc adcione um tempo ao seu código somete naquela posição
time.sleep(1)
pyautogui.write('https://linkedin.com.br')
pyautogui.press('enter')
time.sleep(8)

# Serve para que o mouse va até a cordenada desejada
pyautogui.moveTo(679, 130)
pyautogui.leftClick()
time.sleep(4)
pyautogui.moveTo(920, 120)
pyautogui.leftClick()
pyautogui.scroll(-2000)
pyautogui.sleep(3)
pyautogui.moveTo(599, 117)
pyautogui.leftClick()
pyautogui.sleep(2)

pyautogui.alert("Programa encerrado. Pode voltar a usar porra")



# Serve para que utilize combinações de teclas
# pyautogui.hotkey('winleft', 'd')

#Esse programa pressiona com o mouse
#pyautogui.mouseDown()
