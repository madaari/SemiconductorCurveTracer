
from PyQt4 import QtCore, QtGui

from about_dialog import Ui_Dialog as win1_ui
from DUT_selection import Ui_Dialog as win2_ui
from COM_detect import Ui_Dialog as win3_ui
import sys,glob,serial

app = QtGui.QApplication(sys.argv)
#For window 1
Dialog1 = QtGui.QDialog()

#For window 2
Dialog2 = QtGui.QDialog()

#For window 3
Dialog3 = QtGui.QDialog()

device_type = "None"
device_name = "None"

# Overriding virtual functions
class UI_WIN1(win1_ui):
    def win1_accept(self):
        print "2 Accepted"
        Dialog1.done(1)
        call_window2();
        sys.exit()


class UI_WIN2(win2_ui):
    def pushButton_click(self):
        print "2 terminal device pressed"
        device_name = self.get_text()
        device_type = "2 terminal device"
        Dialog2.setVisible(False)
        call_window3(device_name,device_type)
        sys.exit()

    def pushButton_2_click(self):
        print "3 terminal device pressed"
        device_name = self.get_text()
        device_type = "3 terminal device"
        Dialog2.setVisible(False)
        call_window3(device_name,device_type)
        sys.exit()

class UI_WIN3(win3_ui):
    def pushButton_2_click(self):
        print "pushButton_2"
        sys.exit()

    def pushButton_click(self):
        print "pushButton"
        print serial_ports()
        #sys.exit()

ui_1 = UI_WIN1()
ui_2 = UI_WIN2()
ui_3 = UI_WIN3()

def call_window1():
    ui_1.setupUi(Dialog1)
    Dialog1.move(500,100)
    Dialog1.show()
    sys.exit(app.exec_())

def call_window2():

    ui_2.setupUi(Dialog2)
    Dialog2.move(500,100)
    Dialog2.setWindowModality(QtCore.Qt.ApplicationModal)
    Dialog2.exec_()
    sys.exit(app.exec_())

def call_window3(device_name,device_type):

    ui_3.setupUi(Dialog3)
    ui_3.set_label(device_name,device_type)
    Dialog3.move(500,100)
    Dialog3.setWindowModality(QtCore.Qt.ApplicationModal)
    Dialog3.exec_()
    sys.exit(app.exec_())

def serial_ports():
    """ Lists serial port names
        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    #ui_3.add_item("None",0)
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
            ui_3.add_item(port)
        except (OSError, serial.SerialException):
            pass
    return result

if __name__ == "__main__":
    call_window1()
    #call_window3()
    #For window 3
    #Dialog3 = QtGui.QDialog()
    #ui_3 = win3_ui()
    #ui_3.setupUi(Dialog3)
    #Dialog3.move(500,100)
    #Dialog3.show()

    sys.exit(app.exec_())