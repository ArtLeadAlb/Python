import pyautogui
import pyperclip
import time

pyautogui.PAUSE=3 #define pausa entre os comandos

pyautogui.press ('win')
pyperclip.copy('chrome')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
pyperclip.copy('https://salavirtual.castelobranco.br/login/index.php')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(5)

#print(pyautogui.position()) #mostra a posição x,y do mouse / bom usar um time.sleep() antes para dar tempo de posicionar o cursor


pyautogui.click(x=533,y=491)
pyautogui.click(x=847, y=239)
time.sleep(2)
pyautogui.click(x=677, y=574)
pyautogui.click(x=470, y=500)
time.sleep(5)
pyautogui.click(x=26, y=479)
pyautogui.click(x=1280, y=253)
#pyautogui.click(x=,y=, clicks=2, button=right)