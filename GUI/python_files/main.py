
from PyQt4 import QtCore, QtGui

from about_dialog import Ui_Dialog as win1_ui
from COM_detect import Ui_Dialog as win3_ui
from DUT_selection import Ui_Dialog as win2_ui
import sys

def call_window1():
    app = QtGui.QApplication(sys.argv)
    #For window 1
    Dialog1 = QtGui.QDialog()
    ui_1 = UI_WIN1()
    ui_1.setupUi(Dialog1)
    Dialog1.move(500,100)
    Dialog1.show()
    sys.exit(app.exec_())

def call_window2():
    app = QtGui.QApplication(sys.argv)
    #For window 2
    Dialog2 = QtGui.QDialog()
    ui_2 = win2_ui()
    ui_2.setupUi(Dialog2)
    Dialog2.move(500,100)
    Dialog2.setWindowModality(QtCore.Qt.ApplicationModal)
    Dialog2.exec_()
    sys.exit(app.exec_())

# Overriding virtual functions
class UI_WIN1(win1_ui):
    def win1_accept(self):
        print "2 Accepted"
        call_window2();
        sys.exit()

class UI_WIN2(win2_ui):
    def pushButton_click(self):
        print "2 terminal device pressed"
        print self.get_text()
        sys.exit()

    def pushButton_2_click(self):
        print "3 terminal device pressed"
        print self.get_text()
        sys.exit()

if __name__ == "__main__":
    call_window1()

    #For window 3
    #Dialog3 = QtGui.QDialog()
    #ui_3 = win3_ui()
    #ui_3.setupUi(Dialog3)
    #Dialog3.move(500,100)
    #Dialog3.show()

    #sys.exit(app.exec_())