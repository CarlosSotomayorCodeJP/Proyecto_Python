# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import imagenes_rc

class Ui_FormLogin(object):
    def setupUi(self, FormLogin):
        if not FormLogin.objectName():
            FormLogin.setObjectName(u"FormLogin")
        FormLogin.resize(750, 573)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush2 = QBrush(QColor(255, 255, 220, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush2)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 127))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        brush4 = QBrush(QColor(0, 0, 0, 127))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush1)
        FormLogin.setPalette(palette)
        FormLogin.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        FormLogin.setSizeGripEnabled(False)
        FormLogin.setModal(False)
        self.label = QLabel(FormLogin)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 110, 521, 211))
        self.label.setPixmap(QPixmap(u":/xy/banco-union.png"))
        self.label_2 = QLabel(FormLogin)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 340, 101, 31))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        brush5 = QBrush(QColor(212, 255, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush5)
        brush6 = QBrush(QColor(148, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        brush7 = QBrush(QColor(42, 127, 127, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush7)
        brush8 = QBrush(QColor(57, 170, 170, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush9 = QBrush(QColor(85, 255, 255, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush9)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        brush10 = QBrush(QColor(85, 170, 255, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
        brush11 = QBrush(QColor(170, 255, 255, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush11)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.Active, QPalette.Accent, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Accent, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        brush12 = QBrush(QColor(42, 127, 127, 127))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.Accent, brush9)
        self.label_2.setPalette(palette1)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_3 = QLabel(FormLogin)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 390, 71, 16))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush)
        brush13 = QBrush(QColor(127, 127, 127, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush13)
        brush14 = QBrush(QColor(170, 170, 170, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette2.setBrush(QPalette.Active, QPalette.Accent, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.Accent, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        brush15 = QBrush(QColor(127, 127, 127, 127))
        brush15.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.Accent, brush)
        self.label_3.setPalette(palette2)
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(FormLogin)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 440, 91, 16))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush2)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette3.setBrush(QPalette.Active, QPalette.Accent, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.Accent, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.Accent, brush)
        self.label_4.setPalette(palette3)
        self.label_4.setFont(font1)
        self.lineEdit = QLineEdit(FormLogin)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 380, 191, 31))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush2)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette4.setBrush(QPalette.Active, QPalette.Accent, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.Accent, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.Accent, brush)
        self.lineEdit.setPalette(palette4)
        self.lineEdit.setFont(font1)
        self.lineEdit_2 = QLineEdit(FormLogin)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(150, 430, 191, 31))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette5.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipBase, brush2)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette5.setBrush(QPalette.Active, QPalette.Accent, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.Accent, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.Accent, brush)
        self.lineEdit_2.setPalette(palette5)
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.pushButton = QPushButton(FormLogin)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 490, 71, 31))
        palette6 = QPalette()
        brush16 = QBrush(QColor(82, 180, 255, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush16)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush16)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        brush17 = QBrush(QColor(255, 255, 255, 135))
        brush17.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush16)
        self.pushButton.setPalette(palette6)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setStrikeOut(False)
        self.pushButton.setFont(font2)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setTabletTracking(False)
        self.pushButton.setStyleSheet(u"background-color: rgb(82, 180, 255);\n"
"border-radius: 8px;")
        self.label_5 = QLabel(FormLogin)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 530, 611, 20))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush5)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette7.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush11)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipBase, brush2)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette7.setBrush(QPalette.Active, QPalette.Accent, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush11)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.Accent, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        brush18 = QBrush(QColor(161, 255, 255, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Disabled, QPalette.Accent, brush18)
        self.label_5.setPalette(palette7)

        self.retranslateUi(FormLogin)

        QMetaObject.connectSlotsByName(FormLogin)
    # setupUi

    def retranslateUi(self, FormLogin):
        FormLogin.setWindowTitle(QCoreApplication.translate("FormLogin", u"Inicio de seccion ", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("FormLogin", u"Iniciar sesi\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("FormLogin", u"Usuario:", None))
        self.label_4.setText(QCoreApplication.translate("FormLogin", u"Contrase\u00f1a:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("FormLogin", u"Ingrese su usuario", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("FormLogin", u"Ingrese su contrase\u00f1a", None))
        self.pushButton.setText(QCoreApplication.translate("FormLogin", u"Aceptar", None))
        self.label_5.setText(QCoreApplication.translate("FormLogin", u"Mensage", None))
    # retranslateUi

