import tkinter

"""
text : 文本框的插入
容器, 文本，图片啥都能放
"""
root = tkinter.Tk()


def add_text():
    t1.insert('insert','在光标前插入')


def add_text_end():
    t1.insert('end', "在尾部插入")


def add_text_tag():
    t1.insert('end', "自定义样式", 'tag1')


b1 = tkinter.Button(root, text = "insert", command = add_text)
b2 = tkinter.Button(root, text = "end", command = add_text_end)
b3 = tkinter.Button(root, text = "自定义插入", command = add_text_tag)

t1 = tkinter.Text(root)

b1.pack()
b2.pack()
b3.pack()
t1.pack()

# 自定义样式
t1.tag_config('tag1', background = 'yellow', foreground = 'red')

root.mainloop()