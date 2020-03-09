from tkinter import *
import tkinter.messagebox

def loadWrongPath(absPath):
    win = Tk()
    win.title("오류")

    errorText = "\n" + absPath + "\n\n파일을 불러올 수 없습니다.\n"
    lbl = Label(win, text=errorText)
    lbl.grid(row=2, column=1)

    btn = Button(win, text="확인", width=8, command=win.destroy)
    btn.grid(row=3, column=1)

    win.mainloop()

def loadWrongForm(absPath):
    win = Tk()
    win.title("오류")

    errorText = "\n" + absPath + "\n\n양식에 맞지 않은 파일입니다.\n"
    lbl = Label(win, text=errorText)
    lbl.grid(row=2, column=1)

    btn = Button(win, text="확인", width=8, command=win.destroy)
    btn.grid(row=3, column=1)

    win.mainloop()

def NoneTableData():
    win = Tk()
    win.title("오류")

    errorText = "\n\n저장할 데이터가 없습니다.\n"
    lbl = Label(win, text=errorText)
    lbl.grid(row=2, column=1)

    btn = Button(win, text="확인", width=8, command=win.destroy)
    btn.grid(row=3, column=1)

    win.mainloop()

def PageBtnError():
    win = Tk()
    win.title("오류")

    errorText = "없는 페이지입니다."
    lbl = Label(win, text=errorText)
    lbl.grid(row=2, column=1)

    btn = Button(win, text="확인", width=8, command=win.destroy)
    btn.grid(row=3, column=1)

    win.mainloop()

def FileLoadError():
    win = Tk()
    win.title("오류")

    errorText = "지원하지 않는 파일형식입니다."
    lbl = Label(win, text=errorText)
    lbl.grid(row=2, column=1)

    btn = Button(win, text="확인", width=8, command=win.destroy)
    btn.grid(row=3, column=1)

    win.mainloop()