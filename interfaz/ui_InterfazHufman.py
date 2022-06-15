# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InterfazHufmanyUhlgx.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(401, 636)
        Form.setMaximumSize(QSize(401, 636))
        icon = QIcon()
        icon.addFile(u":/icono/resources/letra-h.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"Qwidget\n"
"{\n"
"background-color: rgb(46, 194, 126);\n"
"};")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 60, 281, 16))
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.ejecutar = QPushButton(Form)
        self.ejecutar.setObjectName(u"ejecutar")
        self.ejecutar.setGeometry(QRect(10, 120, 381, 31))
        font1 = QFont()
        font1.setItalic(True)
        self.ejecutar.setFont(font1)
        self.ejecutar.setStyleSheet(u"QPushButton\n"
"\n"
"{\n"
"rgb(53, 132, 228)\n"
"	border-bottom-color: rgb(245, 194, 17);\n"
"font: 700 italic 10pt \"DejaVu Sans\";\n"
"}")
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        font2 = QFont()
        font2.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 160, 341, 141))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 320, 181, 16))
        self.label_2.setFont(font2)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 10, 391, 31))
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(False)
        self.label_3.setFont(font3)
        self.ruta = QLineEdit(Form)
        self.ruta.setObjectName(u"ruta")
        self.ruta.setGeometry(QRect(10, 80, 381, 31))
        self.tabla = QTableWidget(Form)
        if (self.tabla.columnCount() < 2):
            self.tabla.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        self.tabla.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font2);
        self.tabla.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setGeometry(QRect(0, 350, 401, 281))
        self.tabla.horizontalHeader().setDefaultSectionSize(200)
        self.tabla.verticalHeader().setVisible(True)
        self.tabla.verticalHeader().setCascadingSectionResizes(False)
        self.label.raise_()
        self.ejecutar.raise_()
        self.tableWidget.raise_()
        self.label_3.raise_()
        self.ruta.raise_()
        self.label_2.raise_()
        self.tabla.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Compresi\u00f3n Huffman", None))
#if QT_CONFIG(tooltip)
        Form.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label.setStatusTip(QCoreApplication.translate("Form", u"sdasfsadf", None))
#endif // QT_CONFIG(statustip)
        self.label.setText(QCoreApplication.translate("Form", u"Ingresa la ruta del archivo de texto:", None))
#if QT_CONFIG(tooltip)
        self.ejecutar.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.ejecutar.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.ejecutar.setText(QCoreApplication.translate("Form", u"Ejecutar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Datos", None));
        ___qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Tama\u00f1o del archivo comprimido(bytes)", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Tama\u00f1o del archivo original(bytes)", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Porcentaje de comprensi\u00f3n(%)", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Longitud media", None));
        self.label_2.setText(QCoreApplication.translate("Form", u"Codificaci\u00f3n Huffman por linea", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt;\">Practica 3. Compresi\u00f3n Huffman</span></p></body></html>", None))
        ___qtablewidgetitem5 = self.tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"CARACTER", None));
        ___qtablewidgetitem6 = self.tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"C\u00d3DIGO HUFFMAN", None));
    # retranslateUi

