'''
easygui Web:
    https://easygui.readthedocs.io/en/latest

easygui Documentation(pdf):
    https://readthedocs.org/projects/easygui/downloads/pdf/latest/
'''

import easygui

# fileopenbox: fileopenbox returns the name of a file

def OpenWinFileExplorer():
    multiSearchFilePath = easygui.fileopenbox()
    return multiSearchFilePath

'''
        keyword_col2.clear()
        ranking_col2.clear()
        url_col2.clear()
        self.ResultTable2.setRowCount(0)
        self.ResultTable2.setRowCount(25)
        self.ResultTable2.resizeColumnsToContents()
        self.ResultTable2.resizeRowsToContents()

        multiSearchFilePath = easygui.fileopenbox()
        self.LocalPath.setText(multiSearchFilePath)
        multiSearchFilePath = self.LocalPath.text()
        
        rawdata = open(multiSearchFilePath, "r").read()
        result = chardet.detect(rawdata)
        print(result)
        charenc = result['encoding']
        print(charenc)
'''