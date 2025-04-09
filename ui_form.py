# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTreeView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1295, 858)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tree_view_1 = QTreeView(self.centralwidget)
        self.tree_view_1.setObjectName(u"tree_view_1")
        self.tree_view_1.setGeometry(QRect(550, 120, 171, 221))
        self.search_box = QLineEdit(self.centralwidget)
        self.search_box.setObjectName(u"search_box")
        self.search_box.setGeometry(QRect(550, 90, 351, 24))
        self.tree_view_2 = QTreeView(self.centralwidget)
        self.tree_view_2.setObjectName(u"tree_view_2")
        self.tree_view_2.setGeometry(QRect(730, 120, 171, 221))
        self.tree_view_3 = QTreeView(self.centralwidget)
        self.tree_view_3.setObjectName(u"tree_view_3")
        self.tree_view_3.setGeometry(QRect(910, 120, 171, 221))
        self.tree_view_4 = QTreeView(self.centralwidget)
        self.tree_view_4.setObjectName(u"tree_view_4")
        self.tree_view_4.setGeometry(QRect(1090, 120, 161, 221))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(590, 460, 80, 24))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(710, 460, 80, 24))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(820, 460, 80, 24))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(620, 560, 80, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PDF", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"DOCX", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Kep feltoltes", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Hozz\u00e1ad\u00e1s", None))
    # retranslateUi

