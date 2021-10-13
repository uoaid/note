
"""
菜单控件
"""

import tkinter as tk


def hello_handler():   pass
root = tk.Tk()
root.title("演示下拉菜单")

main_menu_bar = tk.Menu(root) # 创建一个菜单

# 创建一个子菜单
filemenu = tk.Menu(main_menu_bar, tearoff=0)
filemenu.add_command(label="打开", command=hello_handler)
filemenu.add_command(label="保存", command=hello_handler)
filemenu.add_separator()
filemenu.add_command(label="退出", command=root.quit)
# 将子菜单加入到菜单条中
main_menu_bar.add_cascade(label="文件", menu=filemenu)
# 创建一个子菜单
editmenu = tk.Menu(main_menu_bar, tearoff=0)
editmenu.add_command(label="剪切", command=hello_handler)
editmenu.add_command(label="复制", command=hello_handler)
editmenu.add_command(label="粘贴", command=hello_handler)
# 将子菜单加入到菜单条中
main_menu_bar.add_cascade(label="编辑", menu=editmenu)
# 创建一个子菜单
helpmenu = tk.Menu(main_menu_bar, tearoff=0)
helpmenu.add_command(label="关于", command=hello_handler)
# 将子菜单加入到菜单条中
main_menu_bar.add_cascade(label="帮组", menu=helpmenu)
# 将菜单添加到主窗口中
root.config(menu=main_menu_bar)
root.mainloop()


# from  tkinter import *
#
# root = Tk()
#
# var = StringVar()
# var.set('code')
# menu = OptionMenu(root, var,'c', "c++",'python')
# menu['width']
# menu.pack()
# root.mainloop()
