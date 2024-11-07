import pyautogui as pa
import time 
import pyperclip

pa.FAILSAFE = False

pa.press('win')
pa.write('chrome')
time.sleep(2)
pa.press('enter')
time.sleep(2)
pa.click(x=1137, y=484) #acessar planilha
time.sleep(2)


pa.hotkey('ctrl', 't')
time.sleep(3)
pa.click(x=686, y=485) #acessar o SEI
time.sleep(4)
pa.write("george.saraujo")
time.sleep(2)
pa.press('tab')
pa.write('-----')
pa.press('enter')
time.sleep(2)

pa.hotkey('ctrl', 't')
pa.click(x=1234, y=491) #acessar mapa cultural
time.sleep(4)
pa.click(x=1597, y=170) #acessar minha conta
time.sleep(2)
pa.click(x=1483, y=378) #acessar minha oportunidade
time.sleep(2)
pa.click(x=888, y=445) #acessar com permissão
time.sleep(2)
pa.click(x=1536, y=777) #acessar caju editar
time.sleep(2)
pa.click(x=853, y=413) #editargeorge.saraujo
time.sleep(2)
pa.click(x=1466, y=520) #acessar e expandir
time.sleep(2)
pa.click(x=646, y=740) #acessar lista de inscrições
time.sleep(2)


