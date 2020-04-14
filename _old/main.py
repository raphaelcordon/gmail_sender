# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_email_message_box(object):
    def setupUi(self, email_message_box):
        if not email_message_box.objectName():
            email_message_box.setObjectName(u"email_message_box")
        email_message_box.resize(602, 543)
        self.centralwidget = QWidget(email_message_box)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Email_body_text = QTextEdit(self.centralwidget)
        self.Email_body_text.setObjectName(u"Email_body_text")
        self.Email_body_text.setGeometry(QRect(10, 220, 581, 231))
        self.send_message = QPushButton(self.centralwidget)
        self.send_message.setObjectName(u"send_message")
        self.send_message.setGeometry(QRect(442, 460, 151, 32))
        self.label_body_text = QLabel(self.centralwidget)
        self.label_body_text.setObjectName(u"label_body_text")
        self.label_body_text.setGeometry(QRect(10, 200, 111, 16))
        self.label_welcoming = QLabel(self.centralwidget)
        self.label_welcoming.setObjectName(u"label_welcoming")
        self.label_welcoming.setGeometry(QRect(10, 110, 141, 21))
        self.label_welcoming.setScaledContents(True)
        self.label_welcoming.setIndent(0)
        self.welcoming_yes = QRadioButton(self.centralwidget)
        self.welcoming_yes.setObjectName(u"welcoming_yes")
        self.welcoming_yes.setGeometry(QRect(150, 110, 51, 20))
        self.welcoming_yes.setChecked(True)
        self.welcoming_no = QRadioButton(self.centralwidget)
        self.welcoming_no.setObjectName(u"welcoming_no")
        self.welcoming_no.setGeometry(QRect(200, 110, 51, 20))
        self.Email_welcoming = QTextEdit(self.centralwidget)
        self.Email_welcoming.setObjectName(u"Email_welcoming")
        self.Email_welcoming.setGeometry(QRect(10, 140, 581, 21))
        self.Email_welcoming.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_welcoming_tip = QLabel(self.centralwidget)
        self.label_welcoming_tip.setObjectName(u"label_welcoming_tip")
        self.label_welcoming_tip.setGeometry(QRect(10, 160, 581, 21))
        font = QFont()
        font.setPointSize(12)
        self.label_welcoming_tip.setFont(font)
        self.label_welcoming_tip.setScaledContents(True)
        self.label_welcoming_tip.setIndent(0)
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, 10, 371, 31))
        font1 = QFont()
        font1.setPointSize(18)
        self.title.setFont(font1)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 50, 127, 47))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_email_address = QLabel(self.widget)
        self.label_email_address.setObjectName(u"label_email_address")
        self.label_email_address.setScaledContents(True)
        self.label_email_address.setIndent(0)

        self.verticalLayout.addWidget(self.label_email_address)

        self.email_address = QLineEdit(self.widget)
        self.email_address.setObjectName(u"email_address")
        self.email_address.setMaxLength(32767)

        self.verticalLayout.addWidget(self.email_address)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(140, 50, 127, 47))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_email_pass = QLabel(self.widget1)
        self.label_email_pass.setObjectName(u"label_email_pass")
        self.label_email_pass.setScaledContents(True)
        self.label_email_pass.setIndent(0)

        self.verticalLayout_2.addWidget(self.label_email_pass)

        self.email_pass = QLineEdit(self.widget1)
        self.email_pass.setObjectName(u"email_pass")
        self.email_pass.setToolTipDuration(0)
        self.email_pass.setMaxLength(32767)
        self.email_pass.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.email_pass)

        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(370, 50, 115, 48))
        self.gridLayout = QGridLayout(self.widget2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_spreadsheet = QLabel(self.widget2)
        self.label_spreadsheet.setObjectName(u"label_spreadsheet")
        self.label_spreadsheet.setScaledContents(True)
        self.label_spreadsheet.setIndent(0)

        self.gridLayout.addWidget(self.label_spreadsheet, 0, 0, 1, 1)

        self.spreadsheet = QToolButton(self.widget2)
        self.spreadsheet.setObjectName(u"spreadsheet")

        self.gridLayout.addWidget(self.spreadsheet, 1, 0, 1, 1)

        email_message_box.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(email_message_box)
        self.statusbar.setObjectName(u"statusbar")
        email_message_box.setStatusBar(self.statusbar)

        self.retranslateUi(email_message_box)

        QMetaObject.connectSlotsByName(email_message_box)
    # setupUi

    def retranslateUi(self, email_message_box):
        email_message_box.setWindowTitle(QCoreApplication.translate("email_message_box", u"MainWindow", None))
        self.send_message.setText(QCoreApplication.translate("email_message_box", u"Send e-mails", None))
        self.label_body_text.setText(QCoreApplication.translate("email_message_box", u"Email body text:", None))
        self.label_welcoming.setText(QCoreApplication.translate("email_message_box", u"Welcoming message?", None))
        self.welcoming_yes.setText(QCoreApplication.translate("email_message_box", u"Yes", None))
        self.welcoming_no.setText(QCoreApplication.translate("email_message_box", u"No", None))
        self.label_welcoming_tip.setText(QCoreApplication.translate("email_message_box", u"Will include the receiver's name from the XLSX file. Ex. \"Good morning Mary,\"", None))
        self.title.setText(QCoreApplication.translate("email_message_box", u"The tool only works by using a Gmail account", None))
        self.label_email_address.setText(QCoreApplication.translate("email_message_box", u"Your Gmail", None))
#if QT_CONFIG(tooltip)
        self.email_address.setToolTip(QCoreApplication.translate("email_message_box", u"  ...@gmail.com", None))
#endif // QT_CONFIG(tooltip)
        self.email_address.setInputMask("")
        self.email_address.setText("")
        self.email_address.setPlaceholderText(QCoreApplication.translate("email_message_box", u"  ...@gmail.com", None))
        self.label_email_pass.setText(QCoreApplication.translate("email_message_box", u"Pass", None))
#if QT_CONFIG(tooltip)
        self.email_pass.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.email_pass.setInputMask("")
        self.email_pass.setText("")
        self.email_pass.setPlaceholderText("")
        self.label_spreadsheet.setText(QCoreApplication.translate("email_message_box", u"Excel Spreadsheet", None))
        self.spreadsheet.setText(QCoreApplication.translate("email_message_box", u"...", None))
    # retranslateUi

