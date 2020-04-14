from PySide2 import QtWidgets

from ui import main
from email_instructions import EmailInstructions


class MessageBox(main.Ui_email_message_box, QtWidgets.QMainWindow, QtWidgets.QMessageBox):
    def __init__(self):
        super(MessageBox, self).__init__()
        self.setupUi(self)
        self.send_message.clicked.connect(self.fill_form)
        self.spreadsheet.clicked.connect(self.select_xlsx)
        self.Welcoming_flag.clicked.connect(self.welcoming_flag)

    def fill_form(self):
        email_address = self.email_address.text()
        email_pass = self.email_pass.text()
        email_from = self.email_From.text()
        Email_title = self.Email_title.toPlainText()
        spreadsheet_address_viewer = self.spreadsheet_address_viewer.text()
        Email_body_text = self.Email_body_text.toPlainText()
        Welcoming_message = self.Email_welcoming.toPlainText()

        if any(v == '' for v in [email_address, email_pass, email_from, Email_title, spreadsheet_address_viewer]):
            self.show_popup()
        else:
            EmailInstructions(
                email_address, email_pass, email_from, spreadsheet_address_viewer,
                Email_body_text, Welcoming_message, Email_title
            )

    def select_xlsx(self):
        excel_patch, ext = QtWidgets.QFileDialog.getOpenFileName(self, 'Select the Excel file')
        self.spreadsheet_address_viewer.setText(excel_patch)

    def show_popup(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('Incomplete field')
        msg.setText('All the fields should be filled up')
        x = msg.exec_()

    def welcoming_flag(self):
        if self.Welcoming_flag.isChecked():
            self.Email_welcoming.setReadOnly(False)
        else:
            self.Email_welcoming.clear()
            self.Email_welcoming.setReadOnly(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MessageBox()
    qt_app.show()
    app.exec_()
