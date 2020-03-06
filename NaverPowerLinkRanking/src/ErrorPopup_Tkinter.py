from tkinter import *
import tkinter.messagebox

def loadWrongPath(absPath):
    win = Tk()
    win.title("오류")

    errorText = "\n" + absPath + "\n\n 위치의 파일을 불러올 수 없습니다.\n"
    lbl = Label(win, text=errorText)
    lbl.grid(row=2, column=1)

    btn = Button(win, text="확인", width=8, command=win.destroy)
    btn.grid(row=3, column=1)

    win.mainloop()

def PreviousBtnError():
    win = Tk()
    win.title("오류")

    errorText = "첫 페이지 입니다."
    lbl = Label(win, text=errorText)
    lbl.grid(row=2, column=1)

    btn = Button(win, text="확인", width=8, command=win.destroy)
    btn.grid(row=3, column=1)

    win.mainloop()