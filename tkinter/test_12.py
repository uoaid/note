from  tkinter import *

"""
键鼠事件
"""

root = Tk()
root.geometry('200x200')

c1 = Canvas(root, width= 200, height=200, bg='blue')
c1.pack()


def mouseTest(event):
    print('相对父容器位置:',event.x, event.y)
    print('相对屏幕位置:',event.x_root, event.y_root)
    print('事件绑定组件',event.widget)

def dragTest(event):
    # 拖动画图
    c1.create_oval(event.x, event.y, event.x+1, event.y+1)
    print(event.x, event.y)

def keyboardTest(event):
    print("键盘keycode:{}  char:{} keysym:{}".format(event.keycode, event.char, event.keysym))

def press_a_Test(event): print('按键 a 按下')

def release_a_Test(event): print('按键 a 释放')

c1.bind("<Button-1>", mouseTest)
c1.bind('<B1-Motion>', dragTest)

root.bind("<KeyPress>", keyboardTest)
root.bind("<KeyPress-a>", press_a_Test)
root.bind("<KeyRelease-a>", release_a_Test)

def tk_event_info():
    """
【鼠标单击事件】
<Button-1>：单击鼠标左键
<Button-2>：单击鼠标中间键（如果有）
<Button-3>：单击鼠标右键
<Button-4>：向上滚动滑轮
<Button-5>：向下滚动滑轮

【鼠标双击事件】
<Double-Button-1>：鼠标左键双击
<Double-Button-2>：鼠标中键双击
<Double-Button-3>.：鼠标右键双击

【鼠标释放事件】
<ButtonRelease-1>：鼠标左键释放
<ButtonRelease-2>：鼠标中键释放
<ButtonRelease-3>：鼠标右键释放

【鼠标移动事件】
<B1-Motion>：左键拖动
<B2-Motion>：中键拖动
<B3-Motion>：右键拖动

【鼠标其他操作】
<Enter>：鼠标进入控件（放到控件上面）
<FocusIn>：控件获得焦点
<Leave>：鼠标移出控件
<FocusOut>：控件失去焦点

【键盘按下事件】
<Key>：键盘按下，事件event中的keycode,char都可以获取按下的键值
<Return>：键位绑定，回车键，其它还有<BackSpace>,<Escape>,<Left>,<Up>,<Right>,<Down>等等
【控件属性改变事件】
<Configure>：控件大小改变，新的控件大小会存储在事件event对象中的 width 和 height 属性传递，部分平台上该事件也代表控件位置改变。

【组合使用】
<Control-Shift-Alt-KeyPress-A>：同时按下Ctrl+Shift+Alt+A等4个键
<KeyPress-A>：按下键盘中的'A'键
    """

root.mainloop()