## DigiLight Control
Программа керування притроєм DigiLight

  ![window](/assets/window.png)

Програам працює в SystemTray

 ![window](/assets/win2.png)  ![window](/assets/win3.png)
 
***
DigiLight Control v0.1
***
що нового:
- Добавлений пунк в контекстному меню вимкнути світло

*** 
### Для збірки в Pyinstaller єкзешніка використовуем конструкцію

> pyinstaller --onefile --windowed --icon=image.ico main.py --hidden-import usb --add-binary="C:\Windows\System32\libusb0.dll;."

Була проблемма втому що скомпонований екзешнік не знаходив файл libusb його 
потріно явно указати