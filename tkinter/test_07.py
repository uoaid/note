import tkinter

"""
Radiobutton 选择控件
行参 value 相同时复选
行参 value 不同时仅单选
"""
tk = tkinter.Tk()



R1 = tkinter.Radiobutton(tk, text = 'c', value = 1)
R2 = tkinter.Radiobutton(tk, text = 'c++', value = 2)
R3 = tkinter.Radiobutton(tk, text = 'java', value = 0)
R4 = tkinter.Radiobutton(tk, text = 'python', value = 0)

R1.pack(anchor = tkinter.W)
R2.pack(anchor = tkinter.W)
R3.pack(anchor = tkinter.W)
R4.pack(anchor = tkinter.W)



tk.mainloop()