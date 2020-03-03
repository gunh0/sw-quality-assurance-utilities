import sys
import os
import json
import csv
import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets

url_col = []
keyword_col = []
ranking_col = []
download1Cnt = 0
download2Cnt = 0
searchBtnCnt = 0
url_col2 = []
keyword_col2 = []
ranking_col2 = []

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("PowerLink Ranking Program")
        Dialog.resize(692, 892)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 671, 861))
        self.tabWidget.setObjectName("tabWidget")
        self.Basic_Tab = QtWidgets.QWidget()
        self.Basic_Tab.setObjectName("Basic_Tab")
        self.label_Keyword = QtWidgets.QLabel(self.Basic_Tab)
        self.label_Keyword.setGeometry(QtCore.QRect(70, 70, 56, 20))
        self.label_Keyword.setObjectName("label_Keyword")

        self.Input_URL = QtWidgets.QLineEdit(self.Basic_Tab)
        self.Input_URL.setGeometry(QtCore.QRect(150, 20, 491, 31))
        self.Input_URL.setObjectName("Input_URL")
        self.Input_URL.setText("Input Search URL...")

        self.Input_Keyword = QtWidgets.QLineEdit(self.Basic_Tab)
        self.Input_Keyword.setGeometry(QtCore.QRect(150, 70, 491, 31))
        self.Input_Keyword.setObjectName("Input_Keyword")
        self.Input_Keyword.setText("Input Search Keyword...")

        self.label_URL = QtWidgets.QLabel(self.Basic_Tab)
        self.label_URL.setGeometry(QtCore.QRect(60, 30, 71, 21))
        self.label_URL.setObjectName("label_URL")

        self.Search = QtWidgets.QPushButton(self.Basic_Tab)
        self.Search.setGeometry(QtCore.QRect(520, 120, 121, 23))
        self.Search.setObjectName("Search")
        self.Search.clicked.connect(self.SearchBtnClicked)

        self.Download = QtWidgets.QPushButton(self.Basic_Tab)
        self.Download.setGeometry(QtCore.QRect(520, 150, 121, 23))
        self.Download.setObjectName("Download")
        self.Download.clicked.connect(self.DownloadBtnClicked)

        self.ResultTable = QtWidgets.QTableWidget(self.Basic_Tab)
        self.ResultTable.setGeometry(QtCore.QRect(20, 180, 621, 581))
        self.ResultTable.setObjectName("ResultTable")
        self.ResultTable.setColumnCount(3)
        self.ResultTable.setRowCount(25)
        column_headers = ['URL', 'Keyword', 'Ranking']
        self.ResultTable.setHorizontalHeaderLabels(column_headers)

        self.Next = QtWidgets.QPushButton(self.Basic_Tab)
        self.Next.setGeometry(QtCore.QRect(360, 780, 75, 23))
        self.Next.setObjectName("Next")
        self.Previous = QtWidgets.QPushButton(self.Basic_Tab)
        self.Previous.setGeometry(QtCore.QRect(230, 780, 75, 23))
        self.Previous.setObjectName("Previous")
        self.tabWidget.addTab(self.Basic_Tab, "")
        self.Multi_Tab = QtWidgets.QWidget()
        self.Multi_Tab.setObjectName("Multi_Tab")
        self.Upload_btn = QtWidgets.QLabel(self.Multi_Tab)
        self.Upload_btn.setGeometry(QtCore.QRect(40, 50, 75, 23))
        self.Upload_btn.setObjectName("Upload")
        self.LocalPath = QtWidgets.QLineEdit(self.Multi_Tab)
        self.LocalPath.setGeometry(QtCore.QRect(130, 40, 501, 31))
        self.LocalPath.setObjectName("LocalPath")
        #self.LocalPath.setText("Input CSV file Absolute Path...")
        self.LocalPath.setText(r"D:\Devgun_Repo\URL_Ranking\MultiSearch\MultiSearchSample.csv")

        self.Search2 = QtWidgets.QPushButton(self.Multi_Tab)
        self.Search2.setGeometry(QtCore.QRect(510, 100, 121, 23))
        self.Search2.setObjectName("Search2")
        self.Search2.clicked.connect(self.Search2BtnClicked)
        
        self.Download2 = QtWidgets.QPushButton(self.Multi_Tab)
        self.Download2.setGeometry(QtCore.QRect(510, 130, 121, 23))
        self.Download2.setObjectName("Download2")
        self.Download2.clicked.connect(self.Download2BtnClicked)

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
        self.ResultTable2.setHorizontalHeaderLabels(column_headers)

        self.tabWidget.addTab(self.Multi_Tab, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate(
            "Dialog", "Power Link Ranking Program"))
        self.label_Keyword.setText(_translate("Dialog", "Keyword"))
        self.label_URL.setText(_translate("Dialog", "Search URL"))
        self.Search.setText(_translate("Dialog", "Search"))
        self.Download.setText(_translate("Dialog", "Download (Excel)"))
        self.Next.setText(_translate("Dialog", "Next"))
        self.Previous.setText(_translate("Dialog", "Previous"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.Basic_Tab), _translate("Dialog", "Basic"))
        self.Upload_btn.setText(_translate("Dialog", "Upload"))
        self.Search2.setText(_translate("Dialog", "Search"))
        self.Download2.setText(_translate("Dialog", "Download (Excel)"))
        self.Previous2.setText(_translate("Dialog", "Previous"))
        self.Next2.setText(_translate("Dialog", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.Multi_Tab), _translate("Dialog", "Multi"))

    def SearchBtnClicked(self):
        global searchBtnCnt
        searchBtnCnt+=1
        keyword = self.Input_Keyword.text()
        searchUrl = self.Input_URL.text()

        if keyword != '':
            baseurl = 'https://ad.search.naver.com/search.naver?where=ad&query='
            url = baseurl + quote_plus(keyword)
            req = urllib.request.urlopen(url)
            res = req.read()

            soup = BeautifulSoup(res, 'html.parser')
            divData = soup.find_all('a', class_='url')
            rank = 0
            findFlag = 0
            for urls in divData:
                rank += 1
                #print(keyword, "|", searchUrl, "-", rank, ":", urls.get_text())
                if(searchUrl == urls.get_text()):
                    findFlag = 1
                    url_col.append(searchUrl)
                    keyword_col.append(keyword)
                    ranking_col.append(str(rank))
            if(findFlag == 0):
                url_col.append(searchUrl)
                keyword_col.append(keyword)
                ranking_col.append("None")

        tableTempData = {
            'url_col': url_col,
            'keyword_col': keyword_col,
            'ranking_col': ranking_col
        }
        column_idx_lookup = {'url_col': 0, 'keyword_col': 1, 'ranking_col': 2}

        for k, v in tableTempData.items():
            col = column_idx_lookup[k]
            for row, val in enumerate(v):
                item = QTableWidgetItem(val)
                self.ResultTable.setItem(row, col, item)

        self.ResultTable.resizeColumnsToContents()
        self.ResultTable.resizeRowsToContents()

    def Search2BtnClicked(self):
        multiSearchFilePath = self.LocalPath.text()
        try:
            f = open(multiSearchFilePath, 'r', encoding='utf-8')
        except OSError:
            print('cannot open : ',multiSearchFilePath)
        else:
            reading = csv.reader(f)
            for line in reading:
                if(line[0]=='URL')&(line[1]=='KEYWORD'):
                    continue
                searchUrl = line[0]
                keyword = line[1]
                if keyword != '':
                    baseurl = 'https://ad.search.naver.com/search.naver?where=ad&query='
                    url = baseurl + quote_plus(keyword)
                    req = urllib.request.urlopen(url)
                    res = req.read()

                    soup = BeautifulSoup(res, 'html.parser')
                    divData = soup.find_all('a', class_='url')
                    rank = 0
                    findFlag = 0
                    for urls in divData:
                        rank += 1
                        #print(keyword, "|", searchUrl, "-", rank, ":", urls.get_text())
                        if(searchUrl == urls.get_text()):
                            findFlag = 1
                            url_col2.append(searchUrl)
                            keyword_col2.append(keyword)
                            ranking_col2.append(str(rank))
                    if(findFlag == 0):
                        url_col2.append(searchUrl)
                        keyword_col2.append(keyword)
                        ranking_col2.append("None")
                #print(line)

            tableTempData = {
                'url_col': url_col2,
                'keyword_col': keyword_col2,
                'ranking_col': ranking_col2
            }
            column_idx_lookup = {'url_col': 0, 'keyword_col': 1, 'ranking_col': 2}

            for k, v in tableTempData.items():
                col = column_idx_lookup[k]
                for row, val in enumerate(v):
                    item = QTableWidgetItem(val)
                    self.ResultTable2.setItem(row, col, item)

            self.ResultTable2.resizeColumnsToContents()
            self.ResultTable2.resizeRowsToContents()
            
            f.close()

    def DownloadBtnClicked(self):
        tableTempData = {
            'URL': url_col,
            'KEYWORD': keyword_col,
            'RANKING': ranking_col
        }
        #print(tableTempData)

        current_path = os.path.dirname(os.path.realpath(__file__))
        download_path = current_path + r'\SearchResults'
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        global download1Cnt, searchBtnCnt
        download1Cnt += 1
        output_file_name = download_path + '\SearchResults' + str(download1Cnt) + quote_plus(".csv")
        output_file = open(output_file_name, 'w+', newline='')
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(tableTempData)
        rulList = tableTempData['URL']
        keywordList = tableTempData['KEYWORD']
        rankingList = tableTempData['RANKING']
        for i in range(0,searchBtnCnt):
            tmpRowData=[]
            tmpRowData.append(rulList[i])
            tmpRowData.append(keywordList[i])
            tmpRowData.append(rankingList[i])
            csv_writer.writerow(tmpRowData)
        output_file.close()

        url_col.clear()
        keyword_col.clear()
        ranking_col.clear()
        self.ResultTable.setRowCount(0)
        searchBtnCnt=0
        self.ResultTable.setRowCount(25)
        self.ResultTable.resizeColumnsToContents()
        self.ResultTable.resizeRowsToContents()

    def Download2BtnClicked(self):
        tableTempData = {
            'URL': url_col2,
            'KEYWORD': keyword_col2,
            'RANKING': ranking_col2
        }
        #print(tableTempData)

        current_path = os.path.dirname(os.path.realpath(__file__))
        download_path = current_path + r'\MultiSearchResults'
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        
        global download2Cnt, searchBtnCnt
        download2Cnt += 1
        output_file_name = download_path + '\MultiSearchResults' + str(download2Cnt) + quote_plus(".csv")
        output_file = open(output_file_name, 'w+', newline='')
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(tableTempData)
        rulList = tableTempData['URL']
        keywordList = tableTempData['KEYWORD']
        rankingList = tableTempData['RANKING']
        for i in range(0,len(rulList)):
            tmpRowData=[]
            tmpRowData.append(rulList[i])
            tmpRowData.append(keywordList[i])
            tmpRowData.append(rankingList[i])
            csv_writer.writerow(tmpRowData)
        output_file.close()

        url_col2.clear()
        keyword_col2.clear()
        ranking_col2.clear()
        self.ResultTable2.setRowCount(0)
        self.ResultTable2.setRowCount(25)
        self.ResultTable2.resizeColumnsToContents()
        self.ResultTable2.resizeRowsToContents()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
