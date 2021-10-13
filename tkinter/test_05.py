import tkinter

"""
text.search
查找
"""
tk = tkinter.Tk()

text = tkinter.Text(tk)

l1 = text.insert('insert', '\nabcd')
l2 = text.index('insert')
print(l2)

position = text.search('a', 1.0, stopindex='end')
print(f"pos:{position}  bool:{bool(position)}")

text.pack()
tk.mainloop()