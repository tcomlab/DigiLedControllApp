

import usb
from pystray import MenuItem as item
import pystray
from PIL import Image
import tkinter as tk
from tkinter import Scale, HORIZONTAL, Button, Label


def getStringDescriptor(device, index):
    """
    """
    response = device.ctrl_transfer(usb.util.ENDPOINT_IN,
                                    usb.legacy.REQ_GET_DESCRIPTOR,
                                    (usb.util.DESC_TYPE_STRING << 8) | index,
                                    0,  # language id
                                    255)  # length

    # TODO: Refer to 'libusb_get_string_descriptor_ascii' for error handling

    return response[2:].tostring().decode('utf-16')


REQUEST_TYPE_SEND = usb.util.build_request_type(usb.util.CTRL_OUT,
                                                usb.util.CTRL_TYPE_CLASS,
                                                usb.util.CTRL_RECIPIENT_DEVICE)

REQUEST_TYPE_RECEIVE = usb.util.build_request_type(usb.util.CTRL_IN,
                                                   usb.util.CTRL_TYPE_CLASS,
                                                   usb.util.CTRL_RECIPIENT_DEVICE)

USBRQ_HID_GET_REPORT = 0x01
USBRQ_HID_SET_REPORT = 0x09
USB_HID_REPORT_TYPE_FEATURE = 0x03


class ArduinoUsbDevice(object):
    """
    """

    def __init__(self, idVendor, idProduct):
        """
        """
        self.idVendor = idVendor
        self.idProduct = idProduct

        # TODO: Make more compliant by checking serial number also.
        self.device = usb.core.find(idVendor=self.idVendor,
                                    idProduct=self.idProduct)

        if not self.device:
            raise Exception("Device not found")

    def write(self, byte):
        """
        """
        # TODO: Return bytes written?
        # print "Write:"+str(byte)
        self._transfer(REQUEST_TYPE_SEND, USBRQ_HID_SET_REPORT,
                       byte,
                       [])  # ignored

    def read(self):
        """
        """
        response = self._transfer(REQUEST_TYPE_RECEIVE, USBRQ_HID_GET_REPORT,
                                  0,  # ignored
                                  1)  # length

        if not response:
            raise Exception("No Data")

        return response[0]

    def _transfer(self, request_type, request, index, value):
        """
        """
        return self.device.ctrl_transfer(request_type, request,
                                         (USB_HID_REPORT_TYPE_FEATURE << 8) | 0,
                                         index,
                                         value)

    @property
    def productName(self):
        """
        """
        return getStringDescriptor(self.device, self.device.iProduct)

    @property
    def manufacturer(self):
        """
        """
        return getStringDescriptor(self.device, self.device.iManufacturer)

digispark = None

try:
    digispark = ArduinoUsbDevice(idVendor=0x16c0, idProduct=0x05df)

except:
    win = tk.Tk()
    win.title("Welcome")
    win.geometry("200x40")
    label1 = Label(win, text="USB Пристрій не знайденний", fg="#eee", bg="#333")
    label1.pack()
    win.protocol('WM_DELETE_WINDOW')
    win.mainloop()
    exit(0)


window = tk.Tk()
window.title("Welcome")
window.geometry("200x280")
w1 = Scale(window, from_=0, to=255, tickinterval=51, orient=HORIZONTAL, length=190, label="CH1", resolution=5)
w1.pack()

w2 = Scale(window, from_=0, to=255, tickinterval=51, orient=HORIZONTAL, length=190, label="CH2", resolution=5)
w2.pack()

w3 = Scale(window, from_=0, to=255, tickinterval=51, orient=HORIZONTAL, length=190, label="CH3", resolution=5)
w3.pack()


def helloCallBack():
    digispark.write(1)
    digispark.write(w1.get())
    digispark.write(w2.get())
    digispark.write(w3.get())
    digispark.write(0)
    pass


btn = Button(window, text ="Set PWM", command = helloCallBack)
btn.pack()


def quit_window(icon, item):
    icon.stop()
    window.destroy()


def show_window(icon, item):
    icon.stop()
    window.after(0, window.deiconify)


def withdraw_window():
    window.withdraw()
    image = Image.open("image.ico")
    menu = (item('Show', show_window), item('Quit', quit_window) )
    icon = pystray.Icon("name", image, "title", menu)
    icon.run()


window.protocol('WM_DELETE_WINDOW', withdraw_window)
window.mainloop()
