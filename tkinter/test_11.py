from tkinter import *
from tkinter import messagebox

"""
消息弹窗
"""
root = Tk()# 初始化


frame = Frame(root)
frame.pack()
def hit_me():  messagebox.showinfo(title='提示', message='错误')
button = Button(frame, text='点我', command=hit_me)
button.pack()
mainloop()

