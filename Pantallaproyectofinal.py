# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pantallaproyectofinal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(681, 417)
        Form.setMinimumSize(QtCore.QSize(681, 400))
        Form.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.pantalla = QtWidgets.QTabWidget(Form)
        self.pantalla.setGeometry(QtCore.QRect(0, 0, 551, 421))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pantalla.sizePolicy().hasHeightForWidth())
        self.pantalla.setSizePolicy(sizePolicy)
        self.pantalla.setMinimumSize(QtCore.QSize(541, 400))
        self.pantalla.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.pantalla.setObjectName("pantalla")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.bt_refrescar = QtWidgets.QPushButton(self.tab_5)
        self.bt_refrescar.setGeometry(QtCore.QRect(204, 350, 101, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 191, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 191, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 191, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.bt_refrescar.setPalette(palette)
        self.bt_refrescar.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.bt_refrescar.setObjectName("bt_refrescar")
        self.tabla_canciones = QtWidgets.QTableWidget(self.tab_5)
        self.tabla_canciones.setGeometry(QtCore.QRect(30, 60, 511, 281))
        self.tabla_canciones.setRowCount(0)
        self.tabla_canciones.setColumnCount(5)
        self.tabla_canciones.setObjectName("tabla_canciones")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 0, 191))
        self.tabla_canciones.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 255, 127))
        self.tabla_canciones.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 248, 53))
        self.tabla_canciones.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 170, 127))
        self.tabla_canciones.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tabla_canciones.setHorizontalHeaderItem(4, item)
        self.pantalla.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.bt_agregar = QtWidgets.QPushButton(self.tab_2)
        self.bt_agregar.setGeometry(QtCore.QRect(420, 260, 75, 23))
        self.bt_agregar.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.bt_agregar.setObjectName("bt_agregar")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 70, 231, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.codigoA = QtWidgets.QLineEdit(self.layoutWidget)
        self.codigoA.setObjectName("codigoA")
        self.verticalLayout.addWidget(self.codigoA)
        self.nombreA = QtWidgets.QLineEdit(self.layoutWidget)
        self.nombreA.setObjectName("nombreA")
        self.verticalLayout.addWidget(self.nombreA)
        self.generoA = QtWidgets.QLineEdit(self.layoutWidget)
        self.generoA.setObjectName("generoA")
        self.verticalLayout.addWidget(self.generoA)
        self.albumA = QtWidgets.QLineEdit(self.layoutWidget)
        self.albumA.setObjectName("albumA")
        self.verticalLayout.addWidget(self.albumA)
        self.interpreteA = QtWidgets.QLineEdit(self.layoutWidget)
        self.interpreteA.setObjectName("interpreteA")
        self.verticalLayout.addWidget(self.interpreteA)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.pantalla.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.bt_actualizar = QtWidgets.QPushButton(self.tab_3)
        self.bt_actualizar.setGeometry(QtCore.QRect(60, 200, 91, 21))
        self.bt_actualizar.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.bt_actualizar.setObjectName("bt_actualizar")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(270, 80, 251, 221))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.codigo = QtWidgets.QLabel(self.layoutWidget1)
        self.codigo.setObjectName("codigo")
        self.verticalLayout_4.addWidget(self.codigo)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.codigo_actualizar = QtWidgets.QLineEdit(self.layoutWidget1)
        self.codigo_actualizar.setObjectName("codigo_actualizar")
        self.verticalLayout_3.addWidget(self.codigo_actualizar)
        self.nombre_actualizar = QtWidgets.QLineEdit(self.layoutWidget1)
        self.nombre_actualizar.setObjectName("nombre_actualizar")
        self.verticalLayout_3.addWidget(self.nombre_actualizar)
        self.genero_actualizar = QtWidgets.QLineEdit(self.layoutWidget1)
        self.genero_actualizar.setObjectName("genero_actualizar")
        self.verticalLayout_3.addWidget(self.genero_actualizar)
        self.album_actualizar = QtWidgets.QLineEdit(self.layoutWidget1)
        self.album_actualizar.setObjectName("album_actualizar")
        self.verticalLayout_3.addWidget(self.album_actualizar)
        self.interprete_actualizar = QtWidgets.QLineEdit(self.layoutWidget1)
        self.interprete_actualizar.setObjectName("interprete_actualizar")
        self.verticalLayout_3.addWidget(self.interprete_actualizar)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.id_cancion = QtWidgets.QLineEdit(self.tab_3)
        self.id_cancion.setGeometry(QtCore.QRect(30, 120, 180, 20))
        self.id_cancion.setObjectName("id_cancion")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(40, 80, 191, 39))
        self.label_13.setObjectName("label_13")
        self.id_buscar = QtWidgets.QPushButton(self.tab_3)
        self.id_buscar.setGeometry(QtCore.QRect(70, 150, 75, 23))
        self.id_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.id_buscar.setObjectName("id_buscar")
        self.pantalla.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.bt_buscar = QtWidgets.QPushButton(self.tab)
        self.bt_buscar.setGeometry(QtCore.QRect(250, 360, 75, 23))
        self.bt_buscar.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.bt_buscar.setObjectName("bt_buscar")
        self.codigoB = QtWidgets.QLineEdit(self.tab)
        self.codigoB.setGeometry(QtCore.QRect(72, 51, 101, 20))
        self.codigoB.setText("")
        self.codigoB.setObjectName("codigoB")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(21, 51, 45, 16))
        self.label.setObjectName("label")
        self.tabla_buscar = QtWidgets.QTableWidget(self.tab)
        self.tabla_buscar.setGeometry(QtCore.QRect(30, 90, 511, 261))
        self.tabla_buscar.setRowCount(0)
        self.tabla_buscar.setColumnCount(5)
        self.tabla_buscar.setObjectName("tabla_buscar")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 0, 191))
        self.tabla_buscar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 255, 127))
        self.tabla_buscar.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 248, 53))
        self.tabla_buscar.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 170, 127))
        self.tabla_buscar.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tabla_buscar.setHorizontalHeaderItem(4, item)
        self.pantalla.addTab(self.tab, "")

        self.retranslateUi(Form)
        self.pantalla.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "REGISTRO DE PRODUCTOS"))
        self.bt_refrescar.setText(_translate("Form", "REFRESCAR"))
        item = self.tabla_canciones.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Codigo"))
        item = self.tabla_canciones.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombre"))
        item = self.tabla_canciones.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Genero"))
        item = self.tabla_canciones.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Album"))
        item = self.tabla_canciones.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Interprete"))
        self.pantalla.setTabText(self.pantalla.indexOf(self.tab_5), _translate("Form", "CANCIONES"))
        self.bt_agregar.setText(_translate("Form", "AGREGAR"))
        self.label_2.setText(_translate("Form", "CODIGO:"))
        self.label_3.setText(_translate("Form", "NOMBRE:"))
        self.label_4.setText(_translate("Form", "GENERO:"))
        self.label_5.setText(_translate("Form", "ALBUM:"))
        self.label_6.setText(_translate("Form", "INTERPRETE:"))
        self.pantalla.setTabText(self.pantalla.indexOf(self.tab_2), _translate("Form", "AGREGARCANCIONES"))
        self.bt_actualizar.setText(_translate("Form", "ACTUALIZAR"))
        self.codigo.setText(_translate("Form", "NOMBRE:"))
        self.label_8.setText(_translate("Form", "NOMBRE:"))
        self.label_9.setText(_translate("Form", "GENERO:"))
        self.label_10.setText(_translate("Form", "ALBUM: "))
        self.label_11.setText(_translate("Form", "INTERPRETE: "))
        self.label_13.setText(_translate("Form", "INGRESE EL ID DE LA CANCION"))
        self.id_buscar.setText(_translate("Form", "BUSCAR"))
        self.pantalla.setTabText(self.pantalla.indexOf(self.tab_3), _translate("Form", "MODIFICARCANCIONES"))
        self.bt_buscar.setText(_translate("Form", "BUSCAR"))
        self.label.setText(_translate("Form", "CODIGO:"))
        item = self.tabla_buscar.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Codigo"))
        item = self.tabla_buscar.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombre"))
        item = self.tabla_buscar.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Genero"))
        item = self.tabla_buscar.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Album"))
        item = self.tabla_buscar.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Interprete"))
        self.pantalla.setTabText(self.pantalla.indexOf(self.tab), _translate("Form", "CONSULTARCANCION"))
