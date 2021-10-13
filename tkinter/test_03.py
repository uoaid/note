import tkinter

"""
text : 图片的插入
"""
root = tkinter.Tk()
text = tkinter.Text(root)
text.pack()
# 实例化图像对象的引用，以免被gc
img1 = tkinter.PhotoImage(file="1.gif")

def insert_end_text():
    text.insert('end', '尾插内容')

def insert_end_img():

    text.image_create('end', image = img1)

def del_all_text():
    text.delete(1.0,'end')

def get_all_text():
    print(text.get(1.0, 'end'))


b1 = tkinter.Button(root, text = '尾部插入', command = insert_end_text)
b2 = tkinter.Button(root, text = '尾插图片', command = insert_end_img)
b3 = tkinter.Button(root, text = '删除内容', command = del_all_text)
b4 = tkinter.Button(root, text = '获取文本', command = get_all_text)

text.window_create('insert', window = b1)
b1.pack()
b2.pack()
b3.pack()
b4.pack()


root.mainloop()