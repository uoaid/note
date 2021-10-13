import tkinter
from tkinter import *
"""

label 组件
from PIL import Image, ImageTk
# 通过PIL 即可正常加载 支持jpg等格式图片
img = Image.open('1.jpg')
photo = ImageTk.PhotoImage(img)
"""

img_01 = "1.gif"
root = Tk()
var = tkinter.StringVar()

def touch2(): print('touched')
# laber 显示文本, 前景:fg，背景bg, font:字体
l1 = tkinter.Label(root, text ="显示文本的", bg = "black",fg = 'white', font=("楷体", 12))
# 文本对齐方式, 默认居中(center), 东南西北: E,S,W,N
l2 = tkinter.Label(root, text ="anchor : N 上对齐",  anchor = tkinter.N , height = 2)

img = tkinter.PhotoImage(file = img_01)

l3 = tkinter.Label(root, image = img)

# width height 容器尺寸
b1 = tkinter.Button(root, text ='文本按钮',width = 30, height = 1, command = touch2)


l1.pack()
l2.pack()
l3.pack()
b1.pack()

root.mainloop()