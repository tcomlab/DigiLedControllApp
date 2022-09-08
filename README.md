## DigiLight Control
Программа керування притроєм DigiLight

  ![window](/assets/window.png)

Програам працює в SystemTray

 ![window](/assets/win2.png)  ![window](/assets/pic2.png)
 
***
DigiLight Control v0.2
***
що нового:
- Доданий пункт в контекстному меню вимкнути світло v0.1
- Додана функція збереження налаштувать v0.2
- Программа автоматично вимикає освітлення коли программа закривается ато вимикаєтся пк v0.2
- Автоматичне ввімкненя  освітлення при ввімкненні  ПК v0.2

*** 
### Для збірки в Pyinstaller єкзешніка використовуем конструкцію

> pyinstaller --onefile --windowed --icon=image.ico main.py --hidden-import usb --add-binary="C:\Windows\System32\libusb0.dll;."

Була проблемма втому що скомпонований екзешнік не знаходив файл libusb його 
потріно явно указати