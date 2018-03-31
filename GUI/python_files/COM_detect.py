# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'COM_detect.ui'
#
# Created: Sat Mar 31 04:26:33 2018
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    number = 0
    dev_name = ""
    dev_type = ""
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(475, 371)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 451, 31))
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 100, 181, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(260, 150, 51, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(290, 170, 151, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_3.setWordWrap(True)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 111, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.label_4.setPalette(palette)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 270, 281, 31))
        self.progressBar.setProperty("value", 8)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(300, 270, 161, 31))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 310, 131, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 320, 154, 44))
        self.label_6.setStyleSheet(_fromUtf8(" background-color: white;\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-color: black;\n"
" max-width:150px;\n"
" max-height:40px;\n"
" min-width:150px;\n"
" min-height:40px;\n"
"background-image: url(../images/cedt.jpg)"))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("images/cedt.png")))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(150, 10, 311, 41))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 100, 231, 121))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.number = 0
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 371, 41))
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_click)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_2_click)
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), self.listWidget_update)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Make sure the device is connected and then press Detect COM Port", None))
        self.pushButton.setText(_translate("Dialog", "Detect COM Port", None))
        self.label_2.setText(_translate("Dialog", "Status:", None))
        self.label_3.setText(_translate("Dialog", "COM Port undetected", None))
        self.label_4.setText(_translate("Dialog", "Device selected:", None))
        self.pushButton_2.setText(_translate("Dialog", "Proceed", None))
        self.label_7.setText(_translate("Dialog", "2 terminal device named Blue LED", None))
        self.label_8.setText(_translate("Dialog", "Select the desired COM port and click on Proceed", None))

    def pushButton_2_click(self):
        print "pushButton_2"
        sys.exit()

    def pushButton_click(self):
        print "pushButton"
        sys.exit()

    def set_label(self,device_name,device_type):
        self.label_7.setText(_translate("Dialog", device_type+" named "+device_name, None))
        self.dev_type = device_type
        self.dev_name = device_name

    def add_item(self,text,number=1):
        item = self.listWidget.item(self.number)
        if number == 1:
            item = self.listWidget.item(0)
            item.setText(_translate("Dialog", text, None))
            self.number = self.number + 1
        else:
            if number == 0:
                item = self.listWidget.item(0)
                item.setText(_translate("Dialog", text, None))

    def set_progressbar_value(self,value):
        self.progressBar.setProperty("value", value)

    def set_progress_label(self,text):
        self.label_5.setText(_fromUtf8(""+text))

    def listWidget_update(self):
        print "selected"
        print self.listWidget.currentItem().text()
        self.label_3.setText(_translate("Dialog","COM port selected: "+ self.listWidget.currentItem().text() , None))

    def get_device_name(self):
        return self.dev_name

    def get_device_type(self):
        return self.dev_type

    def get_COM(self):
        return self.listWidget.currentItem().text()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

