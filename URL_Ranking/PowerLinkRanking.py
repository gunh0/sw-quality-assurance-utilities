# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Power Link Ranking Program")
        Dialog.resize(692, 892)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 671, 861))
        self.tabWidget.setObjectName("tabWidget")
        self.Basic_Tab = QtWidgets.QWidget()
        self.Basic_Tab.setObjectName("Basic_Tab")
        self.label_Keyword = QtWidgets.QLabel(self.Basic_Tab)
        self.label_Keyword.setGeometry(QtCore.QRect(70, 70, 56, 20))
        self.label_Keyword.setObjectName("label_Keyword")
        self.Input_URL = QtWidgets.QTextEdit(self.Basic_Tab)
        self.Input_URL.setGeometry(QtCore.QRect(150, 20, 491, 31))
        self.Input_URL.setObjectName("Input_URL")
        self.Input_Keyword = QtWidgets.QTextEdit(self.Basic_Tab)
        self.Input_Keyword.setGeometry(QtCore.QRect(150, 70, 491, 31))
        self.Input_Keyword.setObjectName("Input_Keyword")
        self.label_URL = QtWidgets.QLabel(self.Basic_Tab)
        self.label_URL.setGeometry(QtCore.QRect(60, 30, 71, 21))
        self.label_URL.setObjectName("label_URL")
        self.Search = QtWidgets.QPushButton(self.Basic_Tab)
        self.Search.setGeometry(QtCore.QRect(520, 120, 121, 23))
        self.Search.setObjectName("Search")
        self.Download = QtWidgets.QPushButton(self.Basic_Tab)
        self.Download.setGeometry(QtCore.QRect(520, 150, 121, 23))
        self.Download.setObjectName("Download")
        
        self.ResultTable = QtWidgets.QTableWidget(self.Basic_Tab)
        self.ResultTable.setGeometry(QtCore.QRect(20, 180, 621, 581))
        self.ResultTable.setObjectName("ResultTable")
        self.ResultTable.setColumnCount(3)
        self.ResultTable.setRowCount(25)

        self.Next = QtWidgets.QPushButton(self.Basic_Tab)
        self.Next.setGeometry(QtCore.QRect(360, 780, 75, 23))
        self.Next.setObjectName("Next")
        self.Previous = QtWidgets.QPushButton(self.Basic_Tab)
        self.Previous.setGeometry(QtCore.QRect(230, 780, 75, 23))
        self.Previous.setObjectName("Previous")
        self.tabWidget.addTab(self.Basic_Tab, "")
        self.Multi_Tab = QtWidgets.QWidget()
        self.Multi_Tab.setObjectName("Multi_Tab")
        self.Upload_btn = QtWidgets.QPushButton(self.Multi_Tab)
        self.Upload_btn.setGeometry(QtCore.QRect(40, 50, 75, 23))
        self.Upload_btn.setObjectName("Upload_btn")
        self.LocalPath = QtWidgets.QTextBrowser(self.Multi_Tab)
        self.LocalPath.setGeometry(QtCore.QRect(130, 40, 501, 31))
        self.LocalPath.setObjectName("LocalPath")
        self.Search2 = QtWidgets.QPushButton(self.Multi_Tab)
        self.Search2.setGeometry(QtCore.QRect(510, 100, 121, 23))
        self.Search2.setObjectName("Search2")
        self.Download2 = QtWidgets.QPushButton(self.Multi_Tab)
        self.Download2.setGeometry(QtCore.QRect(510, 130, 121, 23))
        self.Download2.setObjectName("Download2")
        self.Previous2 = QtWidgets.QPushButton(self.Multi_Tab)
        self.Previous2.setGeometry(QtCore.QRect(230, 790, 75, 23))
        self.Previous2.setObjectName("Previous2")
        self.Next2 = QtWidgets.QPushButton(self.Multi_Tab)
        self.Next2.setGeometry(QtCore.QRect(360, 790, 75, 23))
        self.Next2.setObjectName("Next2")
        self.ResultTable2 = QtWidgets.QTableWidget(self.Multi_Tab)
        self.ResultTable2.setGeometry(QtCore.QRect(20, 190, 621, 581))
        self.ResultTable2.setObjectName("ResultTable2")
        self.ResultTable2.setColumnCount(3)
        self.ResultTable2.setRowCount(25)

        self.tabWidget.addTab(self.Multi_Tab, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Power Link Ranking Program"))
        self.label_Keyword.setText(_translate("Dialog", "Keyword"))
        self.label_URL.setText(_translate("Dialog", "Search URL"))
        self.Search.setText(_translate("Dialog", "Search"))
        self.Download.setText(_translate("Dialog", "Download (Excel)"))
        self.Next.setText(_translate("Dialog", "Next"))
        self.Previous.setText(_translate("Dialog", "Previous"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Basic_Tab), _translate("Dialog", "Basic"))
        self.Upload_btn.setText(_translate("Dialog", "Upload"))
        self.Search2.setText(_translate("Dialog", "Search"))
        self.Download2.setText(_translate("Dialog", "Download (Excel)"))
        self.Previous2.setText(_translate("Dialog", "Previous"))
        self.Next2.setText(_translate("Dialog", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Multi_Tab), _translate("Dialog", "Multi"))

    def SearchClicked(self):
        keyword = self.Input_Keyword.text()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
