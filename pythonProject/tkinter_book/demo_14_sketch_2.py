from tkinter import *

"画布-点击选择绘制线条的颜色"
# 定义全局变量
lastx, lasty = 0, 0
color = "black"  # 默认颜色为黑色


def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y


# 选择颜色
def setColor(newcolor):
    global color
    color = newcolor


def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y), fill=color)
    lastx, lasty = event.x, event.y


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
# 创建三个矩形框，用于绑定点击事件 选择绘制线条的颜色
id = canvas.create_rectangle((10, 10, 30, 30), fill="red")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
id = canvas.create_rectangle((10, 35, 30, 55), fill="blue")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
id = canvas.create_rectangle((10, 60, 30, 80), fill="black")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))

root.mainloop()
