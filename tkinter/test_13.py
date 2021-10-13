from tkinter.filedialog import *


"""
记事本demo
"""
class App(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.testpad = None
        self.pack()
        self.create_Widget()

    def create_Widget(self):
        menubar = Menu(root)  # 创建主菜单栏

        # 创建子菜单
        menuFile = Menu(menubar)
        menuEdit = Menu(menubar)
        menuHelp = Menu(menubar)

        # 子菜单加到菜单栏
        menubar.add_cascade(label='文件(F)', menu=menuFile)
        menubar.add_cascade(label='编辑(E)', menu=menuEdit)
        menubar.add_cascade(label='帮助(H)', menu=menuHelp)

        # 添加菜单选项
        menuFile.add_command(label='新建', accelerator='ctrl n', command=self.newfile)
        menuFile.add_command(label='打开', accelerator='ctrl o', command=self.openfile)
        menuFile.add_command(label='保存', accelerator='ctrl s', command=self.savefile)
        menuFile.add_separator()  # 添加分割线 ------
        menuFile.add_command(label='退出', accelerator='ctrl q', command=self.quit)

        root['menu'] = menubar
        # 设置快捷键
        root.bind("<Control-n>", lambda event: self.newfile())
        root.bind("<Control-o>", lambda event: self.openfile())
        root.bind("<Control-s>", lambda event: self.savefile())

        # 文本编辑区
        self.testpad = Text(root, width=60, height=30)
        self.testpad.pack()

        # 创建上下菜单
        self.contextMenu = Menu(root)
        self.contextMenu.add_command(label='背景颜色', command=self.test)

        root.bind('<3>', self.crate_context_Wigth)

    def test(self): pass

    def crate_context_Wigth(self, event):
        self.contextMenu.post(event.x_root, event.y_root)

    def openfile(self):
        self.testpad.delete('1.0', END)
        with askopenfile(title='打开文件') as f:
            self.testpad.insert(INSERT, f.read())
            self.filename = f.name

    def newfile(self):
        self.filename = asksaveasfile(title='另存为', initialfile='未命名.txt',
                                      filetypes=[('文本文档', "*.txt")],
                                      defaultextension='*.txt')
        self.savefile()

    def savefile(self):
        with open(self.filename, 'w') as f:
            c = self.testpad.get(1.0, END)
            f.write(c)

    def exit(self):
        root.quit()


if __name__ == '__main__':
    root = Tk()
    root.geometry('450x300+200+300')
    root.title('notebook')
    app = App(master=root)
    root.mainloop()



