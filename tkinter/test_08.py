import tkinter

"""
scale : 刻度控件
"""
tk = tkinter.Tk()

# 默认刻度条竖向 刻度值 1-100
scale = tkinter.Scale(tk)

def show_scale(num): var.set('当前刻度：' + num)
# 刻度条水平 刻度值 0-50 滑动步长 : resolution
scale = tkinter.Scale(tk, label='try me', from_=0, to=50, orient=tkinter.HORIZONTAL, length=200,
                      showvalue=True,tickinterval=10, resolution=0.1, command = show_scale)

var = tkinter.StringVar()
var.set('当前刻度：' + str(scale.get()))


lable = tkinter.Label(tk, textvariable = var)
scale.pack()
lable.pack()
tk.mainloop()