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
        email_message_box.setEnabled(True)
        email_message_box.resize(692, 687)
        email_message_box.setContextMenuPolicy(Qt.NoContextMenu)
        email_message_box.setAutoFillBackground(False)
        self.centralwidget = QWidget(email_message_box)
        self.centralwidget.setObjectName(u"centralwidget")
        self.send_message = QPushButton(self.centralwidget)
        self.send_message.setObjectName(u"send_message")
        self.send_message.setGeometry(QRect(540, 620, 151, 32))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.send_message.setFont(font)
        self.label_body_text = QLabel(self.centralwidget)
        self.label_body_text.setObjectName(u"label_body_text")
        self.label_body_text.setGeometry(QRect(10, 360, 181, 16))
        self.label_body_text.setFont(font)
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, 10, 371, 31))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setWeight(50)
        self.title.setFont(font1)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(270, 50, 191, 47))
        self.layoutWidget.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_email_From = QLabel(self.layoutWidget)
        self.label_email_From.setObjectName(u"label_email_From")
        self.label_email_From.setFont(font)
        self.label_email_From.setScaledContents(True)
        self.label_email_From.setIndent(0)

        self.verticalLayout_3.addWidget(self.label_email_From)

        self.email_From = QLineEdit(self.layoutWidget)
        self.email_From.setObjectName(u"email_From")
        self.email_From.setFont(font)
        self.email_From.setToolTipDuration(0)
        self.email_From.setMaxLength(32767)
        self.email_From.setEchoMode(QLineEdit.Normal)
        self.email_From.setReadOnly(False)

        self.verticalLayout_3.addWidget(self.email_From)

        self.Email_body_text = QPlainTextEdit(self.centralwidget)
        self.Email_body_text.setObjectName(u"Email_body_text")
        self.Email_body_text.setGeometry(QRect(10, 380, 671, 231))
        self.Email_body_text.setFont(font)
        self.label_email_title = QLabel(self.centralwidget)
        self.label_email_title.setObjectName(u"label_email_title")
        self.label_email_title.setGeometry(QRect(10, 180, 181, 16))
        self.label_email_title.setFont(font)
        self.Email_title = QPlainTextEdit(self.centralwidget)
        self.Email_title.setObjectName(u"Email_title")
        self.Email_title.setGeometry(QRect(10, 200, 671, 31))
        self.Email_title.setFont(font)
        self.WelcomingMessage = QFrame(self.centralwidget)
        self.WelcomingMessage.setObjectName(u"WelcomingMessage")
        self.WelcomingMessage.setGeometry(QRect(10, 240, 671, 111))
        self.WelcomingMessage.setFrameShape(QFrame.Box)
        self.WelcomingMessage.setFrameShadow(QFrame.Sunken)
        self.widget = QWidget(self.WelcomingMessage)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 40, 531, 40))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_welcoming_tip_2 = QLabel(self.widget)
        self.label_welcoming_tip_2.setObjectName(u"label_welcoming_tip_2")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_welcoming_tip_2.setFont(font2)
        self.label_welcoming_tip_2.setScaledContents(True)
        self.label_welcoming_tip_2.setIndent(0)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_welcoming_tip_2)

        self.label_welcoming_tip_3 = QLabel(self.widget)
        self.label_welcoming_tip_3.setObjectName(u"label_welcoming_tip_3")
        font3 = QFont()
        font3.setFamily(u"Helvetica")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_welcoming_tip_3.setFont(font3)
        self.label_welcoming_tip_3.setFrameShadow(QFrame.Plain)
        self.label_welcoming_tip_3.setScaledContents(True)
        self.label_welcoming_tip_3.setIndent(0)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_welcoming_tip_3)

        self.label_welcoming_tip = QLabel(self.widget)
        self.label_welcoming_tip.setObjectName(u"label_welcoming_tip")
        self.label_welcoming_tip.setFont(font2)
        self.label_welcoming_tip.setLayoutDirection(Qt.LeftToRight)
        self.label_welcoming_tip.setScaledContents(True)
        self.label_welcoming_tip.setIndent(0)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_welcoming_tip)

        self.widget1 = QWidget(self.WelcomingMessage)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 10, 651, 27))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Welcoming_flag = QCheckBox(self.widget1)
        self.Welcoming_flag.setObjectName(u"Welcoming_flag")
        self.Welcoming_flag.setChecked(True)

        self.horizontalLayout.addWidget(self.Welcoming_flag)

        self.Email_welcoming = QTextEdit(self.widget1)
        self.Email_welcoming.setObjectName(u"Email_welcoming")
        self.Email_welcoming.setFont(font)
        self.Email_welcoming.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.Email_welcoming.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Email_welcoming.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout.addWidget(self.Email_welcoming)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 50, 127, 47))
        self.widget2.setFont(font)
        self.verticalLayout = QVBoxLayout(self.widget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_email_address = QLabel(self.widget2)
        self.label_email_address.setObjectName(u"label_email_address")
        self.label_email_address.setFont(font)
        self.label_email_address.setScaledContents(True)
        self.label_email_address.setIndent(0)

        self.verticalLayout.addWidget(self.label_email_address)

        self.email_address = QLineEdit(self.widget2)
        self.email_address.setObjectName(u"email_address")
        self.email_address.setFont(font)
        self.email_address.setMaxLength(32767)

        self.verticalLayout.addWidget(self.email_address)

        self.widget3 = QWidget(self.centralwidget)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(140, 50, 127, 47))
        self.widget3.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.widget3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_email_pass = QLabel(self.widget3)
        self.label_email_pass.setObjectName(u"label_email_pass")
        self.label_email_pass.setFont(font)
        self.label_email_pass.setScaledContents(True)
        self.label_email_pass.setIndent(0)

        self.verticalLayout_2.addWidget(self.label_email_pass)

        self.email_pass = QLineEdit(self.widget3)
        self.email_pass.setObjectName(u"email_pass")
        self.email_pass.setFont(font)
        self.email_pass.setToolTipDuration(0)
        self.email_pass.setMaxLength(32767)
        self.email_pass.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.email_pass)

        self.widget4 = QWidget(self.centralwidget)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(10, 110, 451, 48))
        self.widget4.setFont(font)
        self.gridLayout = QGridLayout(self.widget4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_spreadsheet = QLabel(self.widget4)
        self.label_spreadsheet.setObjectName(u"label_spreadsheet")
        self.label_spreadsheet.setFont(font)
        self.label_spreadsheet.setScaledContents(True)
        self.label_spreadsheet.setIndent(0)

        self.gridLayout.addWidget(self.label_spreadsheet, 0, 0, 1, 2)

        self.spreadsheet = QToolButton(self.widget4)
        self.spreadsheet.setObjectName(u"spreadsheet")
        self.spreadsheet.setFont(font)

        self.gridLayout.addWidget(self.spreadsheet, 1, 0, 1, 1)

        self.spreadsheet_address_viewer = QLineEdit(self.widget4)
        self.spreadsheet_address_viewer.setObjectName(u"spreadsheet_address_viewer")
        self.spreadsheet_address_viewer.setFont(font)
        self.spreadsheet_address_viewer.setContextMenuPolicy(Qt.PreventContextMenu)
        self.spreadsheet_address_viewer.setAutoFillBackground(False)
        self.spreadsheet_address_viewer.setReadOnly(True)

        self.gridLayout.addWidget(self.spreadsheet_address_viewer, 1, 1, 1, 1)

        email_message_box.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(email_message_box)
        self.statusbar.setObjectName(u"statusbar")
        email_message_box.setStatusBar(self.statusbar)

        self.retranslateUi(email_message_box)

        QMetaObject.connectSlotsByName(email_message_box)
    # setupUi

    def retranslateUi(self, email_message_box):
        email_message_box.setWindowTitle(QCoreApplication.translate("email_message_box", u"E-Mail Sender", None))
        self.send_message.setText(QCoreApplication.translate("email_message_box", u"Send e-mails", None))
        self.label_body_text.setText(QCoreApplication.translate("email_message_box", u"Email body text:", None))
        self.title.setText(QCoreApplication.translate("email_message_box", u"The tool only works by using a Gmail account", None))
        self.label_email_From.setText(QCoreApplication.translate("email_message_box", u"Name to be shown", None))
#if QT_CONFIG(tooltip)
        self.email_From.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.email_From.setInputMask("")
        self.email_From.setText("")
        self.email_From.setPlaceholderText(QCoreApplication.translate("email_message_box", u"ex.: ABC Company", None))
        self.label_email_title.setText(QCoreApplication.translate("email_message_box", u"Email Title", None))
        self.label_welcoming_tip_2.setText(QCoreApplication.translate("email_message_box", u"Ex. Good Morning", None))
        self.label_welcoming_tip_3.setText(QCoreApplication.translate("email_message_box", u" Mary,", None))
        self.label_welcoming_tip.setText(QCoreApplication.translate("email_message_box", u"Will include the receiver's name from the XLSX file at the end of the line.", None))
        self.Welcoming_flag.setText(QCoreApplication.translate("email_message_box", u"Welcoming message?", None))
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
