# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

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

class Ui_Form(QtGui.QWidget):
    # class variables
    up_sd = ""
    up_dd = ""
    up_bat = ""
    pe_sd = ""
    pe_dd = ""
    pe_bat = ""

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 305)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Sciencestic Knowledgebase/logos/trans_bmp_logo.bmp")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ui2py_btn = QtGui.QPushButton(Form)
        self.ui2py_btn.setObjectName(_fromUtf8("ui2py_btn"))
        self.gridLayout.addWidget(self.ui2py_btn, 5, 0, 1, 1)
        self.py2exe_btn = QtGui.QPushButton(Form)
        self.py2exe_btn.setObjectName(_fromUtf8("py2exe_btn"))
        self.gridLayout.addWidget(self.py2exe_btn, 12, 0, 1, 1)
        self.up_run_btn = QtGui.QPushButton(Form)
        self.up_run_btn.setEnabled(False)
        self.up_run_btn.setObjectName(_fromUtf8("up_run_btn"))
        self.gridLayout.addWidget(self.up_run_btn, 5, 1, 1, 1)
        self.up_sd_line = QtGui.QLineEdit(Form)
        self.up_sd_line.setObjectName(_fromUtf8("up_sd_line"))
        self.gridLayout.addWidget(self.up_sd_line, 2, 0, 1, 2)
        self.up_dd_line = QtGui.QLineEdit(Form)
        self.up_dd_line.setObjectName(_fromUtf8("up_dd_line"))
        self.gridLayout.addWidget(self.up_dd_line, 4, 0, 1, 2)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 2)
        self.label = QtGui.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.pe_run_btn = QtGui.QPushButton(Form)
        self.pe_run_btn.setEnabled(False)
        self.pe_run_btn.setObjectName(_fromUtf8("pe_run_btn"))
        self.gridLayout.addWidget(self.pe_run_btn, 12, 1, 1, 1)
        self.pe_dd_line = QtGui.QLineEdit(Form)
        self.pe_dd_line.setEnabled(False)
        self.pe_dd_line.setObjectName(_fromUtf8("pe_dd_line"))
        self.gridLayout.addWidget(self.pe_dd_line, 11, 0, 1, 2)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 2)
        self.pe_sd_line = QtGui.QLineEdit(Form)
        self.pe_sd_line.setObjectName(_fromUtf8("pe_sd_line"))
        self.gridLayout.addWidget(self.pe_sd_line, 9, 0, 1, 2)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 2)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 2)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 6, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "EasyConverter", None))
        self.ui2py_btn.setText(_translate("Form", "Create .bat", None))
        self.py2exe_btn.setText(_translate("Form", "Create .bat", None))
        self.up_run_btn.setText(_translate("Form", "Run", None))
        self.label_2.setText(_translate("Form", "Source directory (__.ui)", None))
        self.label_3.setText(_translate("Form", "Destination directory (__.py)", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">UI to PY</span></p></body></html>", None))
        self.pe_run_btn.setText(_translate("Form", "Run", None))
        self.label_6.setText(_translate("Form", "Destination directory (__.exe)", None))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">PY to EXE</span></p></body></html>", None))
        self.label_5.setText(_translate("Form", "Source directory (__.py)", None))

        self.ui2py_btn.clicked.connect(self.ui2py)
        self.py2exe_btn.clicked.connect(self.py2exe)
        self.up_run_btn.clicked.connect(self.upBatRun)
        self.pe_run_btn.clicked.connect(self.peBatRun)

    def getDataUP(self):
        self.up_sd = self.up_sd_line.text()
        self.up_dd = self.up_dd_line.text()

    def geyDataPE(self):
        self.pe_sd = self.pe_sd_line.text()
        self.pe_dd = self.pe_dd_line.text()

    def makeUPName(self):
        return self.up_sd[:2]+self.up_dd[:2]+".bat"

    def makePEName(self):
        return self.pe_sd[:2]+self.pe_dd[:2]+".bat"

    def ui2py(self):
        self.getDataUP() 
        self.up_run_btn.setEnabled(False)
        pyuic4_bat = open("pyuic4.bat", "w")
        pyuic4_bat.write("@python.exe -c\"import PyQt4.uic.pyuic\" %*")
        pyuic4_bat.close()

        up_bat = ".\pyuic4 -o "+self.up_dd+" "+self.up_sd
        up_file = open(self.makeUPName(), "w")
        up_file.write(up_bat)
        up_file.close()
        print(up_bat)
        self.up_run_btn.setEnabled(True)

    def py2exe(self):
        self.geyDataPE()
        self.pe_run_btn.setEnabled(False)
        pe_bat = "pyinstaller -F "+self.pe_sd+" -y"
        pe_file = open(self.makePEName(), "w")
        pe_file.write(pe_bat)
        pe_file.close()
        print(pe_bat)
        self.pe_run_btn.setEnabled(True)

    def upBatRun(self):
        import os
        os.system(self.makeUPName())

    def peBatRun(self):
        import os
        os.system(self.makePEName())
        self.pe_dd_line.setText("../dist/"+self.pe_sd[:-3]+".exe")


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())