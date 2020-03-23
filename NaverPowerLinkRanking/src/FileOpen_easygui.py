'''
easygui Web:
    https://easygui.readthedocs.io/en/latest

easygui Documentation(pdf):
    https://readthedocs.org/projects/easygui/downloads/pdf/latest/

윈도우 파일 탐색기를 띄우기 위해 fileopenbox() 사용
'''

import easygui

# fileopenbox: fileopenbox returns the name of a file

def OpenWinFileExplorer():
    multiSearchFilePath = easygui.fileopenbox()
    return multiSearchFilePath