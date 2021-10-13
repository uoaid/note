import tkinter

"""
listbox 组件
"""
tk = tkinter.Tk()

var  = tkinter.StringVar()
list = ['a', 'b', 'c', 'd']
var.set(list)

def del_active():
    # ACTIVE 表示选中
    lb1.delete(tkinter.ACTIVE)


def get_index():
    # 获取列表索引
    print(lb1.curselection(), type(lb1.curselection()))
    # print(var.get())


b1 = tkinter.Button(tk, text='delete',  command = del_active)
b2 = tkinter.Button(tk, text='get_index', command = get_index)
lb1 =tkinter.Listbox(tk, listvariable = var, selectmode = tkinter.MULTIPLE)
def run(): print('run')
lb1.bind("<1>", lambda event: run)


lb1.pack()
b1.pack()
b2.pack()

tk.mainloop()