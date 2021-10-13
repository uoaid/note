import  tkinter
"""

text.delete(r,c)
r代表行从1开始， c代表索引从0开始
"""

root = tkinter.Tk()

text = tkinter.Text(root)
text.pack()


def del_all_text():
    text.delete(1.0,'end')

def get_all_text():
    print(text.get(1.0, 'end'))


b1 = tkinter.Button(root, text = '删除文本', command = del_all_text)
b2 = tkinter.Button(root, text = '获取文本', command = get_all_text)
b1.pack()
b2.pack()
root.mainloop()