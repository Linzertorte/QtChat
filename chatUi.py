# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\chat.ui'
#
# Created: Sun May 18 23:50:08 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(512, 382)
        Form.setMinimumSize(QtCore.QSize(512, 382))
        Form.setMaximumSize(QtCore.QSize(512, 382))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 20, 451, 351))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chatEdit = QtGui.QTextEdit(self.widget)
        self.chatEdit.setObjectName("chatEdit")
        self.verticalLayout.addWidget(self.chatEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.msgEdit = QtGui.QLineEdit(self.widget)
        self.msgEdit.setObjectName("msgEdit")
        self.horizontalLayout.addWidget(self.msgEdit)
        self.sendButton = QtGui.QPushButton(self.widget)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout.addWidget(self.sendButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "ChatRoom", None, QtGui.QApplication.UnicodeUTF8))
        self.sendButton.setText(QtGui.QApplication.translate("Form", "Send", None, QtGui.QApplication.UnicodeUTF8))

