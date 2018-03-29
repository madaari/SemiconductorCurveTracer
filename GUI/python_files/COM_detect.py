# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'COM_detect.ui'
#
# Created: Fri Mar 30 01:49:38 2018
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
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 255)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 351, 61))
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 90, 311, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 120, 51, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(235, 120, 151, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 60, 181, 21))
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
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 160, 201, 31))
        self.progressBar.setProperty("value", 8)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(210, 150, 171, 51))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(237, 210, 131, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(0, 220, 141, 31))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("../../../development/ACT_ZIF_GUI/cedt.jpg")))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Make sure the device is connected and then press Detect COM Port", None))
        self.pushButton.setText(_translate("Dialog", "Detect COM Port", None))
        self.label_2.setText(_translate("Dialog", "Status:", None))
        self.label_3.setText(_translate("Dialog", "COM Port undetected", None))
        self.pushButton_2.setText(_translate("Dialog", "Proceed", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

