from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        MainWindow.setMaximumSize(QtCore.QSize(300, 400))
        MainWindow.setStyleSheet("background-color: rgb(26, 26, 26);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(23, 23, 23)")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.top_bar.setStyleSheet("background-color: rgb(17, 17, 17);")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.top_bar)
        self.frame_toggle.setEnabled(True)
        self.frame_toggle.setMaximumSize(QtCore.QSize(45, 30))
        self.frame_toggle.setStyleSheet("background-color: rgb(17, 17, 17);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_toggle)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_toggle.setFont(font)
        self.btn_toggle.setStyleSheet("background-color: rgb(17, 17, 17);\n"
"border: 0px solid;\n"
"color: rgb(241, 241, 241);")
        self.btn_toggle.setText("")
        self.btn_toggle.setObjectName("btn_toggle")
        self.horizontalLayout_3.addWidget(self.btn_toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.top_bar)
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.title = QtWidgets.QLabel(self.frame_top)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(239, 239, 239);")
        self.title.setObjectName("title")
        self.horizontalLayout_4.addWidget(self.title)
        self.horizontalLayout.addWidget(self.frame_top, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setMinimumSize(QtCore.QSize(300, 0))
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.content)
        self.frame_left_menu.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(17, 17, 17);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_page_1 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_1.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn_page_1.setFont(font)
        self.btn_page_1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(17, 17, 17);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#00cec9\n"
"}\n"
"")
        self.btn_page_1.setObjectName("btn_page_1")
        self.verticalLayout_4.addWidget(self.btn_page_1)
        self.btn_page_2 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn_page_2.setFont(font)
        self.btn_page_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(17, 17, 17);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#00cec9\n"
"}\n"
"")
        self.btn_page_2.setObjectName("btn_page_2")
        self.verticalLayout_4.addWidget(self.btn_page_2)
        self.btn_page_3 = QtWidgets.QPushButton(self.frame_top_menus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_page_3.sizePolicy().hasHeightForWidth())
        self.btn_page_3.setSizePolicy(sizePolicy)
        self.btn_page_3.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn_page_3.setFont(font)
        self.btn_page_3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(17, 17, 17);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#00cec9\n"
"}\n"
"")
        self.btn_page_3.setObjectName("btn_page_3")
        self.verticalLayout_4.addWidget(self.btn_page_3)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.btn_page_4 = QtWidgets.QPushButton(self.frame_left_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_page_4.sizePolicy().hasHeightForWidth())
        self.btn_page_4.setSizePolicy(sizePolicy)
        self.btn_page_4.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_page_4.setFont(font)
        self.btn_page_4.setStyleSheet("QPushButton {\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#00cec9\n"
"}\n"
"")
        self.btn_page_4.setText("")
        self.btn_page_4.setObjectName("btn_page_4")
        self.verticalLayout_3.addWidget(self.btn_page_4)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pages_widget = QtWidgets.QStackedWidget(self.frame_pages)
        self.pages_widget.setObjectName("pages_widget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.input_iterations = QtWidgets.QLineEdit(self.page_1)
        self.input_iterations.setGeometry(QtCore.QRect(130, 30, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.input_iterations.setFont(font)
        self.input_iterations.setAutoFillBackground(False)
        self.input_iterations.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.input_iterations.setAlignment(QtCore.Qt.AlignCenter)
        self.input_iterations.setObjectName("input_iterations")
        self.output = QtWidgets.QPlainTextEdit(self.page_1)
        self.output.setGeometry(QtCore.QRect(20, 220, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setBold(False)
        font.setWeight(50)
        self.output.setFont(font)
        self.output.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.output.setPlainText("")
        self.output.setObjectName("output")
        self.label_3 = QtWidgets.QLabel(self.page_1)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(231, 231, 231);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_1)
        self.label_4.setGeometry(QtCore.QRect(130, 10, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(231, 231, 231);")
        self.label_4.setObjectName("label_4")
        self.btn_calculate = QtWidgets.QPushButton(self.page_1)
        self.btn_calculate.setGeometry(QtCore.QRect(20, 300, 201, 41))
        self.btn_calculate.setAutoFillBackground(False)
        self.btn_calculate.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(17, 17, 17);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #00cec9\n"
"}\n"
"")
        self.btn_calculate.setObjectName("btn_calculate")
        self.label_9 = QtWidgets.QLabel(self.page_1)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 251, 371))
        self.label_9.setMinimumSize(QtCore.QSize(251, 371))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("back_theme.png"))
        self.label_9.setObjectName("label_9")
        self.comboBox = QtWidgets.QComboBox(self.page_1)
        self.comboBox.setGeometry(QtCore.QRect(20, 30, 61, 22))
        self.comboBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(17, 17, 17);\n"
"border: 1px solid #00cec9;\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.pages_spins = QtWidgets.QStackedWidget(self.page_1)
        self.pages_spins.setGeometry(QtCore.QRect(20, 60, 201, 151))
        self.pages_spins.setObjectName("pages_spins")
        self.page_2x2 = QtWidgets.QWidget()
        self.page_2x2.setObjectName("page_2x2")
        self.el_2x2_1 = QtWidgets.QLineEdit(self.page_2x2)
        self.el_2x2_1.setGeometry(QtCore.QRect(0, 40, 31, 21))
        self.el_2x2_1.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_2x2_1.setObjectName("el_2x2_1")
        self.el_2x2_2 = QtWidgets.QLineEdit(self.page_2x2)
        self.el_2x2_2.setGeometry(QtCore.QRect(60, 40, 31, 21))
        self.el_2x2_2.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_2x2_2.setObjectName("el_2x2_2")
        self.el_2x2_3 = QtWidgets.QLineEdit(self.page_2x2)
        self.el_2x2_3.setGeometry(QtCore.QRect(0, 90, 31, 21))
        self.el_2x2_3.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_2x2_3.setObjectName("el_2x2_3")
        self.el_2x2_4 = QtWidgets.QLineEdit(self.page_2x2)
        self.el_2x2_4.setGeometry(QtCore.QRect(60, 90, 31, 21))
        self.el_2x2_4.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_2x2_4.setObjectName("el_2x2_4")
        self.el_2x2_5 = QtWidgets.QLineEdit(self.page_2x2)
        self.el_2x2_5.setGeometry(QtCore.QRect(160, 40, 31, 20))
        self.el_2x2_5.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_2x2_5.setObjectName("el_2x2_5")
        self.el_2x2_6 = QtWidgets.QLineEdit(self.page_2x2)
        self.el_2x2_6.setGeometry(QtCore.QRect(160, 90, 31, 21))
        self.el_2x2_6.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_2x2_6.setObjectName("el_2x2_6")
        self.pages_spins.addWidget(self.page_2x2)
        self.page_3x3 = QtWidgets.QWidget()
        self.page_3x3.setObjectName("page_3x3")
        self.el_3x3_1 = QtWidgets.QLineEdit(self.page_3x3)
        self.el_3x3_1.setGeometry(QtCore.QRect(0, 30, 31, 21))
        self.el_3x3_1.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_3x3_1.setObjectName("el_3x3_1")
        self.el_3x3_2 = QtWidgets.QLineEdit(self.page_3x3)
        self.el_3x3_2.setGeometry(QtCore.QRect(40, 30, 31, 21))
        self.el_3x3_2.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_3x3_2.setObjectName("el_3x3_2")
        self.el_3x3_3 = QtWidgets.QLineEdit(self.page_3x3)
        self.el_3x3_3.setGeometry(QtCore.QRect(80, 30, 31, 21))
        self.el_3x3_3.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_3x3_3.setObjectName("el_3x3_3")
        self.el_3x3_4 = QtWidgets.QLineEdit(self.page_3x3)
        self.el_3x3_4.setGeometry(QtCore.QRect(0, 70, 31, 21))
        self.el_3x3_4.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_3x3_4.setObjectName("el_3x3_4")
        self.el_3x3_5 = QtWidgets.QLineEdit(self.page_3x3)
        self.el_3x3_5.setGeometry(QtCore.QRect(40, 70, 31, 21))
        self.el_3x3_5.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_3x3_5.setObjectName("el_3x3_5")
        self.el_3x3_6 = QtWidgets.QLineEdit(self.page_3x3)
        self.el_3x3_6.setGeometry(QtCore.QRect(80, 70, 31, 21))
        self.el_3x3_6.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_3x3_6.setObjectName("el_3x3_6")
        self.el_3x3_7 = QtWidgets.QLineEdit(self.page_3x3)
        self.el_3x3_7.setGeometry(QtCore.QRect(0, 110, 31, 21))
        self.el_3x3_7.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_3x3_7.setObjectName("el_3x3_7")
        self.el_3x3_8 = QtWidgets.QLineEdit(self.page_3x3)
        self.el_3x3_8.setGeometry(QtCore.QRect(40, 110, 31, 21))
        self.el_3x3_8.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_3x3_8.setObjectName("el_3x3_8")
        self.el_3x3_9 = QtWidgets.QLineEdit(self.page_3x3)
        self.el_3x3_9.setGeometry(QtCore.QRect(80, 110, 31, 21))
        self.el_3x3_9.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_3x3_9.setObjectName("el_3x3_9")
        self.el_3x3_10 = QtWidgets.QLineEdit(self.page_3x3)
        self.el_3x3_10.setGeometry(QtCore.QRect(160, 30, 31, 21))
        self.el_3x3_10.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_3x3_10.setObjectName("el_3x3_10")
        self.el_3x3_11 = QtWidgets.QLineEdit(self.page_3x3)
        self.el_3x3_11.setGeometry(QtCore.QRect(160, 70, 31, 21))
        self.el_3x3_11.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_3x3_11.setObjectName("el_3x3_11")
        self.el_3x3_12 = QtWidgets.QLineEdit(self.page_3x3)
        self.el_3x3_12.setGeometry(QtCore.QRect(160, 110, 31, 21))
        self.el_3x3_12.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_3x3_12.setObjectName("el_3x3_12")
        self.pages_spins.addWidget(self.page_3x3)
        self.page_4x4 = QtWidgets.QWidget()
        self.page_4x4.setObjectName("page_4x4")
        self.el_4x4_1 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_1.setGeometry(QtCore.QRect(0, 30, 21, 21))
        self.el_4x4_1.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_1.setObjectName("el_4x4_1")
        self.el_4x4_2 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_2.setGeometry(QtCore.QRect(30, 30, 21, 21))
        self.el_4x4_2.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_2.setObjectName("el_4x4_2")
        self.el_4x4_3 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_3.setGeometry(QtCore.QRect(60, 30, 21, 21))
        self.el_4x4_3.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_3.setObjectName("el_4x4_3")
        self.el_4x4_4 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_4.setGeometry(QtCore.QRect(90, 30, 21, 21))
        self.el_4x4_4.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_4.setObjectName("el_4x4_4")
        self.el_4x4_5 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_5.setGeometry(QtCore.QRect(0, 60, 21, 21))
        self.el_4x4_5.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_5.setObjectName("el_4x4_5")
        self.el_4x4_6 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_6.setGeometry(QtCore.QRect(30, 60, 21, 21))
        self.el_4x4_6.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_6.setObjectName("el_4x4_6")
        self.el_4x4_7 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_7.setGeometry(QtCore.QRect(60, 60, 21, 21))
        self.el_4x4_7.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_7.setObjectName("el_4x4_7")
        self.el_4x4_8 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_8.setGeometry(QtCore.QRect(90, 60, 21, 21))
        self.el_4x4_8.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_8.setObjectName("el_4x4_8")
        self.el_4x4_9 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_9.setGeometry(QtCore.QRect(0, 90, 21, 21))
        self.el_4x4_9.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_9.setObjectName("el_4x4_9")
        self.el_4x4_10 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_10.setGeometry(QtCore.QRect(30, 90, 21, 21))
        self.el_4x4_10.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_10.setObjectName("el_4x4_10")
        self.el_4x4_11 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_11.setGeometry(QtCore.QRect(60, 90, 21, 21))
        self.el_4x4_11.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_11.setObjectName("el_4x4_11")
        self.el_4x4_12 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_12.setGeometry(QtCore.QRect(90, 90, 21, 21))
        self.el_4x4_12.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_12.setObjectName("el_4x4_12")
        self.el_4x4_13 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_13.setGeometry(QtCore.QRect(0, 120, 21, 21))
        self.el_4x4_13.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_13.setObjectName("el_4x4_13")
        self.el_4x4_14 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_14.setGeometry(QtCore.QRect(30, 120, 21, 21))
        self.el_4x4_14.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_14.setObjectName("el_4x4_14")
        self.el_4x4_15 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_15.setGeometry(QtCore.QRect(60, 120, 21, 21))
        self.el_4x4_15.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_15.setObjectName("el_4x4_15")
        self.el_4x4_16 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_16.setGeometry(QtCore.QRect(90, 120, 21, 21))
        self.el_4x4_16.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_16.setObjectName("el_4x4_16")
        self.el_4x4_17 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_17.setGeometry(QtCore.QRect(170, 30, 21, 21))
        self.el_4x4_17.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_17.setObjectName("el_4x4_17")
        self.el_4x4_18 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_18.setGeometry(QtCore.QRect(170, 60, 21, 21))
        self.el_4x4_18.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_18.setObjectName("el_4x4_18")
        self.el_4x4_19 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_19.setGeometry(QtCore.QRect(170, 90, 21, 21))
        self.el_4x4_19.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_19.setObjectName("el_4x4_19")
        self.el_4x4_20 = QtWidgets.QLineEdit(self.page_4x4)
        self.el_4x4_20.setGeometry(QtCore.QRect(170, 120, 21, 21))
        self.el_4x4_20.setStyleSheet("border: 1px solid #00cec9;\n"
"color:  rgb(240, 240, 240);")
        self.el_4x4_20.setObjectName("el_4x4_20")
        self.pages_spins.addWidget(self.page_4x4)
        self.label_5 = QtWidgets.QLabel(self.page_1)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(231, 231, 231);")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.page_1)
        self.label_7.setGeometry(QtCore.QRect(140, 70, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(231, 231, 231);")
        self.label_7.setObjectName("label_7")
        self.label_9.raise_()
        self.input_iterations.raise_()
        self.output.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.btn_calculate.raise_()
        self.comboBox.raise_()
        self.pages_spins.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.pages_widget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 261, 371))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("About.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(20, 190, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(23, 23, 23);\n"
"color: rgb(220, 220, 220);")
        self.label_2.setObjectName("label_2")
        self.pages_widget.addWidget(self.page_2)
        self.page_2_rus = QtWidgets.QWidget()
        self.page_2_rus.setObjectName("page_2_rus")
        self.label_21 = QtWidgets.QLabel(self.page_2_rus)
        self.label_21.setGeometry(QtCore.QRect(0, 0, 251, 371))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("about_rus.png"))
        self.label_21.setObjectName("label_21")
        self.label_10 = QtWidgets.QLabel(self.page_2_rus)
        self.label_10.setGeometry(QtCore.QRect(20, 190, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(23, 23, 23);\n"
"color: rgb(220, 220, 220);")
        self.label_10.setObjectName("label_10")
        self.pages_widget.addWidget(self.page_2_rus)
        self.unknown = QtWidgets.QWidget()
        self.unknown.setObjectName("unknown")
        self.pages_widget.addWidget(self.unknown)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setGeometry(QtCore.QRect(0, -10, 261, 381))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Author.png"))
        self.label_6.setObjectName("label_6")
        self.pages_widget.addWidget(self.page_3)
        self.page_3_rus = QtWidgets.QWidget()
        self.page_3_rus.setObjectName("page_3_rus")
        self.label_22 = QtWidgets.QLabel(self.page_3_rus)
        self.label_22.setGeometry(QtCore.QRect(0, 0, 251, 371))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("author_rus.png"))
        self.label_22.setObjectName("label_22")
        self.pages_widget.addWidget(self.page_3_rus)
        self.page_sttngs = QtWidgets.QWidget()
        self.page_sttngs.setObjectName("page_sttngs")
        self.btn_page_5 = QtWidgets.QPushButton(self.page_sttngs)
        self.btn_page_5.setGeometry(QtCore.QRect(30, 80, 91, 31))
        self.btn_page_5.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn_page_5.setFont(font)
        self.btn_page_5.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(17, 17, 17);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#00cec9\n"
"}\n"
"")
        self.btn_page_5.setObjectName("btn_page_5")
        self.btn_page_6 = QtWidgets.QPushButton(self.page_sttngs)
        self.btn_page_6.setGeometry(QtCore.QRect(140, 80, 91, 31))
        self.btn_page_6.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn_page_6.setFont(font)
        self.btn_page_6.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(17, 17, 17);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#00cec9\n"
"}\n"
"")
        self.btn_page_6.setObjectName("btn_page_6")
        self.btn_page_7 = QtWidgets.QPushButton(self.page_sttngs)
        self.btn_page_7.setGeometry(QtCore.QRect(30, 150, 91, 31))
        self.btn_page_7.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn_page_7.setFont(font)
        self.btn_page_7.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(17, 17, 17);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #00cec9\n"
"}")
        self.btn_page_7.setObjectName("btn_page_7")
        self.btn_page_8 = QtWidgets.QPushButton(self.page_sttngs)
        self.btn_page_8.setGeometry(QtCore.QRect(140, 150, 91, 31))
        self.btn_page_8.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn_page_8.setFont(font)
        self.btn_page_8.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(17, 17, 17);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f39c12\n"
"}\n"
"")
        self.btn_page_8.setObjectName("btn_page_8")
        self.label_8 = QtWidgets.QLabel(self.page_sttngs)
        self.label_8.setGeometry(QtCore.QRect(-4, 2, 251, 361))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("page_settings.png"))
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.page_sttngs)
        self.label_11.setGeometry(QtCore.QRect(30, 10, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(23, 23, 23);\n"
"color: rgb(220, 220, 220);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page_sttngs)
        self.label_12.setGeometry(QtCore.QRect(60, 50, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(23, 23, 23);\n"
"color: rgb(220, 220, 220);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.page_sttngs)
        self.label_13.setGeometry(QtCore.QRect(60, 120, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(23, 23, 23);\n"
"color: rgb(220, 220, 220);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page_sttngs)
        self.label_14.setGeometry(QtCore.QRect(60, 200, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(23, 23, 23);\n"
"color: rgb(220, 220, 220);")
        self.label_14.setObjectName("label_14")
        self.btn_page_9 = QtWidgets.QPushButton(self.page_sttngs)
        self.btn_page_9.setGeometry(QtCore.QRect(30, 230, 191, 31))
        self.btn_page_9.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn_page_9.setFont(font)
        self.btn_page_9.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(17, 17, 17);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #00cec9\n"
"}")
        self.btn_page_9.setObjectName("btn_page_9")
        self.label_8.raise_()
        self.btn_page_5.raise_()
        self.btn_page_6.raise_()
        self.btn_page_7.raise_()
        self.btn_page_8.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.btn_page_9.raise_()
        self.pages_widget.addWidget(self.page_sttngs)
        self.verticalLayout_2.addWidget(self.pages_widget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pages_widget.setCurrentIndex(0)
        self.pages_spins.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "JACOBI METHOD"))
        self.btn_page_1.setText(_translate("MainWindow", "Main"))
        self.btn_page_2.setText(_translate("MainWindow", "About"))
        self.btn_page_3.setText(_translate("MainWindow", "Author"))
        self.label_3.setText(_translate("MainWindow", "Order"))
        self.label_4.setText(_translate("MainWindow", "Iterations"))
        self.btn_calculate.setText(_translate("MainWindow", "CALCULATE"))
        self.label_5.setText(_translate("MainWindow", "Matrix A"))
        self.label_7.setText(_translate("MainWindow", "Vector B"))
        self.label_2.setText(_translate("MainWindow", "Links: Wikipedia"))
        self.label_10.setText(_translate("MainWindow", "Ссылки: Википедия"))
        self.btn_page_5.setText(_translate("MainWindow", "Eng"))
        self.btn_page_6.setText(_translate("MainWindow", "Rus"))
        self.btn_page_7.setText(_translate("MainWindow", "Blue"))
        self.btn_page_8.setText(_translate("MainWindow", "Orange"))
        self.label_11.setText(_translate("MainWindow", "SETTINGS"))
        self.label_12.setText(_translate("MainWindow", "Language"))
        self.label_13.setText(_translate("MainWindow", "Theme color"))
        self.label_14.setText(_translate("MainWindow", "Save in .txt"))
        self.btn_page_9.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
