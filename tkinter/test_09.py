import tkinter
"""
canvas 画布控件
"""
tk = tkinter.Tk()


canvas = tkinter.Canvas(tk, width=500, height=400, bg ='blue')
img_file = tkinter.PhotoImage(file = "1.gif")
image = canvas.create_image(0,0,image = img_file)
canvas.place(x=0, y=0)



# canvas.pack()
tk.mainloop()