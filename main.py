'''
Программа керування світодіодним контрлером

04.05.2022 by TC0mLab
'''

import ArduinoUsb
from pystray import MenuItem as item
import pystray
from PIL import Image
import tkinter as tk
from tkinter import Scale, HORIZONTAL, Button, Label


class light_control:

    window = tk.Tk()

    # Формуємо та віправляємо пакет по шині USB
    def control(self):
        self.digispark.write(1)
        self.digispark.write(int(self.w1.get()*2.551))
        self.digispark.write(int(self.w2.get()*2.551))
        self.digispark.write(int(self.w3.get()*2.551))
        self.digispark.write(0)

    def quit_window(self, icon, item):
        icon.stop()
        self.window.destroy()

    def show_window(self, icon, item):
        icon.stop()
        self.window.after(0, self.window.deiconify)

    # Формуємо та віправляємо пакет по шині USB
    def off_light(self,icon, item):
        self.digispark.write(1)
        self.digispark.write(0)
        self.digispark.write(0)
        self.digispark.write(0)
        self.digispark.write(0)

    def withdraw_window(self):
        self.window.withdraw()
        image = Image.open("image.ico")
        menu = (item('Вимкнути світло', self.off_light),item('Показати вікно', self.show_window), item('Вихід', self.quit_window) )
        icon = pystray.Icon("name", image, "title", menu)
        icon.run()

    def Start(self):

        try:
            self.digispark = ArduinoUsb.ArduinoUsbDevice(idVendor=0x16c0, idProduct=0x05df)

        except:
            self.win = tk.Tk()
            self.win.title("Control")
            self.win.geometry("200x40")
            label1 = Label(self.win, text="USB Пристрій не знайденний", fg="#eee", bg="#333")
            label1.pack()
            self.win.protocol('WM_DELETE_WINDOW')
            self.win.mainloop()
            return

        self.window.title("Control")
        self.window.geometry("200x280")
        self.w1 = Scale(self.window, from_=0, to=100, tickinterval=20, orient=HORIZONTAL, length=190, label="Канал 1 Яскравість в %", resolution=5)
        self.w1.pack()

        self.w2 = Scale(self.window, from_=0, to=100, tickinterval=20, orient=HORIZONTAL, length=190, label="Канал 2 Яскравість в %", resolution=5)
        self.w2.pack()

        self.w3 = Scale(self.window, from_=0, to=100, tickinterval=100, orient=HORIZONTAL, length=190, label="Канал 3", resolution=100)
        self.w3.pack()

        btn = Button(self.window, text="Встановити", command=self.control)
        btn.pack()

        self.window.protocol('WM_DELETE_WINDOW', self.withdraw_window)
        self.window.mainloop()


if __name__ == "__main__":
    light = light_control()
    light.Start()
