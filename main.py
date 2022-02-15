import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent
from PyQt5.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient
from PyQt5.QtWidgets import *

from ui_splash_screen import Ui_SplashScreen
from ui_main import Ui_MainWindow
from ui_functions import *

counter = 0

class Jacobi(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.main()
        self.ui.comboBox.addItem('2x2', 2)
        self.ui.comboBox.addItem('3x3', 3)
        self.ui.comboBox.addItem('4x4', 4)
        self.orders()
        self.validators()

    def main(self):
        self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 135, True))

        self.ui.comboBox.currentIndexChanged.connect(self.orders)

        #icons
        self.ui.btn_toggle.setIcon(QIcon('menu.png'))
        self.ui.btn_toggle.setIconSize(QSize(17, 17))
        self.ui.btn_page_1.setIcon(QIcon('home.png'))
        self.ui.btn_page_1.setIconSize(QSize(10, 10))
        self.ui.btn_page_2.setIcon(QIcon('about_icon.png'))
        self.ui.btn_page_2.setIconSize(QSize(10, 10))
        self.ui.btn_page_3.setIcon(QIcon('author_icon.png'))
        self.ui.btn_page_3.setIconSize(QSize(10, 10))
        self.ui.btn_page_4.setIcon(QIcon('settings.png'))
        self.ui.btn_page_4.setIconSize(QSize(20, 20))

        #images_eng
        self.ui.label.setPixmap(QPixmap('About.png'))
        self.ui.label_6.setPixmap(QPixmap('Author.png'))
        self.ui.label_8.setPixmap(QPixmap('page_settings.png'))
        self.ui.label_2.setFont(QtGui.QFont("Century Gothic", 7))
        self.ui.label_2.setText(
            '<a style="color: #00cec9;" href="https://en.wikipedia.org/wiki/Jacobi_method"> Links: Wikipedia </a>')
        self.ui.label_2.setOpenExternalLinks(True)

        #color_blue
        self.ui.btn_page_1.setStyleSheet('QPushButton {color: rgb(255, 255, 255); background-color: rgb(17,17,17); border: 0px solid;} QPushButton:hover {background-color:#00cec9}')
        self.ui.btn_page_2.setStyleSheet('QPushButton {color: rgb(255, 255, 255); background-color: rgb(17,17,17); border: 0px solid;} QPushButton:hover {background-color:#00cec9}')
        self.ui.btn_page_3.setStyleSheet('QPushButton {color: rgb(255, 255, 255); background-color: rgb(17,17,17); border: 0px solid;} QPushButton:hover {background-color:#00cec9}')
        self.ui.btn_toggle.setStyleSheet('background-color: rgb(17,17,17);border: 0px solid;color: #00cec9;')
        self.ui.input_iterations.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.output.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.btn_calculate.setStyleSheet('QPushButton {color: rgb(255, 255, 255); background-color: rgb(17,17,17); border: 0px solid;} QPushButton:hover {background-color:#00cec9}')
        self.ui.btn_page_4.setStyleSheet('QPushButton {color: rgb(255, 255, 255); background-color: rgb(17,17,17); border: 0px solid;} QPushButton:hover {background-color:#00cec9}')
        self.ui.btn_page_5.setStyleSheet('QPushButton {color: rgb(255, 255, 255); background-color: rgb(17,17,17); border: 0px solid;} QPushButton:hover {background-color:#00cec9}')
        self.ui.btn_page_6.setStyleSheet('QPushButton {color: rgb(255, 255, 255); background-color: rgb(17,17,17); border: 0px solid;} QPushButton:hover {background-color:#00cec9}')
        self.ui.btn_page_9.setStyleSheet('QPushButton {color: rgb(255, 255, 255); background-color: rgb(17,17,17); border: 0px solid;} QPushButton:hover {background-color:#00cec9}')

        self.ui.comboBox.setStyleSheet('color: rgb(255, 255, 255); background-color: rgb(17, 17, 17); border: 1px solid #00cec9;')
        self.ui.el_2x2_1.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_2x2_2.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_2x2_3.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_2x2_4.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_2x2_5.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_2x2_6.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_3x3_1.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_3x3_2.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_3x3_3.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_3x3_4.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_3x3_5.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_3x3_6.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_3x3_7.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_3x3_8.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_3x3_9.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_3x3_10.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_3x3_11.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_3x3_12.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_1.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_2.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_3.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_4.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_5.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_6.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_7.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_8.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_9.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_10.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_11.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_12.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_13.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_14.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_15.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_16.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_17.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_18.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_19.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')
        self.ui.el_4x4_20.setStyleSheet('border: 1px solid #00cec9; color:  rgb(240,240,240);')






        #text_eng
        self.ui.input_iterations.setPlaceholderText('Enter iterations:')
        self.ui.output.setPlaceholderText('Results')

        self.ui.btn_page_6.clicked.connect(self.rus)
        self.ui.btn_page_5.clicked.connect(self.eng)
        self.ui.btn_page_8.clicked.connect(self.orange)
        self.ui.btn_page_7.clicked.connect(self.main)

        #link_eng
        self.ui.label_2.setFont(QtGui.QFont("Century Gothic", 7))
        self.ui.label_2.setText('<a style="color: rgb(20, 169, 222);" href="https://en.wikipedia.org/wiki/Jacobi_method"> Links: Wikipedia </a>')
        self.ui.label_2.setOpenExternalLinks(True)

        #link_rus
        self.ui.label_10.setFont(QtGui.QFont("Century Gothic", 7))
        self.ui.label_10.setText( '<a style="color: rgb(20, 169, 222);" href="https://en.wikipedia.org/wiki/Jacobi_method"> Ссылки: Википедия </a>')
        self.ui.label_10.setOpenExternalLinks(True)

        self.ui.btn_page_1.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_1))
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_3))
        self.ui.btn_page_4.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_sttngs))

        self.show()

    def validators(self):
        #self.stu_id_regx = QRegExp('^[0-9]{12}$')
        #stu_id_validator = QRegExpValidator(stu_id_regx, self.ui.el_2x2_5)
        self.ui.el_2x2_1.setValidator(QtGui.QIntValidator())
        self.ui.el_2x2_2.setValidator(QtGui.QIntValidator())
        self.ui.el_2x2_3.setValidator(QtGui.QIntValidator())
        self.ui.el_2x2_4.setValidator(QtGui.QIntValidator())
        self.ui.el_2x2_5.setValidator(QtGui.QIntValidator())
        self.ui.el_2x2_6.setValidator(QtGui.QIntValidator())
        self.ui.el_3x3_1.setValidator(QtGui.QIntValidator())
        self.ui.el_3x3_2.setValidator(QtGui.QIntValidator())
        self.ui.el_3x3_3.setValidator(QtGui.QIntValidator())
        self.ui.el_3x3_4.setValidator(QtGui.QIntValidator())
        self.ui.el_3x3_5.setValidator(QtGui.QIntValidator())
        self.ui.el_3x3_6.setValidator(QtGui.QIntValidator())
        self.ui.el_3x3_7.setValidator(QtGui.QIntValidator())
        self.ui.el_3x3_8.setValidator(QtGui.QIntValidator())
        self.ui.el_3x3_9.setValidator(QtGui.QIntValidator())
        self.ui.el_3x3_10.setValidator(QtGui.QIntValidator())
        self.ui.el_3x3_11.setValidator(QtGui.QIntValidator())
        self.ui.el_3x3_12.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_1.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_2.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_3.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_4.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_5.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_6.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_7.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_8.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_9.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_10.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_11.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_12.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_13.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_14.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_15.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_16.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_17.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_20.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_19.setValidator(QtGui.QIntValidator())
        self.ui.el_4x4_18.setValidator(QtGui.QIntValidator())

    def rus(self):
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_1))
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_2_rus))
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_3_rus))

        self.ui.input_iterations.setPlaceholderText('Введите итерации')
        self.ui.output.setPlaceholderText('Результат')

        self.ui.label_3.setText('Порядок:')
        self.ui.label_4.setText('Итерации:')
        self.ui.label_5.setText('Матрица А')
        self.ui.label_7.setText('Вектор В')
        self.ui.btn_calculate.setText('ПОСЧИТАТЬ')
        self.ui.btn_page_1.setText('Главная')
        self.ui.btn_page_2.setText('Проект')
        self.ui.btn_page_3.setText('Автор')
        self.ui.btn_page_5.setText('Английский')
        self.ui.btn_page_6.setText('Русский')
        self.ui.btn_page_7.setText('Синяя')
        self.ui.btn_page_8.setText('Оранжевая')
        self.ui.label_11.setText('НАСТРОЙКИ')
        self.ui.label_12.setText('Язык')
        self.ui.label_13.setText('Цвет темы')

    def orders(self):
        order = self.ui.comboBox.currentData()
        if order == 2:
            self.ui.pages_spins.setCurrentWidget(self.ui.page_2x2)
        if order == 3:
            self.ui.pages_spins.setCurrentWidget(self.ui.page_3x3)
        if order == 4:
            self.ui.pages_spins.setCurrentWidget(self.ui.page_4x4)

    def eng(self):
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_1))
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_3))

        #text_eng
        self.ui.input_iterations.setPlaceholderText('Enter iterations:')
        self.ui.output.setPlaceholderText('Results')

        self.ui.label_3.setText('Order:')
        self.ui.label_4.setText('Iterations:')
        self.ui.label_5.setText('Matrix A:')
        self.ui.label_7.setText('Vector B:')
        self.ui.btn_calculate.setText('CALCULATE')
        self.ui.btn_page_1.setText('Main')
        self.ui.btn_page_2.setText('About')
        self.ui.btn_page_3.setText('Author')

        self.ui.btn_page_5.setText('Eng')
        self.ui.btn_page_6.setText('Rus')
        self.ui.btn_page_7.setText('Blue')
        self.ui.btn_page_8.setText('Orange')

        self.ui.label_11.setText('SETTINGS')
        self.ui.label_12.setText('Language')
        self.ui.label_13.setText('Theme color')

    def orange(self):
        #color_orange
        self.ui.btn_page_1.setStyleSheet('QPushButton {color: rgb(255, 255, 255); background-color: rgb(17,17,17); '
                                         'border: 0px solid;} QPushButton:hover {background-color:#f39c12}')
        self.ui.btn_page_2.setStyleSheet('QPushButton {color: rgb(255, 255, 255); background-color: rgb(17,17,17); '
                                         'border: 0px solid;} QPushButton:hover {background-color:#f39c12}')
        self.ui.btn_page_3.setStyleSheet('QPushButton {color: rgb(255, 255, 255); background-color: rgb(17,17,17); '
                                         'border: 0px solid;} QPushButton:hover {background-color:#f39c12}')
        self.ui.btn_toggle.setStyleSheet('background-color: rgb(17,17,17);border: 0px solid;color: #f39c12;')
        self.ui.input_iterations.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.output.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.btn_calculate.setStyleSheet('QPushButton {color: rgb(255, 255, 255); background-color: rgb(17,17,17); '
                                            'border: 0px solid;} QPushButton:hover {background-color:#f39c12}')
        self.ui.btn_page_4.setStyleSheet('QPushButton {color: rgb(255, 255, 255); background-color: rgb(17,17,17); '
                                         'border: 0px solid;} QPushButton:hover {background-color:#f39c12}')
        self.ui.btn_page_5.setStyleSheet('QPushButton {color: rgb(255, 255, 255); background-color: rgb(17,17,17); '
                                         'border: 0px solid;} QPushButton:hover {background-color:#f39c12}')
        self.ui.btn_page_6.setStyleSheet('QPushButton {color: rgb(255, 255, 255); background-color: rgb(17,17,17); '
                                         'border: 0px solid;} QPushButton:hover {background-color:#f39c12}')
        self.ui.btn_page_9.setStyleSheet('QPushButton {color: rgb(255, 255, 255); background-color: rgb(17,17,17); '
                                         'border: 0px solid;} QPushButton:hover {background-color:#f39c12}')

        self.ui.comboBox.setStyleSheet('color: rgb(255, 255, 255); background-color: rgb(17, 17, 17); border: 1px solid #f39c12;')
        self.ui.el_2x2_1.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_2x2_2.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_2x2_3.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_2x2_4.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_2x2_5.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_2x2_6.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_3x3_1.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_3x3_2.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_3x3_3.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_3x3_4.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_3x3_5.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_3x3_6.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_3x3_7.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_3x3_8.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_3x3_9.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_3x3_10.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_3x3_11.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_3x3_12.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_1.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_2.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_3.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_4.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_5.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_6.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_7.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_8.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_9.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_10.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_11.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_12.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_13.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_14.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_15.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_16.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_17.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_18.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_19.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')
        self.ui.el_4x4_20.setStyleSheet('border: 1px solid #f39c12; color:  rgb(240,240,240);')

        self.ui.btn_toggle.setIcon(QIcon('menu_orange.png'))
        self.ui.btn_toggle.setIconSize(QSize(17, 17))
        self.ui.btn_page_1.setIcon(QIcon('home_orange.png'))
        self.ui.btn_page_1.setIconSize(QSize(10, 10))
        self.ui.btn_page_2.setIcon(QIcon('about_icon_orange.png'))
        self.ui.btn_page_2.setIconSize(QSize(10, 10))
        self.ui.btn_page_3.setIcon(QIcon('author_icon_orange.png'))
        self.ui.btn_page_3.setIconSize(QSize(10, 10))
        self.ui.btn_page_4.setIcon(QIcon('settings_orange.png'))
        self.ui.btn_page_4.setIconSize(QSize(20, 20))

        #orange_image
        self.ui.label.setPixmap(QPixmap('about_orange.png'))
        self.ui.label_6.setPixmap(QPixmap('author_orange.png'))
        self.ui.label_8.setPixmap(QPixmap('settings_orange_2.png'))
        self.ui.label_2.setFont(QtGui.QFont("Century Gothic", 7))
        self.ui.label_2.setText('<a style="color: #f39c12;" href="https://en.wikipedia.org/wiki/Jacobi_method"> '
                                'Links: Wikipedia </a>')
        self.ui.label_2.setOpenExternalLinks(True)

    def init_UI(self):
        #interface_title
        self.setWindowTitle('Jacobi Method by A.Garmash')
        self.setWindowIcon(QIcon('matrix_img.png'))

        self.ui.btn_calculate.clicked.connect(self.connect_matrix)

    def connect_matrix(self):
        order = self.ui.comboBox.currentData()
        iterations = self.ui.input_iterations.text()
        if iterations == '':
            iterations = 1

        order, iterations = int(order), int(iterations)
        matrix_A, matrix_B, matrix_D_1, matrix_R, result_x, matrix_X_position_zero = [], [], [], [], [], []

        if order == 2:
            line_1, line_2 = [], []
            el_2x2_1, el_2x2_2 = float(self.ui.el_2x2_1.text()), float(self.ui.el_2x2_2.text())
            el_2x2_3, el_2x2_4 = float(self.ui.el_2x2_3.text()), float(self.ui.el_2x2_4.text())
            el_2x2_5, el_2x2_6 = float(self.ui.el_2x2_5.text()), float(self.ui.el_2x2_6.text())

            line_1.append(el_2x2_1), line_1.append(el_2x2_2), line_2.append(el_2x2_3), line_2.append(el_2x2_4)
            matrix_B.append(el_2x2_5), matrix_B.append(el_2x2_6)
            matrix_A.append(line_1), matrix_A.append(line_2)
            if el_2x2_5 == 0 or el_2x2_6 == 0:
                return self.ui.output.setPlainText('Enter valid values!')

        if order == 3:
            line_1, line_2, line_3 = [], [], []
            el_3x3_1, el_3x3_2, el_3x3_3 = float(self.ui.el_3x3_1.text()), float(self.ui.el_3x3_2.text()), float(self.ui.el_3x3_3.text())
            el_3x3_4, el_3x3_5, el_3x3_6 = float(self.ui.el_3x3_4.text()), float(self.ui.el_3x3_5.text()), float(self.ui.el_3x3_6.text())
            el_3x3_7, el_3x3_8, el_3x3_9 = float(self.ui.el_3x3_7.text()), float(self.ui.el_3x3_8.text()), float(self.ui.el_3x3_9.text())
            el_3x3_10, el_3x3_11, el_3x3_12 = float(self.ui.el_3x3_10.text()), float(self.ui.el_3x3_11.text()), float(self.ui.el_3x3_12.text())

            line_1.append(el_3x3_1), line_1.append(el_3x3_2), line_1.append(el_3x3_3)
            line_2.append(el_3x3_4), line_2.append(el_3x3_5), line_2.append(el_3x3_6)
            line_3.append(el_3x3_7), line_3.append(el_3x3_8), line_3.append(el_3x3_9)
            matrix_B.append(el_3x3_10), matrix_B.append(el_3x3_11), matrix_B.append(el_3x3_12)
            matrix_A.append(line_1), matrix_A.append(line_2), matrix_A.append(line_3)
            if el_3x3_10 == 0 or el_3x3_11 == 0 or el_3x3_12 == 0:
                return self.ui.output.setPlainText('Enter valid value!')

        if order == 4:
            line_1, line_2, line_3, line_4 = [], [], [], []
            el_4x4_1, el_4x4_2, el_4x4_3, el_4x4_4 = float(self.ui.el_4x4_1.text()), float(self.ui.el_4x4_2.text()), float(
                self.ui.el_4x4_3.text()), float(self.ui.el_4x4_4.text())
            el_4x4_5, el_4x4_6, el_4x4_7, el_4x4_8 = float(self.ui.el_4x4_5.text()), float(self.ui.el_4x4_6.text()), float(
                self.ui.el_4x4_7.text()), float(self.ui.el_4x4_8.text())
            el_4x4_9, el_4x4_10, el_4x4_11, el_4x4_12 = float(self.ui.el_4x4_9.text()), float(self.ui.el_4x4_10.text()), float(
                self.ui.el_4x4_11.text()), float(self.ui.el_4x4_12.text())
            el_4x4_13, el_4x4_14, el_4x4_15, el_4x4_16 = float(self.ui.el_4x4_13.text()), float(self.ui.el_4x4_14.text()), float(
                self.ui.el_4x4_15.text()), float(self.ui.el_4x4_16.text())
            el_4x4_17, el_4x4_18, el_4x4_19, el_4x4_20 = float(self.ui.el_4x4_17.text()), float(self.ui.el_4x4_18.text()), float(
                self.ui.el_4x4_19.text()), float(self.ui.el_4x4_20.text())

            line_1.append(el_4x4_1), line_1.append(el_4x4_2), line_1.append(el_4x4_3), line_1.append(el_4x4_4)
            line_2.append(el_4x4_5), line_2.append(el_4x4_6), line_2.append(el_4x4_7), line_2.append(el_4x4_8)
            line_3.append(el_4x4_9), line_3.append(el_4x4_10), line_3.append(el_4x4_11), line_3.append(el_4x4_12)
            line_4.append(el_4x4_13), line_4.append(el_4x4_14), line_4.append(el_4x4_15), line_4.append(el_4x4_16)
            matrix_B.append(el_4x4_17), matrix_B.append(el_4x4_18), matrix_B.append(el_4x4_19), matrix_B.append(el_4x4_20)
            matrix_A.append(line_1), matrix_A.append(line_2), matrix_A.append(line_3), matrix_A.append(line_4)
            if el_4x4_17 == 0 or el_4x4_18 == 0 or el_4x4_19 == 0 or el_4x4_20 == 0:
                return self.ui.output.setPlainText('Enter valid value!')


        for i in range(order):
            matrix_X_position_zero.append(matrix_A[i][i] / matrix_B[i])

        for j in range(order):
            e = []
            for i in range(order):
                if i == j:
                    e.append(1 / matrix_A[j][i])
                else:
                    e.append(0)
            matrix_D_1.append(e)

        for i in range(order):
            w = []
            for j in range(order):
                if i == j:
                    w.append(0)
                else:
                    w.append(matrix_A[i][j])
            matrix_R.append(w)

        matrix_T, matrix_C = [], []

        for i in range(order):
            z = []
            for j in range(order):
                z.append(0)
            matrix_T.append(z)

        for i in range(order):
            for j in range(order):
                for k in range(order):
                    matrix_T[i][j] += (-1) * (matrix_D_1[i][k] * matrix_R[k][j])

        for i in range(order):
            x = 0
            for k in range(order):
                x += matrix_D_1[i][k] * matrix_B[k]
            matrix_C.append(x)

        temp_T_X = []

        for i in range(iterations):
            for j in range(order):
                x = 0
                for k in range(order):
                    x += matrix_T[j][k] * matrix_X_position_zero[k]
                temp_T_X.append(x)
            matrix_X_position_zero.clear()
            result_x.clear()
            for l in range(order):
                result_x.append(temp_T_X[l] + matrix_C[l])
                matrix_X_position_zero.append(temp_T_X[l] + matrix_C[l])
            temp_T_X.clear()

            result = ''
            for i in range(order):
                result += 'x(' + str(i + 1) + ') = '
                result += str(round(result_x[i], 2))
                result += ', ε = '

                result += str(abs(round((abs(result_x[i]) - abs(round(result_x[i]))), 4)))
                result += '\n'


            f = open("result.txt", "w+", encoding='utf-8')
            f.write(result)
            f.close()

            self.ui.output.setPlainText(str(result))


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        self.timer.start(35)

        self.show()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)

        if counter > 100:
            self.timer.stop()
            self.main = Jacobi()
            self.main.show()
            self.close()

        counter += 2


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
