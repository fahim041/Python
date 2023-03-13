class UsbPort:
    def __init__(self):
        self.portAvailable = True

    def plug(self, usb):
        if self.portAvailable:
            usb.plugUsb()
            self.portAvailable = False


class UsbCable:
    def __init__(self):
        self.isPlugged = False

    def plugUsb(self):
        self.isPlugged = True


class MicroUsb:
    def __init__(self):
        self.isPlugged = False

    def plugMicroUsb(self):
        self.isPlugged = True


class MicroToUsbAdapter(UsbCable):
    def __init__(self, microUsb):
        self.microUsb = microUsb

    def plugUsb(self):
        self.microUsb.plugMicroUsb()


usbCable = UsbCable()
port1 = UsbPort()
port1.plug(usbCable)

micro = MicroUsb()
adapter = MicroToUsbAdapter(micro)
port2 = UsbPort()
port2.plug(adapter)

port3 = UsbPort()

print(port1.portAvailable)
print(port2.portAvailable)
print(port3.portAvailable)
