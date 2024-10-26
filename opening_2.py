from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import re
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import os
import sys

# کلاس صفحه لاگین (ورود)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(349, 357)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("f.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 103, 15);\n"
                                 "background-color: rgb(0, 0, 0);")
        MainWindow.setIconSize(QtCore.QSize(40, 40))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(299, 7, 61, 21))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(19, 20, 251, 151))
        self.label.setPixmap(QtGui.QPixmap("images.jpg"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(129, 270, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(208, 214, 90);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 227, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(135, 192, 80, 21))
        self.label_3.setStyleSheet("background-color: rgb(208, 214, 90);")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # اتصال دکمه تایید به تابع بررسی رمز
        self.pushButton.clicked.connect(self.check_password)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ورود"))
        self.label_2.setText(_translate("MainWindow", " فست فودی "))
        self.pushButton.setText(_translate("MainWindow", "تایید"))
        self.label_3.setText(_translate("MainWindow", "  رمز را وارد کنید:"))

    def check_password(self):
        entered_pin = self.lineEdit.text()
        correct_pin = "1"
        if entered_pin == correct_pin:
            self.show_message_box("رمز درست است! فایل باز می‌شود.")
            self.load_main_ui()
            MainWindow.close()  # بستن پنجره ورود بعد از ورود موفق
        else:
            self.show_message_box("رمز اشتباه است!")

    def show_message_box(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("نتیجه")
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def load_main_ui(self):
        self.window = Ui_Main3_A()  # باز کردن صفحه اصلی برنامه
        self.window.show()

class Ui_Main3_A(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Main3_A.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.create_toolbar()

        # متغیرهای جمع کل برای غذا و نوشیدنی
        self.total_food = 0
        self.total_drink = 0

        self.pushButton_6.clicked.connect(self.tayid)
        self.pushButton_6.clicked.connect(self.kol)
        self.pushButton_2.clicked.connect(self.kol_2)

    def tayid(self):
        selected_text_1 = self.comboBox.currentText()
        if selected_text_1.strip():
            current_text_1 = self.label_6.text()
            new_text_1 = current_text_1 + "\n" + selected_text_1 + "\n"
            self.label_6.setText(new_text_1)
        
        selected_text_2 = self.comboBox_2.currentText()
        if selected_text_2.strip():
            current_text_2 = self.label_6.text()
            new_text_2 = current_text_2 + "\n" + selected_text_2 + "\n"
            self.label_6.setText(new_text_2)

    def kol(self):
        try:
            # بررسی ورودی برای تعداد غذا
            entered_text = self.tedad_Line_Edit.text().strip()
            if entered_text.isdigit():
                quantity_food = int(entered_text)
                price_food = int(self.lineEdit_3.text())
                total_food_price = quantity_food * price_food
                food_name = self.comboBox.currentText()
                food_text = f"{total_food_price}"
            else:
                food_text = "ورودی نادرست برای غذا"

            # بررسی ورودی برای تعداد نوشیدنی
            entered_text_2 = self.lineEdit_5.text().strip()
            if entered_text_2.isdigit():
                quantity_drink = int(entered_text_2)
                price_drink = int(self.lineEdit_4.text())
                total_drink_price = quantity_drink * price_drink
                drink_text = f"{total_drink_price}"
            else:
                drink_text = "ورودی نادرست برای نوشیدنی"

            # نمایش قیمت غذا و نوشیدنی به همراه نام آن‌ها با یک خط فاصله
            current_text = self.label_5.text()  # متن فعلی در لیبل
            final_text = f"{current_text}\n{food_text}\n\n{drink_text}\n"
            self.label_5.setText(final_text)

        except ValueError:
            self.label_5.setText("خطا در ورودی")

    def kol_2(self):
        # دریافت متن `label_5`
        label_text = self.label_5.text()

        # استخراج تمامی اعداد از متن
        numbers = re.findall(r'\d+', label_text)

        # تبدیل اعداد استخراج شده به عدد صحیح و جمع کردن آن‌ها
        total_sum = sum(int(num) for num in numbers)

        # نمایش نتیجه در `label_4`
        self.label_4.setText(str(total_sum))


    def create_toolbar(self):
        toolbar = self.addToolBar("ابزارها")

        # قرار دادن گزینه‌های ماشین حساب و یادداشت
        toolbar.setLayoutDirection(Qt.RightToLeft)

        # افزودن دکمه ماشین حساب
        calculator_action = QtWidgets.QAction("ماشین حساب", self)
        calculator_action.setIcon(QtGui.QIcon("D:/Desktop/python/Icons/icons/calculator-gray.png"))
        calculator_action.triggered.connect(self.open_calculator)
        toolbar.addAction(calculator_action)

        # افزودن دکمه یادداشت
        note_action = QtWidgets.QAction("یادداشت", self)
        note_action.setIcon(QtGui.QIcon("D:/Desktop/python/Icons/icons/notebook-medium.png"))
        note_action.triggered.connect(self.open_note)
        toolbar.addAction(note_action)

        # افزودن دکمه ساعت
        clock_action = QtWidgets.QAction("ساعت", self)
        clock_action.setIcon(QtGui.QIcon("D:/Desktop/python/Icons/icons/clock.png"))
        clock_action.triggered.connect(self.open_clock)
        toolbar.addAction(clock_action)

        # افزودن دکمه جستجو
        search_action = QtWidgets.QAction("جستوجو", self)
        search_action.setIcon(QtGui.QIcon("D:/Desktop/python/Icons/icons/occluder.png"))
        search_action.triggered.connect(self.open_search)
        toolbar.addAction(search_action)

        # افزودن دکمه تنظیمات
        setting_action = QtWidgets.QAction("تنظیمات", self)
        setting_action.setIcon(QtGui.QIcon("D:/Desktop/python/Icons/icons/clipboard-task.png"))
        setting_action.triggered.connect(self.open_setting)
        toolbar.addAction(setting_action)

    def open_calculator(self):
        if sys.platform == "win32":
            os.system("calc")
        elif sys.platform == "linux":
            os.system("gnome-calculator")
        elif sys.platform == "darwin":
            os.system("open -a Calculator")

    def open_note(self):
        if sys.platform == "win32":
            os.system("notepad")
        elif sys.platform == "linux":
            os.system("gedit")
        elif sys.platform == "darwin":
            os.system("open -a TextEdit")

    def open_clock(self):
        from clock import root

    def open_search(self):
        from search import root

    def open_setting(self):
        pass

# اجرای برنامه
if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
